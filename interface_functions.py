import json
import customtkinter as ctk
import functions  

def open_settings_wdw(parent):
    # обращение  к переменным через functions.
    if functions.open_window is not None and functions.open_window.winfo_exists():
        functions.open_window.lift()
        functions.open_window.focus()
        return

    with open("settings.json", "r") as f:
        settings = json.load(f)
        current_theme = settings["visual"]["theme"]

    functions.open_window = ctk.CTkToplevel(parent)  
    functions.open_window.title("Settings")
    functions.open_window.geometry("300x450+100+200")
    functions.open_window.protocol("WM_DELETE_WINDOW", functions.on_close)
# переключатель  для переключения темы
    functions.theme_switch_var = ctk.StringVar(value="on" if current_theme == "dark" else "off")
    theme_switch = ctk.CTkSwitch(
        functions.open_window,
        text="Dark theme",
        variable=functions.theme_switch_var,
        onvalue="on",
        offvalue="off",
        command=functions.change_theme
    )
    theme_switch.place(x=50, y=20)
# конец
# кнопка для изменения размера
    change_size1 = ctk.CTkButton(function.)
    close_btn = ctk.CTkButton(functions.open_window, text="Close", command=functions.on_close)
    close_btn.place(x=75, y=420)

size_100 =  # список размеров для интерфейса