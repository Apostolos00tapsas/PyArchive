import tkinter as tk

def quit(event):
    print ("you pressed control-forwardslash")
    root.destroy()

root = tk.Tk()
root.bind('<Shift-q>', quit)    # forward-slash
root.bind('<Control-f>', quit)  # backslash
root.mainloop()
