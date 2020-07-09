import Descriptive

class Physics(Descriptive):
    """This is simply a small description on the specifcs of a given scene's or object's gravity, pace and etc."""
    def __init__(self, description: str):
        self.description = description

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        assert type(description) is str
        self.__description = description