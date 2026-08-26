import re, html, json

src = open("/Users/WyattLapaillerieEngone/Desktop/M13/build_pdf.py", encoding="utf-8").read()

def clean(s):
    s = s.replace("<br/>", "\n")
    s = html.unescape(s)
    return s

# Extract everything from "S = []" to "doc.build(S)"
body = src.split("S = []", 1)[1].split("doc.build(S)", 1)[0]

# Tokenize top-level calls in order: chap(...), p("..."), name("..."), S.append(Paragraph("...", style)), S.append(PageBreak())
# We scan line by line, grouping multi-line string literals.

chapters = []
current = None

# Find all calls of form funcname( ...args... ) possibly spanning many lines,
# where args are python string literals concatenated with '+' implicitly (adjacent string literals)
# We use a regex that captures balanced parens is hard; instead split on top-level call boundaries
# by finding patterns: p(\n...\n)  name(\n...\n)  chap(\n...\n)  S.append(Paragraph(\n...\n))

pattern = re.compile(
    r'(?P<fn>^p|^name|^chap)\(\s*(?P<args>.*?)\)\s*$|'
    r'S\.append\(Paragraph\(\s*(?P<pargs>.*?),\s*\w+\)\)\s*$|'
    r'S\.append\(rule\(\)\)|'
    r'S\.append\(PageBreak\(\)\)',
    re.MULTILINE | re.DOTALL
)

# Simpler: split body into statements by finding lines that start a new top-level call
lines = body.split("\n")
buf = []
depth = 0
statements = []
for line in lines:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        continue
    buf.append(line)
    depth += line.count("(") - line.count(")")
    if depth <= 0:
        statements.append("\n".join(buf))
        buf = []
        depth = 0

def extract_strings(s):
    # extract all "...": python double-quoted strings, concatenation implied
    return "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', s))

for stmt in statements:
    s = stmt.strip()
    if s.startswith("chap("):
        args = s[len("chap("):-1]
        parts = [a.strip() for a in re.split(r',(?![^"]*"(?:[^"\\]|\\.)*(?:\s*"|$))', args)]
        # crude split by comma at top level outside quotes
        # fallback: use regex to find num and title
        m = re.match(r'\s*(\d+)\s*,\s*(.*)', args)
        num = int(m.group(1))
        rest = m.group(2)
        # rest may be: "TITLE"   or "TITLE", "TAG"
        strs = re.findall(r'"((?:[^"\\]|\\.)*)"', rest)
        title = clean(strs[0]) if strs else ""
        tag = clean(strs[1]) if len(strs) > 1 else None
        if current:
            chapters.append(current)
        current = {"num": num, "title": title, "tag": tag, "blocks": []}
    elif s.startswith("p("):
        text = clean(extract_strings(s))
        if current is not None:
            current["blocks"].append({"type": "p", "text": text})
    elif s.startswith("name("):
        text = clean(extract_strings(s))
        if current is not None:
            current["blocks"].append({"type": "name", "text": text})
    elif s.startswith("S.append(Paragraph("):
        # machine style / label style blocks, or chapter headers (which we skip, already handled by chap())
        strs = re.findall(r'"((?:[^"\\]|\\.)*)"', s)
        if strs:
            text = clean(strs[0])
            # skip meta lines like PROJECT-M13 / Chapitre N / chapter_title already in chap()
            if text not in ("PROJECT-M13",) and not re.match(r'^Chapitre \d+$', text) and current is not None:
                # heuristic: only include if looks like machine text or dialogue tag or label
                if len(text) > 0:
                    current["blocks"].append({"type": "machine", "text": text})
    # ignore rule(), PageBreak(), etc.

if current:
    chapters.append(current)

# Remove duplicate leading chapter-header-ish machine blocks (title/label already used as chap title)
cleaned_chapters = []
for c in chapters:
    blocks = c["blocks"]
    cleaned_chapters.append({"num": c["num"], "title": c["title"], "tag": c["tag"], "blocks": blocks})

print(json.dumps({"chapters": cleaned_chapters}, ensure_ascii=False)[:2000])
print("---")
print("Total chapters extracted:", len(cleaned_chapters))
for c in cleaned_chapters:
    print(c["num"], c["title"], "blocks:", len(c["blocks"]))

with open("/Users/WyattLapaillerieEngone/Desktop/M13/site/chapters.json", "w", encoding="utf-8") as f:
    json.dump({"chapters": cleaned_chapters}, f, ensure_ascii=False)
