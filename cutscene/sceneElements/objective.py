from cutscene.sceneElements.event import Event
from cutscene.sceneElements.animation import Animation
from cutscene.utils import NameDescription

class Objective(NameDescription):
    """Objective class"""
    def __init__(self, 
                 name: str,
                 description: str):
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)

    def addAnimation(self):
        animation = Animation(*args)
        self.addNew(animation)

    def addEvent(self):
        event = Event(*args)
        self.addNew(event)

    def addObjective(self):
        objective = Objective(*args)
        self.addNew(objective)