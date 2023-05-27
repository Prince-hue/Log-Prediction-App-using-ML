import tkinter as tk
import upload1 as u
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
import RFml as rf

def plot():
    root = tk.Toplevel()
    root.title('Scatter Plot')
    #create matplot fig
    fig, ax = plt.subplots()
    
    label = tk.Label(root, text='Scatter Plot', font=('calibra', 18))
    label.pack()
    text = 'Blue dots above the black line \n represent the values that the model overestimated. \n Those beneath were underestimated'
    tk.Label(root, text= text, fg = 'red').pack()
    #create canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    #packing the canvas
    canvas.get_tk_widget().pack()

    #adding navigation bar
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor = 'w', fill=tk.X)

    #frame.pack()
    #-----------------------

    viewplot = tk.Button(root, text='View Plot', command=lambda: errplot_g())
    viewplot.pack()
    #-----------------------------------------------------------
    
    def errplot_g():
        ax.clear()
        #ax.set_title(yaxis, 'against', xaxis)
        ax.scatter(rf.y_val, rf.y_prdt)
        ax.plot((0, 150), (0, 150), 'black')
        ax.grid()
        canvas.draw()
        
        
        