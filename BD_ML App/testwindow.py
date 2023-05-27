import tkinter as tk
import upload1 as u
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox
from tkinter import ttk
import errorplot as err
import RFml as rf
#---------------------------
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
#---------------------------

def testget():
    if (u.file_dir_test):
              keys = u.df_test.keys()
              j = 0
              for i in keys:
                    testlistm.insert(j, i)
                    testlistt.insert(j, i)
                    j+=1
    else:
        messagebox.showerror(title='File Upload Error', message='No file was uploaded')
        
def submittestm():
    global testlistm, testx
    #an empty array that stores the mulitple selection from the user
    testx = []
    for i in testlistm.curselection():
            testx.insert(i, testlistm.get(i))
    #testm = u.df_test[x]
    testlistm.config(bg='#a8ecc2')
    #print(RFxaxis)
    messagebox.showinfo(title='Input Data Specification', message='Input Data submitted')
    
def submittestt():
    global testlistt, testt, RFyT
    #the variable RFyaxis is the output and the RFlist allows the user to choose from a list which log to predict
    RFyT = testlistt.get(testlistt.curselection())
    testt = u.df_test[RFyT]
    #changes the backgorund colour
    testlistt.config(bg='#a8ecc2')
    messagebox.showinfo(title='Output Data Specification', message='Output Data submitted')

def predictt():
    #trying to predict the target by taking in inputs
    x_ts = u.df_test[testx]
    messagebox.showinfo(title='Input Data', message='Input Data received successfully')
    #Target model
    u.df_test['Predicted'+RFyT] = rf.reg.predict(x_ts)
    messagebox.showinfo(title='Prediction', message= 'Prediction completed successfully')
  
  
    
def newtestwindow():
    #window
    root = tk.Tk()
    root.geometry('500x650')
    root.resizable(False, False)
    root.title('Test File')
    
    #label
    tk.Label(root, text = 'Input', font=(20)).place(x=50, y=20)
    #get inputs
    tk.Button(root, text='Get logs', command=testget).place(x=50, y= 60)
    #listbox
    global testlistm, testlistt
    testlistm = tk.Listbox(root, selectmode='multiple')
    testlistm.place(x=50, y= 100)
    #button
    tk.Button(root, text='Submit Inputs', command=submittestm).place(x=50, y= 290)
    #target
    tk.Label(root, text = 'Output', font=(20)).place(x=50, y=400)
    testlistt = tk.Listbox(root, height=5)
    testlistt.place(x=50, y= 460)
    #button
    tk.Button(root, text='Submit Target', command=submittestt).place(x=50, y= 550)
    #RHS
    framet = tk.Frame(root, width=250, height=650, bg='#c1f7d8')
    tk.Button(framet, text='Predict target', bg='#87afa3', command=predictt).pack(padx=10, pady=35)
    tk.Button(framet, text='View Graph Predicted', bg='#87afa3').pack(padx= 10, pady=35)
    tk.Button(framet, text='Error margin analysis Graph', bg='#87afa3').pack(padx= 10, pady=35)
    tk.Button(framet, text='True verse Predicted log Graph', bg='#87afa3').pack(padx= 10, pady=35)
    framet.pack(side='right', fill='y')