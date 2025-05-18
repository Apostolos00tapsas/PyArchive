import tkinter as tk


"""
Script Name: Event_Cutcher.PY
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements a class that prints any key pressed from keyboard.

Parameters:
    
    
Returns:
    event_cutcher()

Example:
    PSO(swarm)
"""


class event_cutcher():
    def __init__(self):
        self.root = tk.Tk()
        self.root.bind('<Key>', self.test)
        self.root.mainloop()

    def test(self, event):
        print('keysym:', event.keysym)

    
event_cutcher()