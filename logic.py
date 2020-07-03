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
        set_list = ["LEVEL"]
    elif STATE == "OBJECTIVE":
        set_list = ["LEVEL"]
    elif STATE == "EVENT":
        set_list = ["LEVEL"]
    elif STATE == "ANIMATION":
        set_list = ["LEVEL"]
    elif STATE == "NONE":
        set_list = ["LEVEL"]
    return set_list
    
        




        

