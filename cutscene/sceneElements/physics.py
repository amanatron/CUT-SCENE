from cutscene.utils import Description, ID

class Physics(Description, ID):
    """This is simply a small description on the specifcs of a given scene's or object's gravity, pace and etc."""
    def __init__(self, description: str):
        Description.__init__(self, description)
        ID.__init__(self)