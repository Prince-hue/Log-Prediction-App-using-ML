import tkinter as tk
import upload1 as u
from RFml import *
from plot import *

#functions
def browsefile():
    u.path(file_path)
   

def display():
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.END, u.df.head(20))
    textbox.config(state='disabled')

def openplot():
    #loadplot = filedialog.askopenfilename(filetypes=[('PNG File','.png')])
    pass

def newplot():
    window()

def RF():
    RF_window()

def MLG():
    pass

def GB():
    pass

def ANN():
    pass

def concept():
    pass


    

#window
root=tk.Tk()
root.title('CSV File Upload')
root.geometry('600x600')
root.resizable(False, False)
rootimg = tk.PhotoImage(file='img\\root.png')
root.iconphoto(True, rootimg)

#menubar
nav = tk.Menu(root) #we add a menu bar to our root window
root.config(menu=nav)
#creating separate menu and adding it to the menu bar
menu1 = tk.Menu(nav, tearoff=0)

nav.add_cascade(label='Plots', menu=menu1)
menu1.add_command(label='New Plot', command=newplot)
menu1.add_separator()
menu1.add_command(label='Open Plot', command=openplot)

#menu 2
menu2 = tk.Menu(nav, tearoff=0)
nav.add_cascade(label='ML Algorithms', menu=menu2)
menu2.add_command(label='Random Forest (RF)', command=RF)
menu2.add_command(label='Multi-linear Gradient (MLG)', command=MLG)
menu2.add_command(label='Gradient Booster (GB)', command=GB)
menu2.add_command(label='Artificial Neural Network (ANN)', command=ANN)
menu2.add_separator()
menu2.add_command(label='ML Concept', command=concept)



#csv image
csvimg = tk.PhotoImage(file='img\\csv.png')
browselabel = tk.Label(root, text='Browse or Upload training file here', font=('calibra', 20))
browselabel.place(x=16, y=70)

#----------------------------------------------------

#csv img
tk.Label(root, image=csvimg).place(x=450, y =50)

#upload btn
browsebtn = tk.Button(root, text='Browse Training File', command=browsefile)
browsebtn.place(x=100, y=170)

#this variable keeps the uploaded file path name
file_path = tk.StringVar()
path_label = tk.Label(root, textvariable=file_path, fg='red')
path_label.place(x=300, y=170)
file_path.set('File path appears here when uploaded')

#textbox that displays the content of the uploaded file
textbox = tk.Text(root, height=20, width=70, bg='#fbf8bd')
textbox.place(x=16, y=250)

#button that displays file
displayfile = tk.Button(root, text='Display File', command=display)
displayfile.place(x=500, y=218)










root.mainloop()