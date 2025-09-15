import tkinter as tk

# Function for button click
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(result)
        except Exception:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    elif text == "⌫":  # Backspace button
        screen_var.set(screen_var.get()[:-1])
    else:
        screen_var.set(screen_var.get() + text)

# Function for keyboard input
def key_press(event):
    if event.char.isdigit() or event.char in "+-*/.":
        screen_var.set(screen_var.get() + event.char)
    elif event.keysym == "Return":
        click(type("Event", (object,), {"widget": equals_btn}))
    elif event.keysym == "BackSpace":
        screen_var.set(screen_var.get()[:-1])

# Main window
root = tk.Tk()
root.title("Calculator by Mohit")
root.geometry("340x450")
root.config(bg="#f7f1e3")
root.resizable(False, False)

# Screen
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font=("Arial", 20, "bold"),
                  bg="white", fg="black", justify="right")
screen.pack(fill="x", ipadx=8, pady=10, padx=10)
screen.focus_set()  # Focus for keyboard input

# Buttons frame
frame = tk.Frame(root, bg="#dff9fb")
frame.pack()

# Button layout
buttons = [
    ("7", "#ecf0f1"), ("8", "#ecf0f1"), ("9", "#ecf0f1"), ("/", "#f39c12"),
    ("4", "#ecf0f1"), ("5", "#ecf0f1"), ("6", "#ecf0f1"), ("*", "#f39c12"),
    ("1", "#ecf0f1"), ("2", "#ecf0f1"), ("3", "#ecf0f1"), ("-", "#f39c12"),
    ("0", "#ecf0f1"), (".", "#ecf0f1"), ("=", "#27ae60"), ("+", "#f39c12"),
    ("C", "#e74c3c"), ("⌫", "#e67e22")
]

# Create buttons
row = 0
col = 0
for (text, color) in buttons:
    btn = tk.Button(frame, text=text, font=("Arial", 15, "bold"), width=5, height=2,
                    bg=color, fg="black", activebackground="#bdc3c7")
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    
    if text == "=":
        equals_btn = btn  # reference for keyboard Enter key
    
    col += 1
    if col == 4:
        col = 0
        row += 1

# Bind keyboard
root.bind("<Key>", key_press)

root.mainloop()
