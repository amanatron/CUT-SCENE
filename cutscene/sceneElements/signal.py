from cutscene.utils import Instantiable
from typing import Optional

class Signal(Instantiable):
    """docstring for Signal"""
    def __init__(self,
                 itemID: Optional[int] = None):
        Instantiable.__init__(self, itemID)