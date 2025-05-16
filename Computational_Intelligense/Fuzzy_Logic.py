import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, r, c)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="left")
        self.close = tk.Button(self, text="Exit", command=root.destroy)
        self.close.pack(side="left")

    def on_submit(self):
        data = self.table.get()
        plt.title("Participation Function")
        plt.ylim(-0.1,1.1)
        #print(type(data[0][0]))
        x = [int(i) for i in data[0]]
        y = [float(i) for i in data[1]]
        plt.plot(x,y)
        plt.show()
        

r= 2
c = 2

root = tk.Tk()
root.title("Please Insert Data and their participation.")
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()
