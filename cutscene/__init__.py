from cutscene.utils import OrderedInstanceHolder, NameDescription
from cutscene.level import Level, SubLevel
from cutscene.scene import Scene
from cutscene.entities import Characters, Objects
import os
import json

class CutSceneProject(OrderedInstanceHolder, NameDescription):
    """ Highest level class for the entire cutscene project. 
    init: 
        name: str,
        description: str,
        genre: str,
        author: str

    methods:
        addLevel: Add a new level to the project 
            name: str,
            description: str
        addScene: Add a new scene to the project 
            name: str,
            description: str
        get: Get a list of all the highest level elements of the project (scenes, levels)
        remove: Delete an element
            index: int; index of element in project elements list
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
                 description: str,
                 genre: str,
                 author: str):

        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)

        assert type(genre) is str
        assert type(author) is str

        self.genre = genre
        self.author = author

        self.characters = Characters()
        self.objects = Objects()

    def new(self, item, **kwargs):
        if item == "LEVEL":
            return self.addLevel(**kwargs)
        elif item == "SCENE":
            return self.addScene(**kwargs)

    def addLevel(self, **kwargs):
        """ Add a new level to the project """
        level = Level(**kwargs)
        self.addNew(level)
        return level

    def addScene(self, **kwargs):
        """ Add a new scene to the project """
        scene = Scene(**kwargs)
        self.addNew(scene)
        return scene

def loadProject(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as projectFile:
            try:
                project_dict = json.load(projectFile)
                return dict_to_project(project_dict)
            except:
                raise

def saveProject(project, filePath):
    with open(filePath, "w") as projectFile:
        json.dump(obj_to_dict(project), projectFile, default=obj_to_dict)

def dict_to_project(proj_dict):

    def restoreOrderedHolder(parent, orderedHolder):
        for item in orderedHolder:
            # Get the classname of the item
            item_type = item.pop("__type__")
            # See if the item has any contents eg an animation class with dialogue, act etc
            if "ordered_holder" in item.keys():
                itemOrderedHolder = item.pop("ordered_holder")
            else:
                itemOrderedHolder = None
            # Call its parent to init a new instance
            child = parent.new(item_type.upper(), **item)
            # Recurse another level in if there's more contents to this item
            if itemOrderedHolder:
                restoreOrderedHolder(child, itemOrderedHolder)
    
    # Create a new project instance
    project = CutSceneProject(name=proj_dict["name"],
                              description=proj_dict["description"],
                              genre=proj_dict["genre"],
                              author=proj_dict["author"])

    # Restore Characters
    if "characters" in proj_dict.keys():
        for character in proj_dict["characters"]["entities"]:
            project.characters.addCharacter(name=character["name"],
                                            description=character["description"],
                                            entityType=character["entityType"])
    # Restore Objects
    if "objects" in proj_dict.keys():
        for obj in proj_dict["objects"]["entities"]:
            project.objects.addObject(name=obj["name"],
                                      description=obj["description"],
                                      entityType=obj["entityType"])

    # Recursively Restore Project Levels
    if "ordered_holder" in proj_dict.keys():
        restoreOrderedHolder(project, proj_dict["ordered_holder"])

    return project

def obj_to_dict(obj):
    obj_dict = {}
    obj_dict["__type__"] = obj.__class__.__name__.upper()
    for key, value in obj.__dict__.items():
        # eg turns "_Description__description" to "description"
        if "__" in key:
            obj_dict[key.split("__",1)[1]] = value
        else:
            obj_dict[key] = value
    return obj_dict