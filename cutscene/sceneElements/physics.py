from cutscene.utils import Description, Instantiable
from typing import Optional

class Physics(Description, Instantiable):
    """This is simply a small description on the specifcs of a given scene's or object's gravity, pace and etc."""
    def __init__(self, 
                 description: str,
                 itemID: Optional[int] = None):
        Description.__init__(self, description)
        Instantiable.__init__(self, itemID)