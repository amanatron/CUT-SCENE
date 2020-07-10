from cutscene.utils import NameDescription

class Event(NameDescription):
    """docstring for Event"""
    def __init__(self, 
                 name: str,
                 description: str):
        NameDescription.__init__(self, name, description)