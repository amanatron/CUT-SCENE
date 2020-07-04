STATE = "NONE" #use for defining state 

def form_list(STATE):
    set_list = []
    if STATE == "LEVEL":
        set_list = ["LEVEL","SUB-LEVEL","SCENE"]
    elif STATE == "SUB-LEVEL":
        set_list = ["LEVEL","SUB-LEVEL","SCENE"]
    elif STATE == "SCENE":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    elif STATE == "OBJECT":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    elif STATE == "OBJECTIVE":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    elif STATE == "EVENT":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    elif STATE == "ANIMATION":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    elif STATE == "NONE":
        set_list = ["LEVEL","SUB-LEVEL","SCENE","OBJECT","OBJECTIVE","EVENT","ANIMATION"]
    return set_list
    
class LEVEL():
    def __init__(self,name,description):
        self.name = name 
        self.description = description
        

        

level_list = []


        




        

