import customtkinter as ctk
from interface_functions import open_settings_wdw
import json

with open("settings.json", "r") as f:
    settings = json.load(f)
    theme = settings["visual"]["theme"]

ctk.set_appearance_mode(theme)
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Tray")
root.geometry("900x600+500+200")

settings_btn = ctk.CTkButton(
    root,
    text="Settings",
    fg_color="black",
    text_color="white",
    font=("Montserrat", 10),
    command=lambda: open_settings_wdw(root),
    cursor="hand2",
    width=100,
    height=30
)
settings_btn.place(x=1, y=1)

root.mainloop()