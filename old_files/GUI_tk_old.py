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
        MAIN_TOPLEVEL = TOPLEVEL_MAIN(self.box.get())



  
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
        
class TOPLEVEL_MAIN():
    window = Toplevel()
    def __init__ (self,STATE):
        self.STATE = STATE
        self.window = Toplevel(height=300,width=600)
        self.window.resizable(False,False)
        self.window.title("create new {}".format(STATE).title())
        #self.window.grab.set()
        cancel_button = Button(self.window,text="Cancel")
        cancel_button.pack(side=BOTTOM)
        create_button = Button(self.window,text="Create")
        create_button.pack(side=BOTTOM)
        self.create_window(STATE)
    
    def create_window(self,STATE):
        if STATE == "LEVEL":
            level_entry = Entry(self.window)
            level_entry.insert(0,"Enter Name")
            level_entry.pack()
            level_description = Text(self.window,width=50,height=10,highlightbackground="black")
            level_description.pack()
            level_map = Checkbutton(self.window,text="Add A Map")
            level_map.pack()
            
            
        
        
         
    


root.mainloop()  

