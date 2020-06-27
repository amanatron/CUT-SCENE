from tkinter import *
from tkinter.ttk import Combobox
from logic import form_list, STATE 



  
root = Tk()  
root.title("CUT-SCENE")
root.geometry("1080x720")


# Ribbon Frame 

ribbon = Frame(root,bg="yellow",relief=GROOVE,borderwidth = 6,width = 1080,height=50)
ribbon.pack(fill="x",anchor ="nw")

#ComboBox (MAIN) -- Create a combobox that updates it's contents based on state. 
    
class ComboB:
    def __init___(self):
        self.box = Combobox(ribbon,values=form_list("NONE"),postcommand = self.update_list())
        self.box.pack()
    def update_list(self):
        self.box['values'] = form_list(self.box.get())
 
mainbox = ComboB()

# Toolbar 
toolbar = Frame(root,bg="grey",relief=GROOVE,borderwidth = 6,width = 250, height = 335)
toolbar.pack(anchor = "sw",side="bottom")

#scenemanager 

scenemanager = Frame(root,relief = GROOVE, borderwidth = 6, width = 250, height = 335)
scenemanager.pack(anchor = "nw",side="top")
root.mainloop()  