import os
import json


user_path = os.path.expanduser("~")


roblox_path = os.path.join(user_path, "AppData", "Local", "Roblox", "Versions", "version-3243b6d003cf4642")
client_settings_path = os.path.join(roblox_path, "ClientSettings")


if not os.path.exists(client_settings_path):
    os.makedirs(client_settings_path)


json_file_path = os.path.join(client_settings_path, "ClientAppSettings.json")


json_content = {
    "FFlagHandleAltEnterFullscreenManually": "False",
    "DFIntTaskSchedulerTargetFps": "9999",
    "FFlagDebugGraphicsPreferD3D11": "True"
}


with open(json_file_path, 'w') as json_file:
    json.dump(json_content, json_file, indent=2)

print(f"Fix Completed successfully")
