import tkinter as tk
import upload1 as u
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import ttk

def getlog():
    if (u.file_dir):
        keys = u.df.keys()
        j = 0
        for i in keys:
            xlist.insert(j, i)
            ylist.insert(j, i)
            j+=1
    else:
        messagebox.showerror(title='File Upload Error', message='No file was uploaded')
    

def xsubmit():
    global xaxis
    xaxis = xlist.get(xlist.curselection())
    xlist.config(bg='#a8ecc2')
    

def ysubmit():
    global yaxis
    yaxis = ylist.get(ylist.curselection())
    ylist.config(bg='#8de78f')
    


def window():
    #global root
    root=tk.Tk()
    roots = ttk.Notebook(root)
    root.title('Plots')
    root.geometry('600x700')
    root.resizable(False, False)
    
    #tab Frames
    tab1 = tk.Frame(roots)
    tab2 = tk.Frame(roots)

    #tabs
    roots.add(tab1, text = 'Log Type')
    roots.add(tab2, text = 'Plot Log')
    roots.pack(expand=True, fill = 'both')
    #create matplot fig
    fig, ax = plt.subplots()

    #tab1 --------------------------------------------------
    tk.Label(tab1, text='Chose which log to plot', font=('calibra', 20)).pack()
    #button that prints out logs present
    tk.Button(tab1, text='Get logs present', command=getlog).place(x=100, y= 100)
    #label
    tk.Label(tab1, text ='Logs present').place(x= 100, y=150)
    #text
    #tk.Text(tab1, height=2, width=35, bg='#fbf8bd').place(x= 210, y=145)
    #label x and y
    tk.Label(tab1, text ='Plot on x-axis').place(x= 100, y=150)
    tk.Label(tab1, text ='Plot on y-axis').place(x= 100, y=450)
    #entry box
    global xlist, ylist
    xlist = tk.Listbox(tab1)
    xlist.place(x=200, y =150)
    xlist.config(height=xlist.size())
    ylist = tk.Listbox(tab1)
    ylist.place(x=200, y=450)
    ylist.config(height=ylist.size())
    #submit button
    submitx = tk.Button(tab1, text='Submit x-ordinates', command=xsubmit)
    submitx.place(x=400, y= 150)
    submity = tk.Button(tab1, text='Submit y-ordinates', command=ysubmit)
    submity.place(x=400, y= 450)

    
    #-------------------------------------------------------

    #tab2---------------------------------------------------------------------
    #frame -----------------
    #frame = tk.Frame(root)
    label = tk.Label(tab2, text='Generate Synthetic Graph', font=('calibra', 18))
    label.pack()
    #create canvas
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    #packing the canvas
    canvas.get_tk_widget().pack()

    #adding navigation bar
    toolbar = NavigationToolbar2Tk(canvas, tab2, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor = 'w', fill=tk.X)

    #frame.pack()
    #-----------------------

    viewplot = tk.Button(tab2, text='View Plot', command=lambda: plot_g())
    viewplot.pack()
    #-----------------------------------------------------------
    
    def plot_g():
        if (xaxis and yaxis): #changes file path name from the default to it's directory
            ax.clear()
            training_file = pd.read_csv(u.file_dir)
            x = training_file[xaxis] #np.random.randint(0, 10, 10) #btn  0 to 10 , 10 random numbers
            y = training_file[yaxis] #np.random.randint(0, 10, 10) #btn  0 to 10 , 10 random numbers
            ax.invert_yaxis()
            #ax.set_title(yaxis, 'against', xaxis)
            ax.plot(x,y)
            ax.grid()
            canvas.draw()
        elif (FileNotFoundError):
            messagebox.showerror(title='Co-ordinate Submit Error', message='Must submit two co-ordinates')
        
        
        #messagebox.showwarning(title='File Upload Error', message=oink)
        # message='No file was uploaded')
            
    







    root.mainloop()

    
          


    
           
        


      