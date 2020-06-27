from tkinter import *
from tkinter.ttk import Combobox
from time import strftime
from PIL import ImageTk,Image
from logic import form_list, STATE 



  
root = Tk()  
root.title("CUT-SCENE")
root.geometry("1080x720")


# Ribbon Frame 

ribbon = Frame(root,bg="yellow",relief=GROOVE,borderwidth = 6,width = 1080,height=50)
ribbon.pack(fill="x",anchor ="nw")

#ComboBox (MAIN)

class ComboB:
    def update_list(self):
        global STATE
        STATE = self.box.get()
        value_list = form_list(STATE)
        self.box['values'] = value_list
    
    box = Combobox(ribbon,values = form_list(STATE), postcommand = update_list())
    box.pack()  

        
mainbox = ComboB()

        
    


     



root.mainloop()  