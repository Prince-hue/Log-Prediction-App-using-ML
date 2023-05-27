from r import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd



#d = e.t()
#ans = d +1
#un, im = e(0,0,0).oo()

class array():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.z =2
        self.arr1 = [x,y,self.z]

    def ind(self):
        print(f'I have {self.z} oranges')
        print(f'I have {self.arr1[0]} oranges')
    
#array(4,5).ind()
class green():
    def __init__(self):
        pass
    def run(self):
        self.file = filedialog.askopenfilename(filetypes=[('CSV File','.csv')])
        self.df = pd.read_csv(self.file
            #"C:\\Users\\pc\\Desktop\\BD_ML App\\trainfile.csv"
            )
        #self.tin = 'WTF, hahaha'
        return self.df
        
    #def runn(self):    
        #return self.tin
        #return(self.df)

class fuck():
    def __init__(self):
        pass
    def din(self):
        self.di = 'WTF'
        return self.di

#fd = fuck().din()
#print(fd)
#green().run()
#daf = green().run()
#print(daf)

print(num1)