import customtkinter as ctk
import json
#with open("settings.json", "r") as f:
    #settings = json.load(f)

#with open("settings.json", "w") as f:
    #json.dump()
open_window = None  

def on_close():
    global open_window
    if open_window is not None:
        open_window.destroy()
        open_window = None

def open_settings_wdw(parent):
    global open_window
    
    
    if open_window is not None and open_window.winfo_exists():
        open_window.lift()
        open_window.focus()
        return
    
    
    open_window = ctk.CTkToplevel(parent)  
    open_window.title("Settings")
    open_window.geometry("300x450+100+200")
    
    
    open_window.protocol("WM_DELETE_WINDOW", on_close)
    
    
    close_btn = ctk.CTkButton(open_window, text="Save and close", command=on_close)
    close_btn.place(x=75, y=420)  