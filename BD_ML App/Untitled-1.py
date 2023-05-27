import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root= tk.Tk()
f = tk.Listbox(root)
f.pack()
def tt():
    #wee = filedialog.askopenfilename()
    #we  = pd.read_csv('trainfile.csv')
    #if wee: #changes file path name from the default to it's directory
    u =100
    messagebox.showinfo(title='File Upload success', message=f'{u} is gold')
    print(f'print {u}')
    
    #print(we)
    #wee = we.keys()
    #print(1, wee[1])
    #w=0
    #for i in wee:
    #    w
    #    f.insert(w, i)
    #    w+=1
def ttt():
    x = f.get(f.curselection())
    print(x)     
    
def new():
    #path of test file
    testpath = tk.StringVar()
    testlabel = tk.Label(root, textvariable=testpath, fg='red')
    testlabel.pack()
    testpath.set('File path appears here when uploaded')



tk.Button(root, command=new).pack()   
tk.Button(root, text='r', command=ttt).pack()      
root.mainloop()