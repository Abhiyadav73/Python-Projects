import tkinter as tk
#from tkinter import ttk as tkkk
import ttkbootstrap as ttk
import random

def convert():
    mile_input=entry_int.get()
    kmop=float(mile_input)*1.61
    output_string.set(round(kmop,3))
    km.set('Km')

def convert_2():
    km_input=entry_int_2.get()
    mileop=float(km_input) * 0.621371
    output_string_2.set(round(mileop,3))
    mile.set('Miles')


#style.configure('Rounded.TButton', relief='flat', padding=5, font=('Helvetica', 12), borderwidth=2, focusthickness=0)

#window
themes=['journal','minty','sandstone','darkly','pulse','united','solar','superhero','vapor','lumen','pulse','yeti']
random_var=random.randrange(0,len(themes))
#print(themes[random_var])
window=ttk.Window(themename=themes[random_var])
window.title('Converter')
window.geometry('600x350')

# Configure the button style
style=ttk.Style()
style.theme_use(themes[random_var])

#window title
window_label=ttk.Label(master=window,text='Distance Converter',font='Calibri 30 bold').pack(pady=6)

#title
title_label=ttk.Label(master=window,text='Miles to Kilometers',font='Calibri 24 bold')
title_label.pack()

#input file
input_frame=ttk.Frame(master=window)
entry_int=tk.IntVar()
entry=ttk.Entry(master=input_frame,textvariable=entry_int)
button=ttk.Button(master=input_frame,text='Convert',command=convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_frame=ttk.Frame(master=window)
output_string=tk.StringVar()
km=tk.StringVar()
output_label=ttk.Label(master=output_frame,text='output',font='Calibri 24',textvariable=output_string)
output_indicator=ttk.Label(master=output_frame,text='Km',font='Calabri 10',textvariable=km)
output_label.pack(side='left')
output_indicator.pack(side='left')
output_frame.pack(pady=4)

#title 2
title_label=ttk.Label(master=window,text='Kilometers to Miles',font='Calibri 24 bold')
title_label.pack()

#input file 2
input_frame_2=ttk.Frame(master=window)
entry_int_2=tk.IntVar()
entry_2=ttk.Entry(master=input_frame_2,textvariable=entry_int_2)
button_2=ttk.Button(master=input_frame_2,text='Convert',command=convert_2)
entry_2.pack(side='left',padx=10)
button_2.pack(side='left')
input_frame_2.pack(pady=8)

#output 2
output_frame_2=ttk.Frame(master=window)
output_string_2=tk.StringVar()
mile=tk.StringVar()
output_label_2=ttk.Label(master=output_frame_2,text='output',font='Calibri 24',textvariable=output_string_2)
output_indicator_2=ttk.Label(master=output_frame_2,text='Mile',font='Calabri 10',textvariable=mile)
output_label_2.pack(side='left')
output_indicator_2.pack(side='left')
output_frame_2.pack(pady=4)

#run
window.mainloop()