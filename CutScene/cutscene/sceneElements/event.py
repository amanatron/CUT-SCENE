from cutscene.utils import NameDescription, Instantiable
from typing import Optional

class Event(NameDescription, Instantiable):
    """docstring for Event"""
    def __init__(self, 
                 name: str,
                 description: str,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID, parentID)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return None