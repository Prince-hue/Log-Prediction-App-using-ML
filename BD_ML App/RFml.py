import tkinter as tk
import upload1 as u
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox
from tkinter import ttk
import errorplot as err
from testwindow import *
#---------------------------
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
#---------------------------

def RFlog():
       if (u.file_dir):
              RFxlist.delete()
              RFylist.delete()
              keys = u.df.keys()
              j = 0
              for i in keys:
                     RFxlist.insert(j, i)
                     RFylist.insert(j, i)
                     j+=1
       else:
              messagebox.showerror(title='File Upload Error', message='No file was uploaded')
def trainlog():
       global RFxlist, RFxaxis
       #an empty array that stores the mulitple selection from the user
       x = []
       for i in RFxlist.curselection():
              x.insert(i, RFxlist.get(i))
       RFxaxis = u.df[x]
       RFxlist.config(bg='#a8ecc2')
       #print(RFxaxis)
       messagebox.showinfo(title='Input Data Specification', message='Input Data submitted')

def predictlog():
       global RFylist, RFyaxis, RFy
       #the variable RFyaxis is the output and the RFlist allows the user to choose from a list which log to predict
       RFy = RFylist.get(RFylist.curselection())
       RFyaxis = u.df[RFy]
       #changes the backgorund colour
       RFylist.config(bg='#a8ecc2')
       #print(RFyaxis)
       messagebox.showinfo(title='Output Data Specification', message='Output Data submitted')
       
def scaleValue():
       global split
       #obtains the value of choice from the user
       split= scale.get()
       tr_split = 100 - split
       #displays the value
       messagebox.showinfo(title='Data Split', message= f'{tr_split} percent of data will be used for training and {split} percent for validation data test')

def continuebtn():
       #spliting configuration
       global x_tr, x_val, y_tr, y_val
       x_tr, x_val, y_tr, y_val = train_test_split(RFxaxis, RFyaxis, test_size=split*0.01)
       messagebox.showinfo(title='Data Split', message= 'Training and Validation split completed')
       #print('done')
       
def model():
       #print(1)
       global reg
       reg = RandomForestRegressor()
       #print(2)
       reg.fit(x_tr, y_tr)
       #print(3)
       messagebox.showinfo(title='Random Forest Model', message= 'Model built')
       messagebox.showinfo(title='Random Forest Model', message= 'Training is completed')
       
def predicty():
       global y_prdt
       y_prdt = reg.predict(x_val)

def mean_abs_err():
       ans = metrics.mean_absolute_error(y_val, y_prdt)
       txt2.delete('1.0', tk.END)
       txt2.insert(tk.END, ans)
       
def mean_sq_err():
       #root mean sq. error
       mse = metrics.mean_squared_error(y_val, y_prdt)
       rmse = mse**0.5
       #print ('The R value is', rmse)
       ans = metrics.mean_absolute_error(y_val, y_prdt)
       txt1.delete('1.0', tk.END)
       txt1.insert(tk.END, rmse)
       
def err_graph():
       err.plot()

def uploadtestfile():
       u.testpath(testpath)

def displaytest():
       testtxt.delete('1.0', tk.END)
       testtxt.insert(tk.END, u.df_test.head(20))
       testtxt.config(state='disabled')

def testfile():
       newtestwindow()
       
    
#creating a window
def RF_window():
       root=tk.Tk()
       roots = ttk.Notebook(root)
       root.title('Random Forest')
       root.geometry('800x500')
       root.resizable(False, False)

       #menu bar
       nav = tk.Menu(root) #we add a menu bar to our root window
       root.config(menu=nav)
       #creating separate menu and adding it to the menu bar
       menu1 = tk.Menu(nav, tearoff=0)
       nav.add_cascade(label='Help', menu=menu1)
       menu1.add_command(label='RF Concept')
       menu1.add_separator()
       menu1.add_command(label='Help')

       #tab Frames
       tab1 = tk.Frame(roots)
       tab2 = tk.Frame(roots)
       tab3 = tk.Frame(roots)
       tab4 = tk.Frame(roots)
       tab5 = tk.Frame(roots)

       #tabs
       roots.add(tab1, text = 'Principal Component Analysis')
       roots.add(tab2, text = 'Validation (Tuning)')
       roots.add(tab3, text = 'RF Building // Model Training')
       roots.add(tab4, text = 'Prediction')
       roots.add(tab5, text = 'Upload Test File')
       roots.pack(expand=True, fill = 'both')

       #title
       tk.Label(root, text='Random Forest, RF', font=('calibra', 20)).pack()

       #tab1 -------------------------------
       tk.Label(tab1, text='Feature Seletion', font=('Arial', 20)).pack()
       tk.Button(tab1, text='Get logs present', command=RFlog).place(x=100, y= 80)
       #label
       tk.Label(tab1, text ='Logs present').place(x= 100, y=130)
       #text
       #tk.Text(tab1, height=2, width=35, bg='#fbf8bd').place(x= 210, y=145)
       #label x and y
       tk.Label(tab1, text ='Select logs to train').place(x= 100, y=180)
       tk.Label(tab1, text ='Select target log to predict').place(x= 500, y=180)
       #entry box
       global RFxlist, RFylist
       #input list
       RFxlist = tk.Listbox(tab1, selectmode='multiple')
       RFxlist.place(x=100, y =200)
       RFxlist.config(height=RFxlist.size())
       #target selection
       RFylist = tk.Listbox(tab1)
       RFylist.place(x=500, y=200)
       RFylist.config(height=RFylist.size())
       #submit button
       RFsubmitx = tk.Button(tab1, text='Train logs', command=trainlog)
       RFsubmitx.place(x=300, y= 330)
       RFsubmity = tk.Button(tab1, text='Predict log', command=predictlog)
       RFsubmity.place(x=700, y= 330)
       #---------------------------------------------
    
       #tab2-------------------------------------
       tk.Label(tab2, text='Select percentage to used for validation', font=('calibra', 20)).pack()
       global scale
       #a scale wisget to obtain the split value
       scale = tk.Scale(tab2, 
                 from_=0, 
                 to=100,
                 length=350,
                 orient='vertical', #oreintation can horizontal. it is vertical by default
                 tickinterval=1, #numeric indicators on the scale
                 #showvalue=0 --hides current value
                 #troughcolor='#69FAFF',
                 #fg='#ff1c00',
                 #bg='#111111'
                 )
       #default split value
       scale.set(20)
       scale.place(x=100, y=50)
       #button that obatains the split
       scale_btn = tk.Button(tab2, text='Split', command= scaleValue)
       scale_btn.place(x=250, y=50)
       #button that assigns the split to the model to be created
       continue_btn = tk.Button(tab2, text='Continue', command= continuebtn)
       continue_btn.place(x=250, y=100)
       #---------------------------------------------
       
       #tab3---------------------------------------
       tk.Label(tab3, text='Building the Model', font=('calibra', 20)).pack()
       tk.Button(tab3, text='Build Model', command= model, width=20, height=10).place(x=300, y=150)
       #--------------------------------
       
       #tab4 ----------prediction--------------
       tk.Label(tab4, text='Error Analysis', font=('calibra', 20)).pack()
       tk.Button(tab4, text='Predict Output', command=predicty).place(x=100, y=50)
       #mean abs error
       tk.Label(tab4, text='Mean Absolute Error').place(x=230, y=100)
       tk.Button(tab4, text='Get value', command=mean_abs_err).place(x=230, y=120)
       global txt1, txt2
       txt2 = tk.Text(tab4, height=2, width=20, bg='#fbf8bd')
       txt2.place(x=230, y= 150)
       #mean sq error
       tk.Label(tab4, text='Mean Square Error').place(x=500, y=100)
       tk.Button(tab4, text='Get value', command=mean_sq_err).place(x=500, y=120)
       txt1 = tk.Text(tab4, height=2, width=20, bg='#fbf8bd')
       txt1.place(x=500, y=150)
       #graphic view of error
       tk.Label(tab4, text='A graphical representation of the Error margin').place(x=200, y=310)
       tk.Button(tab4, text='Generate Graph', command=err_graph).place(x=600, y=310)
       #-------------------------------------------------
       
       #tab5 ----------------------------------------------------
       global testpath, testtxt
       #upload button
       tk.Button(tab5, text='Upload Test file', command=uploadtestfile).place(x=20, y=20)
       #path of test file----
       testpath = tk.StringVar()
       testlabel = tk.Label(tab5, textvariable=testpath, fg='red')
       testlabel.place(x=200, y=20)
       testpath.set('File path appears here when uploaded')
       #display button -----
       tk.Button(tab5, text='Display', command=displaytest).place(x=20, y=60)
       #textbox
       testtxt=tk.Text(tab5, height= 30, width=73, bg='#fbf8bd')
       testtxt.place(x=100, y= 60)
       #continue button
       tk.Button(tab5, text='Continue', command=testfile).place(x=720, y= 340)
       #--------------------------------------------------
       
       
       
       



       