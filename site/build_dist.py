import json, re, shutil, os

data = json.load(open("/Users/WyattLapaillerieEngone/Desktop/M13/site/chapters.json", encoding="utf-8"))
data_json = json.dumps(data, ensure_ascii=False)

# dist/index.html lives one directory under site/, so audio paths need the
# "assets/voices/" prefix instead of build_site.py's "audio/voices/" — copy
# the m4a files across so the relative paths resolve.
DIST_ROOT = "/Users/WyattLapaillerieEngone/Desktop/M13/site/dist"
os.makedirs(os.path.join(DIST_ROOT, "assets", "voices"), exist_ok=True)
for c in data["chapters"]:
    src = f"/Users/WyattLapaillerieEngone/Desktop/M13/site/audio/voices/chapitre-{c['num']:02d}.m4a"
    dst = os.path.join(DIST_ROOT, "assets", "voices", f"chapitre-{c['num']:02d}.m4a")
    if os.path.exists(src):
        shutil.copyfile(src, dst)

AUDIO_MAP = {c["num"]: f"assets/voices/chapitre-{c['num']:02d}.m4a" for c in data["chapters"]}
audio_map_json = json.dumps(AUDIO_MAP)

html_source = open("/Users/WyattLapaillerieEngone/Desktop/M13/site/build_site.py", encoding="utf-8").read()
# Extract the html_template string out of build_site.py's triple-quoted block
m = re.search(r'html_template = """(.*)"""\n\nout = ', html_source, re.DOTALL)
template = m.group(1)
# The source file has \\' (double backslash) so Python's own triple-quoted
# string parser collapses it to \' for the JS output; since we're reading
# the .py file as raw text here, that collapse never happens, so do it now.
template = template.replace("\\\\'", "\\'")

out = template.replace("__DATA__", data_json).replace("__AUDIOMAP__", audio_map_json)

with open(os.path.join(DIST_ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Written", len(out), "bytes")
