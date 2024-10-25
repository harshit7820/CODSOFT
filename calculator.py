import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(0, 0)

input_text = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(expand=True, fill="both")

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=0, bg="#eee", justify="right")
input_field.grid(row=0, column=0, ipadx=8, sticky="nsew")
input_frame.grid_rowconfigure(0, weight=1)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

# First row
clear = tk.Button(button_frame, text="C", font=('arial', 18, 'bold'), command=lambda: btn_clear())
clear.grid(row=0, column=0, sticky="nsew")
divide = tk.Button(button_frame, text="/", font=('arial', 18, 'bold'), command=lambda: btn_click("/"))
divide.grid(row=0, column=1, sticky="nsew")
multiply = tk.Button(button_frame, text="*", font=('arial', 18, 'bold'), command=lambda: btn_click("*"))
multiply.grid(row=0, column=2, sticky="nsew")
minus = tk.Button(button_frame, text="-", font=('arial', 18, 'bold'), command=lambda: btn_click("-"))
minus.grid(row=0, column=3, sticky="nsew")

# Second row
seven = tk.Button(button_frame, text="7", font=('arial', 18, 'bold'), command=lambda: btn_click(7))
seven.grid(row=1, column=0, sticky="nsew")
eight = tk.Button(button_frame, text="8", font=('arial', 18, 'bold'), command=lambda: btn_click(8))
eight.grid(row=1, column=1, sticky="nsew")
nine = tk.Button(button_frame, text="9", font=('arial', 18, 'bold'), command=lambda: btn_click(9))
nine.grid(row=1, column=2, sticky="nsew")
add = tk.Button(button_frame, text="+", font=('arial', 18, 'bold'), command=lambda: btn_click("+"))
add.grid(row=1, column=3, sticky="nsew")

# Third row
four = tk.Button(button_frame, text="4", font=('arial', 18, 'bold'), command=lambda: btn_click(4))
four.grid(row=2, column=0, sticky="nsew")
five = tk.Button(button_frame, text="5", font=('arial', 18, 'bold'), command=lambda: btn_click(5))
five.grid(row=2, column=1, sticky="nsew")
six = tk.Button(button_frame, text="6", font=('arial', 18, 'bold'), command=lambda: btn_click(6))
six.grid(row=2, column=2, sticky="nsew")
equal = tk.Button(button_frame, text="=", font=('arial', 18, 'bold'), command=lambda: btn_equal())
equal.grid(row=2, column=3, rowspan=2, sticky="nsew")

# Fourth row
one = tk.Button(button_frame, text="1", font=('arial', 18, 'bold'), command=lambda: btn_click(1))
one.grid(row=3, column=0, sticky="nsew")
two = tk.Button(button_frame, text="2", font=('arial', 18, 'bold'), command=lambda: btn_click(2))
two.grid(row=3, column=1, sticky="nsew")
three = tk.Button(button_frame, text="3", font=('arial', 18, 'bold'), command=lambda: btn_click(3))
three.grid(row=3, column=2, sticky="nsew")

# Fifth row
zero = tk.Button(button_frame, text="0", font=('arial', 18, 'bold'), command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2, sticky="nsew")
decimal = tk.Button(button_frame, text=".", font=('arial', 18, 'bold'), command=lambda: btn_click("."))
decimal.grid(row=4, column=2, sticky="nsew")

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
