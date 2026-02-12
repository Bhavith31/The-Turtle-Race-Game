import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(root, font=("bold",20), bg="grey", fg="white",
                 bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+']

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

row = 1
col = 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("bold", 14),
        width=5,
        height=2,
        bg="green" if b in "+-*/=" else "blue",
        fg="white",
        bd=0
    ).grid(row=row, column=col, padx=6, pady=6)

    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(
    root,
    text="C",
    command=clear,
    font=("bold", 14),
    width=22,
    height=2,
    bg="red",
    fg="white",
    bd=0
).grid(row=row, column=0, columnspan=4, pady=8)

root.mainloop()