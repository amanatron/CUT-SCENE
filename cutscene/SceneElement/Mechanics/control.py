from typing import Tuple

class Control(Mechanics):
    """This basically describes the controls a user assigns to the player object – upon choosing to 
    add controls, the user will be prompted to either “add a new control or edit an existing one”.
    They can choose any key on their keyboard and describe in one line what that control does"""
    def __init__(self):
        self.__controls = []

    @property
    def controls(self):
        return self.__controls

    def __checkKeyDesc(self, desc: str):
        if not desc:
            raise ValueError("No description provided")

    def __checkKeyCode(self, key: str):
        if len(key) > 1:
            raise ValueError("Key {} is not a single keypress".format(key))
        if not key:
            raise ValueError("No key provided")

    def __checkKeyBind(self, keybind: Tuple[str, str]):
        key, desc = keybind
        self.__checkKeyCode(key)
        self.__checkKeyDesc(desc)

    # # Might be kind to the frontend to have an input validation function that returns True or False, 
    # # or even something more informative without raising errors
    
    # def checkKeyBind(self, keybind: Tuple[str, str]):
    #     try:
    #         return self.__checkKeyBind(keybind)
    #     except:
    #         return False

    def addNew(self, keybind: Tuple[str, str]):
        """Add new keybind"""
        self.__checkKeyBind(keybind)
        self.controls.append(keybind)

    def edit(self, keycode: str, keybind: Tuple[str, str]):
        """Edit existing keybind"""
        self.__checkKeyCode(keycode)
        self.__checkKeyBind(keybind)
        self.__remove__(keycode)
        self.__addnew__(keybind)

    def remove(self, keycode: str):
        """Delete existing keybind"""
        for i, keybind in enumerate(self.controls):
            if keycode == keybind[0]:
                del self.controls[i]
                return
        else:
            raise ValueError("No bind exists for key {}".format(key))