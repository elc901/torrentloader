import customtkinter as ctk
from functions import *

# Настройка темы
ctk.set_appearance_mode("light")  # или "dark"
ctk.set_default_color_theme("blue")

# Главное окно
root = ctk.CTk()
root.title("Tray")
root.geometry("900x600")

settings_btn = ctk.CTkButton(
    root,
    text="Settings",
    fg_color="black",      # вместо bg
    text_color="white",    # вместо fg
    font=("Montserrat", 10),
    command=lambda: open_settings_wdw(root),
    cursor="hand2"
)
settings_btn.place(x=1, y=1)

root.mainloop()