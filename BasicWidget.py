import tkinter as tk
from tkinter import ttk


def btn_func():
    print(entry.get())


# window
master = tk.Tk()
master.title('Widgets')
master.geometry('1280x720')

# tk text
text = tk.Text(master=master)
text.pack()

# ttk label
label = ttk.Label(master=master, text='Test')
label.pack()

entry = ttk.Entry(master=master)
entry.pack()

button = ttk.Button(master=master, text='button', command=btn_func)
button.pack()

master.mainloop()
