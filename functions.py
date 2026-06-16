import customtkinter as ctk
import json

open_window = None  
theme_switch_var = None

def on_close():
    global open_window
    if open_window is not None:
        open_window.destroy()
        open_window = None

def change_theme():
    global theme_switch_var
    
    with open("settings.json", "r") as f:
        settings = json.load(f)
    
    if theme_switch_var.get() == "on":
        settings["visual"]["theme"] = "dark"
        ctk.set_appearance_mode("dark")
    else:
        settings["visual"]["theme"] = "light"
        ctk.set_appearance_mode("light")
    
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)

