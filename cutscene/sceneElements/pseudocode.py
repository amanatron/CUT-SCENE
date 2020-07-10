from cutscene.utils import Name

class Pseudocode(Name):
    """This feature allows the user to simply write the required pseudocode for any given action, scene, objective or event they deem fit.
    They will be asked to name the code and it's purpose in one line, after which the code will appear next to that which it is a child of. """
    def __init__(self,
                 name: str,
                 purpose: str, 
                 pscode: str):
        Name.__init__(self, name)
        self.purpose = purpose
        self.pscode = pscode

    @property
    def purpose(self) -> str:
        return self.__purpose

    @property
    def pscode(self) -> str:
        return self.__pscode

    @purpose.setter
    def purpose(self, purpose: str):
        assert type(purpose) is str
        self.__purpose = purpose

    @pscode.setter
    def pscode(self, pscode: str):
        assert type(pscode) is str
        self.__pscode = pscode