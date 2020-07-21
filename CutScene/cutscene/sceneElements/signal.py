from cutscene.utils import Instantiable
from typing import Optional

class Signal(Instantiable):
    """docstring for Signal"""
    def __init__(self,
                 itemID: Optional[int] = None):
        Instantiable.__init__(self, itemID)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return None