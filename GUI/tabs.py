#
# DataDoc application 
#
__author__      = "Apostolos Tapsas"
__copyright__   = "Copyright 2019, Apostolos Tapsas"
__license__     = "Heartbit"
__version__     = "0.0.3"
__email__       = "Apostolos Tapsas"
__status__      = "Production"



# Importing Libraries 
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkinter.colorchooser import askcolor
import os





class tabs:
    def __init__(self):

        # Define Dataset
        self.Dataset=[]


        # Create application Gui
        self.app = Tk()
        self.app.title("Tabs")
        self.app.geometry("1020x620")
        self.app.resizable(0,0)
        #self.app.iconbitmap(r"icons\dnd.ico")
        #self.app.iconbitmap(default='icons\dnd.ico')
        self.app.configure(background='white')


        # Put First and Second frames background color
        style = ttk.Style(self.app)
        style.configure('lefttab.TNotebook', tabposition='wn', background='#5c94c5')
        self.s = ttk.Style()
        self.s.configure('My.TFrame', background='white')



        # Fit the selection buttons on application's right site 
        self.note = ttk.Notebook(self.app, style='lefttab.TNotebook')


        # Create the two buttons will fit in the right site
        self.tab1 = ttk.Frame(self.note, style='My.TFrame')
        self.tab5 = ttk.Frame(self.note, style='My.TFrame')
        self.tab2 = ttk.Frame(self.note, style='My.TFrame')
        self.tab3 = ttk.Frame(self.note, style='My.TFrame')
        self.tab4 = ttk.Frame(self.note, style='My.TFrame')
        self.tab6 = ttk.Frame(self.note, style='My.TFrame')
        




        # Pack them
        self.note.add(self.tab1, text = "H")
        self.note.add(self.tab5, text = "V")
        self.note.add(self.tab3, text = "I")
        self.note.add(self.tab2, text = "P")
        self.note.add(self.tab4, text = "T")
        self.note.add(self.tab6, text = "About DataDoc")

        self.note.pack(fill=BOTH, expand=True, side='right')
        self.doc  = ttk.Button(self.note,text='Doc',  command = self.show_app).pack(side=BOTTOM, anchor=W)


        #Create  Menu
        self.menu = Menu(self.app)
        self.app.config(menu=self.menu)
        self.submenu2=Menu(self.menu)


        # Preprocces Menu
        #========================================================================================
        # Create the Menus
        self.preprocces_menu = Menu(self.menu)
        self.miss_val_menu   = Menu(self.menu)
        self.pca_menu        = Menu(self.menu)


        # Put tab in root
        self.menu.add_cascade(label="Preprocces", menu=self.preprocces_menu)


        # First menu of Preprocces tab
        self.preprocces_menu.add_cascade(label="Missing Values Manager",menu=self.miss_val_menu)


        # Sub menus of First menu of Preprocces tab
        self.miss_val_menu.add_command(label="Delete Missing Values", command=self.show_app)
        self.miss_val_menu.add_command(label="Replace Missing Values With Mean", command=self.show_app)
       
        # Second menu of Preprocces tab
        self.preprocces_menu.add_cascade(label="Statistical Procedures", menu=self.show_app)


        # Sub menus of Second menu of Preprocces tab
        self.pca_menu.add_command(label="Principal Component Analysis",  command=self.show_app)
        self.pca_menu.add_command(label="Kernel Principal Component Analysis", command=self.show_app)


        # Analyze

        # Define images for Analyze menu
    
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="Analyze", menu=self.submenu2)
        self.submenu2.add_cascade(label="Descriptive Statistics",menu=self.filemenu)
        self.filemenu.add_command(label="Normality Test" ,command=self.show_app)
        self.filemenu.add_command(label="F Test" ,command=self.show_app)
        self.filemenu.add_command(label="Chisquare Test" ,command=self.show_app)
        self.filemenu = Menu(self.menu)
        

        #Compare Means
        #Define images for Compare Means menu
        

        self.submenu2.add_cascade(label="Compare Means" ,menu=self.filemenu)
        self.filemenu.add_command(label="Independent Sample t-test",command=self.show_app)
        self.filemenu.add_command(label="Paired Sample t-test",command=self.show_app)
        self.filemenu.add_command(label="Anova",command=self.show_app)
        self.filemenu = Menu(self.menu)


        # Regretion
        self.filemenu = Menu(self.menu)


        #Non parametric Tests
        #Define images for Non parametric Tests
   
        self.submenu2.add_cascade(label="Non Parametric Tests", menu=self.filemenu)
        self.filemenu.add_command(label="Wilcoxon signed-rank",command=self.show_app)
        self.filemenu.add_command(label="Kolmogorov Smirnov", command=self.show_app)
        self.filemenu = Menu(self.menu)



        # Regression Menu
        #========================================================================================
        # Create the Menus
        self.regression_menu=Menu(self.menu)
        self.linear_menu=Menu(self.menu)
        self.svm_menu=Menu(self.menu)
        self.dt_menu=Menu(self.menu)


        # Put tab in root
        self.menu.add_cascade(label="Regression", menu=self.regression_menu)
      


        # First menu of Preprocces tab
        self.regression_menu.add_cascade(label="Linear Models",menu=self.linear_menu)
        

        # Sub menus of First menu of Preprocces tab
        self.linear_menu.add_command(label="Simple Linear Regression", command=self.show_app)
        self.linear_menu.add_command(label="Multivariate Regression",  command=self.show_app)
       


        # Second menu of Preprocces tab
        self.regression_menu.add_cascade(label="Support Vector Model",  menu=self.svm_menu)


        # Sub menus of Second menu of Preprocces tab
        self.svm_menu.add_command(label="Support Vector Regression",  command=self.show_app)


        # 3rd menu of Preprocces tab
        self.regression_menu.add_cascade(label="Decision tree models",  menu=self.dt_menu)



        # Sub menus of 3rd menu of Preprocces tab
        self.dt_menu.add_command(label="Decision Tree Regression",  command=self.show_app)
        self.dt_menu.add_command(label="Random Forest Regression",  command=self.show_app)



        # Classification Menu
        #=========================================================================================
        # Create the Menus
        self.classification_menu=Menu(self.menu)
        self.c_linear_menu=Menu(self.menu)
        self.c_svm_menu=Menu(self.menu)
        self.c_dt_menu=Menu(self.menu)
        self.bayes = Menu(self.menu)
        self.knn_menu = Menu(self.menu)


        # Put tab in root
        self.menu.add_cascade(label="Classification", menu=self.classification_menu)


        # First menu of Preprocces tab
        self.classification_menu.add_cascade(label="Linear Models",menu=self.c_linear_menu)
      


        # Sub menus of First menu of Preprocces tab
        self.c_linear_menu.add_command(label="Logistic Regression",  command = self.show_app)


        self.classification_menu.add_cascade(label="Vector Quantization", menu=self.knn_menu)
        # Sub menus of Second menu of Preprocces tab
        self.knn_menu.add_command(label="KNN" ,command=self.show_app)

        
        # Second menu of Preprocces tab
        self.classification_menu.add_cascade(label="Support Vector Model",menu=self.c_svm_menu)


        # Sub menus of Second menu of Preprocces tab
        self.c_svm_menu.add_command(label="Support Vector Classifier" ,command=self.show_app)


        # 3rd menu of Preprocces tab
        self.classification_menu.add_cascade(label="Decision tree models",  menu=self.c_dt_menu)


        # Sub menus of 3rd menu of Preprocces tab
        self.c_dt_menu.add_command(label="Decision Tree Classifier",  command=self.show_app)
        self.c_dt_menu.add_command(label="Random Forest Classifier",  command=self.show_app)

        # Bayes Menu
        self.classification_menu.add_cascade(label="Bayes Model", menu=self.bayes)
        self.bayes.add_command(label="Naive Bayes",  command = self.show_app)


        # Clusstering Menu
        #==========================================================================================
       
        self.clustering_menu=Menu(self.menu)
        self.kmeans_menu=Menu(self.menu)


        # Put tab in root
        self.menu.add_cascade(label="Clustering", menu=self.clustering_menu)


        # First menu of Preprocces tab
        self.clustering_menu.add_cascade(label="Vector Quantization",menu=self.kmeans_menu)



        # Sub menus of 3rd menu of Preprocces tab
        self.kmeans_menu.add_command(label="Hierarchical clustering",  command=self.show_app)
        self.kmeans_menu.add_command(label="K-Means", command=self.show_app)
        



        # Settings Menu
        #==========================================================================================

        
        self.settings_menu=Menu(self.menu)
        self.menu.add_cascade(label="Settings",menu=self.settings_menu)
        self.settings_menu.add_command(label="Change Color", command=self.Change_Color)
        #settings_menu.add_command(label="About Author",command="")


        # First Tab Buttons
        #==========================================================================================

        #Create Button images

        # Create first row's buttons

        S = ttk.Label(self.tab1, text= "Data", background="white",font = "Times").grid(row=0,column=0)
        

        # Gia na mporesei na doulepsei h clasi createToolTip tha prepei na dilosoume ta koumpia me ton
        # Tropo poy vlepoyme parakatw

        self.import_data_button1 = ttk.Button(self.tab1, text='S', command = self.show_app)
        self.import_data_button1.grid(row=1,column=0)
        

        self.import_data_button2 = ttk.Button(self.tab1, text='S',  command = self.show_app)
        self.import_data_button2.grid(row=1,column=1)
      


        self.import_data_button3 = ttk.Button(self.tab1, text='S',  command=self.show_app)
        self.import_data_button3.grid(row=1,column=2)
        
        

        self.import_data_button4 = ttk.Button(self.tab1, text='S',  command=self.show_app)
        self.import_data_button4.grid(row=2,column=1)
        
        
        

        # Second Tab Buttons
        #==========================================================================================

        

        S = ttk.Label(self.tab2, text= "External Modules Installation", background="white",font = "Times", anchor='nw').grid(row=0,column=0)
        
        self.keras_install   = ttk.Button(self.tab2, text='S', command = '')
        self.keras_install.grid(row=1,column=0)
        

        
        self.sklearn_install = ttk.Button(self.tab2, text='S', command = self.show_app)
        self.sklearn_install.grid(row=1,column=1)
       


        



        
        # Vizualize Tab Buttons
        #==========================================================================================

        

        S = ttk.Label(self.tab5, text= "Data Visualization", background="white",font = "Times", anchor='nw').grid(row=0,column=0)
        
        self.hist_btn   = ttk.Button(self.tab5, text='S', command = self.show_app)
        self.hist_btn.grid(row=1,column=0)
       


        
        self.box_btn = ttk.Button(self.tab5, text='S', command = self.show_app)
        self.box_btn.grid(row=1,column=1)
       


        self.pie_btn = ttk.Button(self.tab5, text='S',  command = self.show_app)
        self.pie_btn.grid(row=1,column=2)
        

        
        self.sc_btn  = ttk.Button(self.tab5, text='S',  command=self.show_app)
        self.sc_btn.grid(row=2,column=0)
        


        self.line_btn = ttk.Button(self.tab5, text='S',  command = self.show_app)
        self.line_btn.grid(row=2,column=1)
        


        S = ttk.Label(self.tab3, text= "Image Processing", background="white",font = "Times").grid(row=0,column=0)


    
       
        
        self.hist_btn   = ttk.Button(self.tab4, text='S', command = '')
        self.hist_btn.grid(row=1,column=0)
        

        
        self.app.mainloop()


    # Function Change_Color is responsible to change color depenting depending on user's option.
    def Change_Color(self):
        self.clr = askcolor()
        self.s.configure('My.TFrame', background=self.clr[1])

    def show_app(self):
        messagebox.showinfo("Info","This Module is Under Construction")

   


        


    
tabs()
    
    
        
    
        

             
        
        
        


        










