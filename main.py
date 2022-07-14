from tkinter import *

def put_digit(digit):
    value = calc.get() + str(digit)
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert(0, value)

def put_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '/' in value or '*' in value or '-' in value:
        calculator()
        value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, value+operation)

def calculator():
    value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, eval(value))

def deli():
    calc.delete(0, 'end')
    calc.insert(0, '0')




def digitButton(digit):
    return Button(text=digit,bd = 5, font=('Arial', 13), command=lambda: put_digit(digit))

def operationButton(operation):
    return Button(text=operation, bd = 5, font=('Arial', 13), fg = 'red', command=lambda: put_operation(operation))

def calcButton(caluc):
    return Button(text=caluc, bd = 5, font=('Arial', 13), fg = 'red', command=calculator)



win = Tk()
win.geometry('240x270')
win.config(bg='black')
win.title = 'Калькулятор'

calc = Entry(win, justify=RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)


digitButton(1).grid(row=1, column=0, stick='wens', padx=5, pady=5)
digitButton(2).grid(row=1, column=1, stick='wens', padx=5, pady=5)
digitButton(3).grid(row=1, column=2, stick='wens', padx=5, pady=5)
digitButton(4).grid(row=2, column=0, stick='wens', padx=5, pady=5)
digitButton(5).grid(row=2, column=1, stick='wens', padx=5, pady=5)
digitButton(6).grid(row=2, column=2, stick='wens', padx=5, pady=5)
digitButton(7).grid(row=3, column=0, stick='wens', padx=5, pady=5)
digitButton(8).grid(row=3, column=1, stick='wens', padx=5, pady=5)
digitButton(9).grid(row=3, column=2, stick='wens', padx=5, pady=5)
digitButton(0).grid(row=4, column=0, stick='wens', padx=5, pady=5)

operationButton('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
operationButton('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
operationButton('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
operationButton('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)


calcButton('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

Button(text='C', bd = 5, font=('Arial', 13), fg = 'red', command=deli).grid(row=4, column=1, stick='wens', padx=5, pady=5)



for i in range(4):
    win.grid_columnconfigure(i, minsize=60)
for i in range(4):
    win.grid_rowconfigure(i+1, minsize=60)



win.mainloop()