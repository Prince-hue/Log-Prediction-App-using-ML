from tkinter import filedialog
import pandas as pd
import tkinter as tk
from tkinter import messagebox
#from plot import *
#name of class

def dataframe():
    file_upload = filedialog.askopenfilename(filetypes=[('CSV File','.csv')]) #uploads file
    training_file = pd.read_csv(file_upload)
    
    return training_file, file_upload


#function that uploads and prints file pathname
def path(file_path):
    global df, file_dir
    df, file_dir = dataframe()
    
    if (file_dir):
            messagebox.showinfo(title='File Upload Success', message='File was successfully uploaded') #changes file path name from the default to it's directory
            file_path.set(file_dir)
    else:
        messagebox.showerror(title='File Upload Error', message='No file was uploaded')
    
def testpath(testpath):
    global df_test, file_dir_test
    df_test, file_dir_test = dataframe()
    
    if (file_dir_test):
        messagebox.showinfo(title='File Upload Success', message='File was successfully uploaded') #changes file path name from the default to it's directory
        testpath.set(file_dir_test)
    else:
        messagebox.showerror(title='File Upload Error', message='No file was uploaded')

        
   

        
        
        

    

