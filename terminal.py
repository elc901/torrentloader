from tkinter import *
import command

root = Tk()
root.title("torrentloader")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

output = Text(root, bg="#1e1e1e", fg="#00ff00", font=("Courier", 10), bd=0)
output.pack(fill=BOTH, expand=True)

pending_handler = None  # хранит функцию, ожидающую следующего ввода

def write(text):
    output.insert(END, text)
    output.see(END)

def prompt():
    output.insert(END, ">> ")
    output.mark_set("input_start", "end-1c")
    output.mark_gravity("input_start", LEFT)

def set_handler(handler):
    global pending_handler
    pending_handler = handler
    output.mark_set("input_start", "end-1c")
    output.mark_gravity("input_start", LEFT)

prompt()

def run(event):
    global pending_handler
    line = output.get("input_start", "end-1c").strip()
    output.insert(END, "\n")

    if pending_handler:
       #передача ввода
        handler = pending_handler
        pending_handler = None
        handler(line)
        prompt()
    elif line == "clear":
        output.delete(1.0, END)
        prompt()
    elif line == "clg":
        command.language(write, set_handler)
        
    else:
        write(f"unknown command: {line}\n")
        prompt()

    output.see(END)
    return "break"

output.bind("<Return>", run)
output.focus_force()
root.mainloop()