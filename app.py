import os
import json

# Ottieni il percorso della directory dell'utente
user_path = os.path.expanduser("~")

# Definisci il percorso completo
roblox_path = os.path.join(user_path, "AppData", "Local", "Roblox", "Versions", "version-3243b6d003cf4642")
client_settings_path = os.path.join(roblox_path, "ClientSettings")

# Controlla se la cartella ClientSettings esiste, se no, creala
if not os.path.exists(client_settings_path):
    os.makedirs(client_settings_path)

# Definisci il percorso del file JSON
json_file_path = os.path.join(client_settings_path, "ClientAppSettings.json")

# Contenuto da scrivere nel file JSON
json_content = {
    "FFlagHandleAltEnterFullscreenManually": "False",
    "DFIntTaskSchedulerTargetFps": "9999",
    "FFlagDebugGraphicsPreferD3D11": "True"
}

# Scrivi il contenuto nel file JSON
with open(json_file_path, 'w') as json_file:
    json.dump(json_content, json_file, indent=2)

print(f"File creato con successo in: {json_file_path}")
