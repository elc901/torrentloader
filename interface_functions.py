import json
import customtkinter as ctk

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


def open_settings_wdw(parent):
    global open_window, theme_switch_var
    if open_window is not None and open_window.winfo_exists():
        open_window.lift()
        open_window.focus()
        return

    with open("settings.json", "r") as f:
        settings = json.load(f)
        current_theme = settings["visual"]["theme"]

    open_window = ctk.CTkToplevel(parent)  
    open_window.title("Settings")
    open_window.geometry("550x450+100+200")
    open_window.protocol("WM_DELETE_WINDOW", on_close)

    # Переключатель темы
    theme_switch_var = ctk.StringVar(value="on" if current_theme == "dark" else "off")
    theme_switch = ctk.CTkSwitch(
        open_window,
        text="Dark theme",
        variable=theme_switch_var,
        onvalue="on",
        offvalue="off",
        command=change_theme
    )
    theme_switch.place(x=50, y=20)


    
    close_btn = ctk.CTkButton(open_window, text="Close", command=on_close)
    close_btn.place(x=200, y=420)