from tkinter import *
from code import *
import sys
import tkinter as tk
import os

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')


class main():
    def __init__(self):

        self.root = Tk()
        self.root.title('Datadoc Terminal')
    
        self.frame1 = tk.Frame(self.root,height=100)
        self.frame1.pack(side=TOP,fill=tk.X)

        self.run=Button(self.root,text='Run Code',command = self.buttonCallback)
        self.run.pack()

        
    
        self.frame2 = tk.Frame(self.root,height=50)
        self.frame2.pack(side=BOTTOM,fill=tk.X)

        self.codeEditor = Text(self.frame1,bg='#232323', fg='green', bd=0,insertbackground='green')
    
        self.codeScroll = Scrollbar(self.frame1,command=self.codeEditor.yview)
        self.codeEditor.configure(yscrollcommand=self.codeScroll.set)
        self.codeEditor.pack(side=LEFT)
        self.codeScroll.pack(side=RIGHT,fill=Y)


        self.outputWindow = Text(self.frame2,bg='#232323', fg='red', bd=0,insertbackground='red')
        self.outputScroll = Scrollbar(self.frame2,command=self.outputWindow.yview)
        self.outputWindow.configure(yscrollcommand=self.outputScroll.set)
        self.outputWindow.pack(side=LEFT)
        self.outputScroll.pack(side=RIGHT,fill=Y)

    
        self.root.bind('<F5>',self.buttonCallback)
        self.root.mainloop()

    def buttonCallback(self,event=None):
        self.outputWindow.configure(state='normal')
        code = self.codeEditor.get('1.0',END+'-1c')
        c=code.split()
        if c[0]=="pip":
            os.system(code)
        else:
            stdout = sys.stdout 
            stderr = sys.stderr

            try:
                y=eval(code)
            except:
                try:
                    if code =="clear":
                        self.outputWindow.delete('1.0',END)
                    else:
                        exec(code)
                except Exception as e:
                    StdoutRedirector(e)
            
    
            if code=="clear":
                pass
            else:
                sys.stdout = StdoutRedirector(self.outputWindow)
                sys.stderr = StdoutRedirector(self.outputWindow)

                interp = InteractiveInterpreter()
                interp.runcode(code)

                sys.stdout = stdout
                sys.stderr = stderr
        self.outputWindow.configure(state='disabled')


main()
