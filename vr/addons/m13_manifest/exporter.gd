@tool
extends EditorExportPlugin
# Déclarations Meta Quest : catégorie VR du lanceur, « focus aware », casques compatibles.

func _get_name() -> String:
	return "M13Manifest"

func _supports_platform(platform: EditorExportPlatform) -> bool:
	return platform.get_os_name() == "Android"

func _get_android_manifest_activity_element_contents(platform: EditorExportPlatform, debug: bool) -> String:
	return '<meta-data android:name="com.oculus.vr.focusaware" android:value="true" />\n' \
		+ '<intent-filter>\n<action android:name="android.intent.action.MAIN" />\n<category android:name="com.oculus.intent.category.VR" />\n</intent-filter>\n'

func _get_android_manifest_application_element_contents(platform: EditorExportPlatform, debug: bool) -> String:
	return '<meta-data android:name="com.oculus.supportedDevices" android:value="quest2|questpro|quest3|quest3s" />\n'
