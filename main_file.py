import tkinter as tk, pyglet

#font file
pyglet.font.add_file(r'.\TTLM.ttf')


#make extra buttons (width = width of button, st = text of button, frame = Frame to be added to)
def make_button(frame, st, width):
    return tk.Button(frame,
                     text=str(st),
                     width=width,
                     fg='#FFEEDB',
                     bg='#BA3B46',
                     font=('Titillium Web Regular', 25))


root = tk.Tk()
root.title('Python Calculator')
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

#makes the buttons from 1-9 (reversed)
buttons = [make_button(frame1, i, 4) for i in range(9, -1, -1)]

#extra buttons
button_0 = make_button(frame2, 0, 8)
button_dot = make_button(frame2, '.', 4)

#places the buttons in the correct place
count = 0
for i in range(3):
    for j in range(2, -1, -1):
        buttons[count].grid(row=i, column=j, ipadx=10, ipady=10)
        count += 1
button_0.grid(row=0, column=0, ipadx=20, ipady=10)
button_dot.grid(row=0, column=1, ipadx=15, ipady=10)

frame1.grid()
frame2.grid()

if __name__ == "__main__":
    root.mainloop()
