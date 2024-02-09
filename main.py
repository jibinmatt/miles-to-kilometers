import tkinter as tk
import ttkbootstrap as ttk

def convert():
  mile_input = entry_int.get()
  km_output = mile_input * 1.60934
  output = "{} Kms"
  output_string.set(output.format(km_output))

# main window
window = ttk.Window(themename = 'darkly')
window.title('Miles to Kilometers')
window.geometry('400x300')

## main UI - title, input field, output field
# title
title_label = ttk.Label(
  master = window, 
  text = 'Miles to Kilometers', 
  font = 'Calibri 24 bold'
)
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text ='Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 20)

# output field
output_string = tk.StringVar()
output_label = ttk.Label(
  master = window, 
  text = 'Output', 
  font = 'Calibri 20', 
  textvariable = output_string
)
output_label.pack(pady = 20)

# running the app
window.mainloop()