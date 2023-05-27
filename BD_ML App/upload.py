from tkinter import filedialog
import pandas as pd
import tkinter as tk
from tkinter import messagebox

#from plot import *
#name of class
class upload():

    #function that uploads and prints file pathname
    def load(file_path): #takes one argument, the file_path initially defined
        global file_upload
        file_upload = filedialog.askopenfilename(filetypes=[('CSV File','.csv')]) #uploads file
        if (file_upload): #changes file path name from the default to it's directory
            
            file_path.set(file_upload)
        

    def displayfile(textbox):
        #textbox.delete('1.0', tk.END)
        #creating a dataFrame
        training_file = pd.read_csv(file_upload)
        #displaying data from dataFrame into the textbox
        textbox.insert(tk.END, training_file.head(20))
        textbox.config(state='disabled')
        
        

        
        
        

    

