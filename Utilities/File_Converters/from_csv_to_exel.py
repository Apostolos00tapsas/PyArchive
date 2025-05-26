try:
    from tkinter import *
    from tkinter import messagebox as tkMessageBox
    from tkinter import filedialog as fd
    import pandas as pd
    
except ImportError as e:
    print ("You have to install Tkinter first")
    print (e)

class csv_to_exel:
    def __init__(self):
        self.data = []
        self.root = Tk(className = 'csv to exel convertor')
        self.root.title("csv to exel convertor")
        self.root.geometry("300x80")
        self.C = Button(self.root, text ="Close", command = self.root.destroy)
        self.C.pack(side = BOTTOM)
        self.B = Button(self.root, text ="Impost CSV & Convert", command = self.import_CSV)
        self.B.pack(side = BOTTOM)
        self.root.mainloop()

    def import_CSV(self):
        self.filename = fd.askopenfilename(title = "Select file",filetypes = (("all Files","*.csv"),))
        if not self.filename:
            tkMessageBox.showinfo("Info","The procedure was canceled.")
        else:
            self.data = pd.read_csv(self.filename)
            #print(self.data)
            #print(self.data.shape)
            #df = self.data.iloc[:-4148]
            try:
                self.data.to_excel("output.xlsx", index=False) 
                tkMessageBox.showinfo("Info", "The file is ready and saved to the same directory with this file with name output.xlsx.")
            except ValueError as e :
                tkMessageBox.showerror("Unexpected Error", e)
                
csv_to_exel()
