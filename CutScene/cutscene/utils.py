import uuid
import base64
from typing import Optional

paramHelp = {
"CUTSCENEPROJECT":  ("Create a New Project", "Edit Project",
                        [("name",            "Name",              "shortStr"),
                         ("author",          "Author",            "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("genre",           "Genre",             "shortStr")]),
"LEVEL":            ("Add Level", "Edit Level",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("img",             "Map",               "mapImg")]),
"SUBLEVEL":         ("Add Sublevel", "Add Sublevel",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("img",             "Map",               "mapImg")]),
"SCENE":            ("Add Scene", "Edit Scene",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("img",             "Map",               "mapImg")]),
"CHARACTER":        ("Create Character", "Edit Character",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("entityType",      "Character Type",    ["PLAYER", "ENEMY", "OTHER"]),
                         ("img",             "Character Image",   "charImg")]),
"OBJECT":           ("Create Object", "Edit Object",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str"),
                         ("entityType",      "Object Type",       ["RESPONSIVE", "NON-RESPONSIVE"]),
                         ("img",             "Object Image",      "charImg")]),
"ACTION":           ("Add Action", "Edit Action",
                        [("description",     "Description",       "Str")]),
"ANIMATION":        ("Create Animation", "Edit Animation",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str")]),
"TRANSITION":       ("Add Transistion", "Edit Transistion",
                        [("description",     "Description",       "Str")]),
"ACT":              ("Add Act", "Edit Act",
                        [("description",     "Description",       "Str")]),
"HEADING":          ("Add Heading", "Edit Heading",
                        [("description",     "Description",       "Str")]),
"DIALOGUE":         ("Add Dialogue", "Edit Dialogue",
                        [("character_name",  "Character",         "shortStr"),
                         ("dialogue",        "Dialogue",          "Str"),
                         ("paranthetical",   "Paranthetical",     "Str")]),
"EVENT":            ("Create Event", "Edit Event",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str")]),
"OBJECTIVE":        ("Add Objective", "Edit Objective",
                        [("name",            "Name",              "shortStr"),
                         ("description",     "Description",       "Str")]),
"PHYSICS":          ("Add Physics", "Edit Physics",
                        [("description",     "Description",       "Str")]),
"PSEUDOCODE":       ("Add Pseudocode", "Edit Pseudocode",
                        [("name",            "Name",              "shortStr"),
                         ("purpose",         "Purpose",           "Str"),
                         ("pscode",          "Pseudocode",        "Str")]),
"CONTROL":          ("Add Control", "Edit Control", []),
"SIGNAL":           ("Add Physics", "Edit Physics", []),
}

# Global registry, all instantiable items with an ID give their id and a reference to themselves into this dict
global REGISTRY
REGISTRY = {}

class OrderedInstanceHolder(object):
    """ Helper class for classes that need to store instances in a specific order.
    classes that use this (not limited to): LevelWrapper, Animation, Scene

    init:
        None

    methods:
        get: get a list of the instances
        addNew: add a new instance to the end of the list
            item: instance to add to the list
        remove: remove instance from list at a given index
            index: int
        moveUp: move instance at index one place up the list
            index: int
        moveDown: move instance at index one place down the list
            index: int
        move: move instance from one index to another
            index: int, which item you want
            newIndex: int, where you want the item to go
    """

    def __init__(self):
        self.__ordered_holder = []

    def get(self) -> list:
        return self.__ordered_holder

    def addNew(self, item):
        self.__ordered_holder.append(item)

    def remove(self,
               index: int):
        assert type(index) is int
        del self.__ordered_holder[index]

    def removeByID(self,
                   itemID: int):
        assert type(itemID) is int
        for index, item in enumerate(self.__ordered_holder):
            if item.id == itemID:               
                self.remove(index)
                break

    def __elementSwap(self,
                      index1: int,
                      index2: int):
        """Elementwise swap of two items at specified indexes"""
        self.__ordered_holder[index1], self.__ordered_holder[index2] = self.__ordered_holder[index2], self.__ordered_holder[index1]

    def moveUp(self,
               index: int):
        assert type(index) is int
        if index == 0:
            raise ValueError("Can't move first element of list up")
        elif 0 > index > len(self.__ordered_holder):
            raise ValueError("Index out of range: {}".format(Index))
        self.__elementSwap(index, index-1)

    def moveDown(self,
                 index: int):
        assert type(index) is int
        if index == len(self.__ordered_holder):
            raise ValueError("Can't move last element of list down")
        elif 0 > index > len(self.__ordered_holder):
            raise ValueError("Index out of range: {}".format(Index))
        self.__elementSwap(index, index+1)

    def move(self,
             index: int,
             newIndex: int):
        assert type(index) is int
        assert type(newIndex) is int
        if 0 > index > len(self.__ordered_holder):
            raise ValueError("Index out of range: {}".format(Index))
        if 0 > newIndex > len(self.__ordered_holder)-1:
            raise ValueError("newIndex out of range: {}".format(newIndex))
        item = self.__ordered_holder.pop(index)
        self.__ordered_holder.insert(newIndex, item)

class Image(object):
    """ Base class for image support. Stores image data as base64 encoded strings """
    def __init__(self,
                 img: Optional[str] = None):
        self.img = img

    @property
    def img(self) -> str:
        return self.__img

    @img.setter
    def img(self, img: str):
        try:
            if not img:
                self.__img = None
                return
            if type(img) is bytes:
                img = img.decode("utf-8")
            base64.b64decode(img)
            assert type(img) is str
            self.__img = img
        except:
            raise

class CharacterImage(Image):
    def __init__(self, img):
        Image.__init__(self, img)

class MapImage(Image):
    def __init__(self, img):
        Image.__init__(self, img)

class Name(object):
    """Helper class providing name functionality to other classes"""
    def __init__(self,
                 name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        assert type(name) is str
        self.__name = name

class Description(object):
    """Helper class providing description functionality to other classes"""
    def __init__(self,
                 description: str):
        self.description = description

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        assert type(description) is str
        self.__description = description

class NameDescription(Description, Name):
    """Helper class providing name and description functionality to other classes"""
    def __init__(self, 
                 name: str,
                 description: str):
        Description.__init__(self, description)
        Name.__init__(self, name)

class Instantiable(object):
    """Base class for all instantiable objects, providing core functionality"""
    def __init__(self, itemID, parentID=None, parent=None):
        if not itemID:
            self.itemID = uuid.uuid4().int
        else:
            assert type(itemID) is int
            self.itemID = itemID
        if parent:
            self.parentID = parent.id
        else:
            self.parentID = parentID

        self.type = objToDict(self)["type"]

        global REGISTRY
        REGISTRY[self.itemID] = self

    @property
    def id(self):
        return self.itemID

    def edit(self, params):
        """ Allows any class to update its attributes from a dict """
        for key, value in params.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError("{} has no attribute {}".format(self, key))

    def dict(self):
        """Return a nice dict of the object, including its type"""
        return objToDict(self)

def objToDict(obj):
    obj_dict = {}
    obj_dict["type"] = obj.__class__.__name__.upper()
    for key, value in obj.__dict__.items():
        # eg turns "_Description__description" to "description"
        if "__" in key:
            obj_dict[key.split("__",1)[1]] = value
        else:
            obj_dict[key] = value
    return obj_dict

def getByID(item_id):
    global REGISTRY
    try:
        return REGISTRY[item_id]
    except KeyError:
        raise


def restoreOrderedHolder(parent, orderedHolder):
    if not orderedHolder:
        return
    for item in orderedHolder:
        # Get the classname of the item
        item_type = item.pop("type")
        # See if the item has any contents eg an animation class with dialogue, act etc
        if "elements" in item.keys():
            itemOrderedHolder = item.pop("elements")
        elif "ordered_holder" in item.keys():
            itemOrderedHolder = item.pop("ordered_holder")
        else:
            itemOrderedHolder = None
        # Call its parent to init a new instance
        child = parent.new(item_type.upper(), **item)
        # Recurse another level in if there's more contents to this item
        if itemOrderedHolder:
            restoreOrderedHolder(child, itemOrderedHolder)
        # restore scenematrix if item is a scene
        if item_type == "SCENE":
            matrix = item.pop("sceneMatrix")
            child.restoreSceneMatrix(matrix)