from tkinter import *
import command

root = Tk()
root.title("torrentloader")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

output = Text(root, bg="#1e1e1e", fg="#00ff00", font=("Courier", 10), bd=0)
output.pack(fill=BOTH, expand=True)

pending_handler = None

def write(text): # аналог print для кастомнгоо интерфекйа
    output.insert(END, text)
    output.see(END)

def prompt():
    output.insert(END, ">> ")
    output.mark_set("input_start", "end-1c")
    output.mark_gravity("input_start", LEFT)
write("help for commands    \n")
write("help для комманд     \n")
prompt()

def reset_prompt(): # обновляет позициб input_start и обновляет prompt
    prompt()
    output.mark_set("input_start", "end-1c")
    output.mark_gravity("input_start", LEFT)

def run(event):
    global pending_handler
    line = output.get("input_start", "end-1c").strip()
    output.insert(END, "\n")
    if pending_handler:
        pending_handler(line, write)
        pending_handler = None
        prompt()
    elif line == "clear":
        output.delete(1.0, END)
        prompt()
    elif line == "clg": # выбор языка
        write("Your Language (just write 'en' or 'ru') ->  ")
        output.mark_set("input_start", "end-1c")
        output.mark_gravity("input_start", LEFT)
        pending_handler = command.language
    elif line == "help": # просто вывод команд 
        command.help(write)
        reset_prompt()
    elif line == "exit": # выход
        exit()
    elif line == "about":
        command.about_programm(write)
        reset_prompt()
    else:
        write(f"unknown command: {line}\n")
        prompt()

    output.see(END)
    return "break"

output.bind("<Return>", run)
output.focus_force()
root.mainloop()