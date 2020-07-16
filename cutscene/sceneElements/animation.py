from cutscene.sceneElements.action import Action
from cutscene.utils import Description, NameDescription, OrderedInstanceHolder
from typing import Optional

class Animation(NameDescription, OrderedInstanceHolder):
    """Animation Class. Used to make a written screenplay with Characters, Actions, etc
    init: 
        name: str,
        description: str

    methods:
        addAction:
            description: str
        addTransition:
            description: str
        addHeading:
            description: str
        addAct:
            description: str
        addDialogue: 
            character_name: str, must be an existing character
            dialogue: str
            paranthetical: str

        get: Get a list of all the elements of the animation (headers, dialogue, etc)
        remove: Delete an element
            index: int; index of element in animation elements list
        moveUp: move element at index one place up in the list
            index: int
        moveDown: move element at index one place down the list
            index: int
        move: move element from one index to another
            index: int, which element you want
            newIndex: int, where you want the element to go
    """
    def __init__(self, 
                 name: str,
                 description: str):
        NameDescription.__init__(self, name, description)
        OrderedInstanceHolder.__init__(self)


    def new(self, item, **kwargs):
        if item == "ACTION":
            return self.addAction(**kwargs)
        elif item == "TRANSITION":
            return self.addTransition(**kwargs)
        elif item == "HEADING":
            return self.addHeading(**kwargs)
        elif item == "DIALOGUE":
            return self.addDialogue(**kwargs)
        elif item == "ACT":
            return self.addAct(**kwargs)

    def addAction(self, **kwargs):
        action = Action(**kwargs)
        self.addNew(action)
        return action

    def addTransition(self, **kwargs):
        transition = Transition(**kwargs)
        self.addNew(transition)
        return transition

    def addHeading(self, **kwargs):
        heading = Heading(**kwargs)
        self.addNew(heading)
        return heading

    def addDialogue(self, **kwargs):
        dialogue = Dialogue(**kwargs)
        self.addNew(dialogue)
        return dialogue

    def addAct(self, **kwargs):
        act = Act(**kwargs)
        self.addNew(act)
        return act

class Transition(Description):
    """Describe a transition in an animation"""
    def __init__(self,
                 description: str):
        super().__init__(description)

class Act(Description):
    """Describe a transition in an animation"""
    def __init__(self,
                 description: str):
        super().__init__(description)


class Heading(Description):
    """Add a heading in an animation"""
    def __init__(self,
                 description: str):
        super().__init__(description)

class Dialogue(Animation):
    """A single piece of dialogue from a character"""
    def __init__(self,
                 character_name: str, # character = getCharacter(character_name)
                 dialogue: str,
                 paranthetical: Optional[str] = None):
        self.character_name = character_name
        self.dialogue = dialogue
        self.paranthetical = paranthetical

    @property
    def character_name(self) -> str:
        return self.__character_name

    @character_name.setter
    def character_name(self, character_name: str):
        assert type(character_name) is str
        
        self.__character_name = character_name

    @property
    def paranthetical(self) -> str:
        return self.__paranthetical

    @paranthetical.setter
    def paranthetical(self, paranthetical: str):
        assert type(paranthetical) is str
        self.__paranthetical = paranthetical

    @property
    def dialogue(self) -> str:
        return self.__dialogue

    @dialogue.setter
    def dialogue(self, dialogue: str):
        assert type(dialogue) is str
        self.__dialogue = dialogue
