from cutscene.utils import NameDescription, Instantiable, MapImage
from cutscene.sceneElements.animation import Animation
from cutscene.sceneElements.event import Event
from cutscene.sceneElements.objective import Objective
from typing import Optional

class Scene(NameDescription, Instantiable, MapImage):
    """Scene object. Everything in cutscene happens in a Scene.

    init: 
        name: str
        description: str

    methods:
        addAnimation: Add an Animation to the scene
            name: str
            description: str
        addObjective: Add an Objective to the scene
            name: str
            description: str
        addEvent: Add an Event to the scene
            id1: id of the element the event leads from
            id2: id of the element the event leads from
            name: str
            description: str

        get: get the elements of the scene, and the matrix of events linking the elements
        getEventMap: Returns dict with each entry of itemID giving a list of other itemIDs it links to
                     eg. A: [B, C]
                         B: [D]
                         C: [D]
                         D: []
        getEvents: returns a list of tuples, for each event: (event_id, from_id, to_id) 
        delItem: Delete a scene element and its events
            id: int; id of element in scene elements list
        delEvent: Delete a scene event
            id: int; id of event
    """
    def __init__(self, 
                 name: str,
                 description: str,
                 img: Optional[str] = None,
                 elements: Optional[list] = None,
                 sceneMatrix: Optional[list] = None,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID, parentID)
        MapImage.__init__(self, img)
        self.elements = []
        self.sceneMatrix = []

    def __itemIdxFromId(self, elem_id):
        for idx, element in enumerate(self.elements):
            if element.id == elem_id:
                return idx

    def __eventIdxFromId(self, event_id):
        for fr, row in enumerate(self.sceneMatrix):
            for to, event in enumerate(row):
                if event is not None:
                    if event.itemID == event_id:
                        return (fr, to)

    @property
    def __elementCount(self):
        return len(self.elements)
        # returns number of scene elements

    def restoreSceneMatrix(self, sceneMatrix):
        for fr, row in enumerate(sceneMatrix):
            for to, event_params in enumerate(row):
                if event_params:
                    event_params.pop("type")
                    event = Event(**event_params)
                    self.sceneMatrix[fr][to] = event

    def get(self):
        return (self.elements, self.sceneMatrix)

    def getEventMap(self):
        """ Returns dict with each entry of itemID giving a list of other itemIDs it links to
            eg. A: [B, C]
                B: [D]
                C: [D]
                D: []
        """
        event_dict = {}
        for fr, row in enumerate(self.sceneMatrix):
            item_id = self.elements[fr].itemID
            event_indices = [i for i, fr in enumerate(row) if fr]
            to_item_ids = [self.elements[i].itemID for i in event_indices]
            event_dict[item_id] = to_item_ids
        return event_dict

    def getEvents(self):
        """ returns a list of tuples, for each event (event_id, from, to) """
        events = []
        for fr, row in enumerate(self.sceneMatrix):
            for to, event in enumerate(row):
                if event is not None:
                    fr_id = self.elements[fr].itemID
                    to_id = self.elements[to].itemID
                    events.append((event.itemID, fr_id, to_id))
        return events

    def addNew(self, item):
        # add row at bottom of scene matrix
        self.sceneMatrix.append([None for i in range(self.__elementCount)])
        # add column
        for element in self.sceneMatrix:
            element.append(None)
        # add to item list
        self.elements.append(item)
        # make link?
        pass

    def delItem(self, item_id):
        idx = self.__itemIdxFromId(item_id) # get idx
        for row in self.sceneMatrix:        # remove from event matrix
            del row[idx]
        del self.sceneMatrix[idx]
        del self.elements[idx]              # remove item 

    def addEvent(self, id1, id2, **kwargs):
        fr = self.__itemIdxFromId(id1)
        to = self.__itemIdxFromId(id2)
        event = Event(**kwargs)
        self.sceneMatrix[fr][to] = event
        return event

    def delEvent(self, event_id):
        fr, to = self.__eventIdxFromId(event_id)
        self.sceneMatrix[fr][to] = None

    def moveEvent(self, event_id, new_id1, new_id2):
        fr, to = self.__eventIdxFromId(event_id)
        event = self.sceneMatrix[fr][to]
        self.sceneMatrix[fr][to] = None
        self.sceneMatrix[new_id1][new_id2] = event

    def getEventById(self, event_id):
        fr, to = self.__eventIdxFromId(event_id)
        return self.sceneMatrix[fr][to]

    def getEventFromTo(self, event_id):
        fr, to = self.__eventIdxFromId(event_id)
        fr_id = self.elements[fr].itemID
        to_id = self.elements[to].itemID
        return fr_id, to_id

    def new(self, item, **kwargs):
        if item == "ANIMATION":
            return self.addAnimation(**kwargs)
        elif item == "OBJECTIVE":
            return self.addObjective(**kwargs)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["ANIMATION"], 
                paramHelp["OBJECTIVE"])

    def addAnimation(self, *args, **kwargs):
        animation = Animation(*args, parentID = self.id, **kwargs)
        self.addNew(animation)
        return animation

    def addObjective(self, *args, **kwargs):
        objective = Objective(*args, parentID = self.id, **kwargs)
        self.addNew(objective)
        return objective