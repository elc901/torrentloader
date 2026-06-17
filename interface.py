import customtkinter as ctk
import interface_functions
import json
import functions
with open("settings.json", "r") as f:
    settings = json.load(f)
    theme = settings["visual"]["theme"]
    size = settings["visual"]["size"]

ctk.set_appearance_mode(theme)
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(size)

root = ctk.CTk()
root.title("Tray")
root.geometry("900x600+500+200")


settings_btn = ctk.CTkButton(
    root,
    text="Settings",
    fg_color="black",
    text_color="white",
    font=("Montserrat", 10),
    command=lambda: interface_functions.open_settings_wdw(root),
    cursor="hand2",
    width=100,
    height=30
)
settings_btn.place(x=10, y=10)

exit_btn = ctk.CTkButton(
    root,
    text="Exit",
    fg_color="black",
    text_color="white",
    font=("Montserrat", 10),
    command=root.destroy,
    cursor="hand2",
    width=100,
    height=30
)
exit_btn.place(x=790, y=560)
root.mainloop()