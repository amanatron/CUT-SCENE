from cutscene.utils import Description

class Physics(Description):
    """This is simply a small description on the specifcs of a given scene's or object's gravity, pace and etc."""
    def __init__(self, description: str):
        super().__init__(description)