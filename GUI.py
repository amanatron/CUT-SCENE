from tkinter import *
from tkinter.ttk import Combobox
from logic import form_list, STATE 

#ComboBox (MAIN) -- Create a combobox that updates it's contents based on state. 
    
class ComboB():
    box = Combobox()
    def __init__(self,par):
        self.box = Combobox(par,values=form_list("LEVEL"), postcommand = self.update_list(),state="readonly")
        self.box.pack(padx=(300,0),side=LEFT)
        self.box.bind("<<ComboboxSelected>>", self.comboCallback)
    def update_list(self):
        print("Updqte",self.box.get())
        self.box['values'] = form_list(self.box.get())
    def comboCallback(self,event):
        print("Combo",self.box.get()) 
        self.box['values'] = form_list(self.box.get())
        create_toplevel(self.box.get())


  
root = Tk()  
root.title("CUT-SCENE")
root.geometry("1080x720")

def boldCallback():
    print("Bold")
    
def italicCallback():
    print("Italic")

def underlineCallback():
    print("Underline")
    
def leftCallback():
    print("Left")
    
def rightCallback():
    print("Right")
    
# Ribbon Frame 

ribbon = Frame(root,bg="yellow",relief=GROOVE,borderwidth = 6,width = 1080,height=50)

#mainbox = ComboB(ribbon)
featureCombo = ComboB(ribbon)
leftBut = Button(ribbon, text = "<", command = leftCallback)
leftBut.pack(padx=(200,0),side=LEFT)
rightBut = Button(ribbon, text = ">", command = rightCallback)
rightBut.pack(side=LEFT)


boldBut = Button(ribbon, text = "B", command = boldCallback)
boldBut.pack(padx=(100,0),side=LEFT)
italicBut = Button(ribbon, text = "I", command = italicCallback)
italicBut.pack(side=LEFT)
underlineBut = Button(ribbon, text = "U", underline = 0, command = underlineCallback)
underlineBut.pack(side=LEFT)

ribbon.pack(fill="x",anchor ="nw")

# Toolbar 
toolbar = Frame(root,bg="grey",relief=GROOVE,borderwidth = 6,width = 250, height = 335)
toolbar.pack(anchor = "sw",side="bottom")

#scenemanager 

scenemanager = Frame(root,relief = GROOVE, borderwidth = 6, width = 250, height = 335)
scenemanager.pack(anchor = "nw",side="top")


#create TopLevel which is prompted on main selection

def create_toplevel(STATE):
    top_level = Toplevel(height=300,width=600)
    top_level.title("create {}".format(STATE).title())
    create_button = Button(top_level,text="Create")
    create_button.pack()
    cancel_button = Button(top_level,text="Cancel")
    cancel_button.pack()
    if STATE == "LEVEL":
        level_entry = Entry(top_level)
        level_entry.insert(0,"Enter Name")
        level_entry.pack()
        level_description = Entry(top_level)
        level_description.insert(0,"Enter Description")
        level_description.pack()
        
        
    


root.mainloop()  

