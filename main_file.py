import tkinter as tk, pyglet
from tkinter import ttk

root = tk.Tk()
root.title('Python Calculator')
root.geometry('300x100')
frame = ttk.Frame(root, padding=10)

#makes the buttons from 1-9 (reversed)

pyglet.font.add_file(r'.\TTLM.ttf')

style = ttk.Style()
style.configure("Nums.TButton",
                background='white',
                foreground='white',
                font=('Titillium Web Regular', 10))
label = ttk.Label(font=('Titillium Web Regular', 10),
                  text='This is a test string 123').grid(row=10, column=10)
buttons = [
    ttk.Button(frame, text=str(i), width=4, style="Nums.TButton")
    for i in range(9, -1, -1)
]

#places the numbers in the correct order
count = 0
for i in range(3):
    for j in range(2, -1, -1):
        buttons[count].grid(row=i, column=j)
        count += 1
frame.grid()

if __name__ == "__main__":
    root.mainloop()
