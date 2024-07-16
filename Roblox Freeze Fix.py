import os
import json
import shutil
import tkinter as tk
from tkinter import messagebox
import win32com.client

def main():
    roblox_path = "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Roblox".format(os.getlogin())
    shortcut_name = "Roblox Player.lnk"
    shortcut_path = os.path.join(roblox_path, shortcut_name)
    
    target_path = get_target_path(shortcut_path)
    
    if target_path:
        target_dir = os.path.dirname(target_path)
        clientsettings_path = os.path.join(target_dir, "ClientSettings")
        os.makedirs(clientsettings_path, exist_ok=True)
        
        json_content = {
            "FFlagHandleAltEnterFullscreenManually": "False",
            "DFIntTaskSchedulerTargetFps": "9999",
            "FFlagDebugGraphicsPreferD3D11": "True"
        }
        
        json_file_path = os.path.join(clientsettings_path, "ClientAppSettings.json")
        
        with open(json_file_path, 'w') as json_file:
            json.dump(json_content, json_file, indent=4)
        
        show_success_message()
        
    else:
        print(f"Shortcut '{shortcut_name}' not found in: {roblox_path}")

def get_target_path(shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    return shortcut.TargetPath if shortcut else None

def show_success_message():
    root = tk.Tk()
    root.withdraw()
    
    messagebox.showinfo("Operation Completed", "The JSON file has been successfully created in the original shortcut directory.")
    
    root.destroy()

if __name__ == "__main__":
    main()
