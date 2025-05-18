import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Playing with Scales")

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

slider = tk.StringVar()
slider.set('0')

slider1 = tk.StringVar()
slider1.set('0')


# first scale
ttk.Scale(mainframe, from_=1, to_=100, length=300,command=lambda s:slider.set('%d' % float(s))).grid(column=1, row=1, columnspan=5)

ttk.Label(root, text="Number of Hidden Layers").grid(column=1, row=0)




# second scale
ttk.Scale(mainframe, from_=1, to_=3, length=300,command=lambda s:slider1.set('%d' % float(s))).grid(column=1, row=2, columnspan=5)


# Text
ttk.Label(mainframe, textvariable=slider).grid(column=1, row=3, columnspan=5)

# Text
ttk.Label(mainframe, textvariable=slider1).grid(column=2, row=3, columnspan=5)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
