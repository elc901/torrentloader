from tkinter import *
import command

root = Tk()
root.title("torrentloader")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

output = Text(root, bg="#1e1e1e", fg="#00ff00", font=("Courier", 10), bd=0)
output.pack(fill=BOTH, expand=True)

def prompt():
    output.insert(END, ">> ")
    output.mark_set("input_start", "end-1c")
    output.mark_gravity("input_start", LEFT)

prompt()

def run(event):
    line = output.get("input_start", "end-1c").strip()
    output.insert(END, "\n")

    if line == "clear":
        output.delete(1.0, END)
    elif line == "hello":
        output.insert(END, f"{command.hello()}\n")
    elif line == "download":
        output.insert(END, f"{command.download()}\n")
    else:
        output.insert(END, f"unknown command: {line}\n")

    prompt()
    output.see(END)
    return "break"

output.bind("<Return>", run)
output.focus_force()
root.mainloop()