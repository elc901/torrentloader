import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
def open_settings_wdw(parent):
    setting_wdw = ctk.CTkToplevel(parent) 
    setting_wdw.title("Settings")
    setting_wdw.geometry("300x450")
    
    label = ctk.CTkLabel(setting_wdw, text="Settings", font=("Montserrat", 16))
    label.pack(pady=20)
    
    close_btn = ctk.CTkButton(setting_wdw, text="Close", command=setting_wdw.destroy)
    close_btn.pack(pady=10)