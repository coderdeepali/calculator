import tkinter as tk
from tkinter import font

calculation = ""

def add_to_calculation(symbol):
    global calculation
    if symbol == "=":
        evaluate_calculation()
    elif symbol == "DEL":
        remove_last_digit()
    elif symbol == "AC":
        clear_field()
    else:
        calculation += str(symbol)
        update_display()

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        update_display()
    except:
        clear_field()
        text_result.insert("1.0", "Error")

def clear_field():
    global calculation
    calculation = ""
    update_display()

def remove_last_digit():
    global calculation
    calculation = calculation[:-1]
    update_display()

def update_display():
    text_result.delete("1.0", "end")
    text_result.insert("1.0", calculation)

root = tk.Tk()
root.geometry("300x400")
root.title("Modern Calculator")

root.configure(bg="#2C3E50")  

text_result = tk.Text(root, height=2, width=16, font=("Helvetica", 24), bg="#34495E", fg="#ECF0F1")
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_style = {
    "font": ("Helvetica", 14),
    "width": 5,
    "height": 2,
    "bg": "#3498DB",
    "fg": "#FFFFFF",
    "relief": "raised",
    "borderwidth": 3
}
button_style_ac_del_equal = {
    **button_style,
    "bg": "#E74C3C"
}


buttons = [
    ("AC", "DEL", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", "00", ".", "=")
]

for row_val, row_buttons in enumerate(buttons, start=1):
    for col_val, button in enumerate(row_buttons):
        if button in {"=", "DEL", "AC"}:
            tk.Button(root, text=button, command=lambda b=button: add_to_calculation(b), **button_style_ac_del_equal).grid(row=row_val, column=col_val, padx=5, pady=5)
        else:
            tk.Button(root, text=button, command=lambda b=button: add_to_calculation(b), **button_style).grid(row=row_val, column=col_val, padx=5, pady=5)
text_result.config(state="normal", bg="#34495E", fg="#ECF0F1", insertbackground="#ECF0F1")

for i in range(1, 6):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
