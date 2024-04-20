import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    km_input = entry_int.get()
    mile_output = km_input * 0.621371
    output_string.set(str(round(mile_output, 2)))


# window
window = ttk.Window(themename='darkly')
window.title('Converter')
window.geometry('400x150')

# title
title_label = ttk.Label(master=window, text='Convert kilometer to miles', font='calibri 18 bold')
title_label.pack()

input_frame = ttk.Frame(master=window)
entry_int = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)

entry.pack(pady=5)
button.pack()
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='calibri 14',
                         textvariable=output_string)
output_label.pack()

window.mainloop()
