from cutscene.utils import NameDescription, ID

class Event(NameDescription, ID):
    """docstring for Event"""
    def __init__(self, 
                 name: str,
                 description: str):
        NameDescription.__init__(self, name, description)
        ID.__init__(self)