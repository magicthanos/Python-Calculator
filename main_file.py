import tkinter as tk, pyglet

#starting properties
root = tk.Tk()
root.title('Python Calculator')
root.resizable(False, False)

#font file
pyglet.font.add_file(r'.\TTLM.ttf')

#frames used
text_frame = tk.Frame(root)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)


#make extra buttons (frame = Frame to be added to, st = string of button)
def make_button(frame, st):
    return tk.Button(frame,
                     text=str(st),
                     width=4,
                     fg='#FFEEDB',
                     bg='#BA3B46',
                     relief='groove',
                     font=('Titillium Web Regular', 25),
                     command=lambda: string_concat(st))


#entry box for calculations
text = tk.StringVar()
expr = ''
entry_box = tk.Entry(text_frame,
                     textvariable=text,
                     justify='right',
                     font=('Titillium Web Regular', 26),
                     bg='#FFEEDB',
                     fg='#BA3B46')


#makes the equation
def string_concat(char):
    global expr
    expr += str(char)
    text.set(expr)


#clear the equation
def clear_string():
    global expr
    expr = ''
    text.set('')


#evaluates the equation
def evaluate():
    global text
    global expr
    try:
        expr = str(eval(expr))
        text.set(expr)
    except:
        expr = ''
        text.set('')


#makes the buttons from 1-9 (reversed)
buttons = [make_button(frame2, i) for i in range(9, -1, -1)]

#extra buttons
button_clear = tk.Button(frame1,
                         text='Clear',
                         width=4,
                         fg='#FFEEDB',
                         bg='#BA3B46',
                         relief='groove',
                         font=('Titillium Web Regular', 25),
                         command=lambda: clear_string())
button_enter = tk.Button(frame3,
                         text='Enter',
                         width=4,
                         fg='#FFEEDB',
                         bg='#BA3B46',
                         relief='groove',
                         font=('Titillium Web Regular', 25),
                         command=lambda: evaluate())
button_div = make_button(frame1, '/')
button_multi = make_button(frame2, '*')
button_minus = make_button(frame2, '-')
button_plus = make_button(frame2, '+')
button_0 = make_button(frame3, 0)
button_dot = make_button(frame3, '.')

#places the buttons in the correct place
count = 0
for i in range(1, 4):
    for j in range(2, -1, -1):
        buttons[count].grid(row=i, column=j, ipadx=10, ipady=10)
        count += 1

button_clear.grid(row=0, column=0, ipadx=112, ipady=10)
button_div.grid(row=0, column=1, ipadx=10, ipady=10)
button_multi.grid(row=1, column=3, ipadx=10, ipady=10)
button_minus.grid(row=2, column=3, ipadx=10, ipady=10)
button_plus.grid(row=3, column=3, ipadx=10, ipady=10)
button_0.grid(row=0, column=0, ipadx=61, ipady=10)
button_dot.grid(row=0, column=1, ipadx=10, ipady=10)
button_enter.grid(row=0, column=2, ipadx=10, ipady=10)

#shows everything
entry_box.grid()
text_frame.grid()
frame1.grid()
frame2.grid()
frame3.grid()
frame4.grid(column=1)

if __name__ == "__main__":
    root.mainloop()