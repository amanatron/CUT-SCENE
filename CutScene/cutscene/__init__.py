from cutscene.utils import OrderedInstanceHolder, NameDescription, Instantiable, paramHelp, objToDict, restoreOrderedHolder
from cutscene.level import Level, SubLevel
from cutscene.scene import Scene
from cutscene.entities import Characters, Objects
from typing import Optional
import os
import json

class CutSceneProject(OrderedInstanceHolder, NameDescription, Instantiable):
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
                 author: str,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):

        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID, parentID)

        assert type(genre) is str
        assert type(author) is str

        self.genre = genre
        self.author = author

        self.characters = Characters()
        self.objects = Objects()

    def new(self, item, **kwargs):
        if item == "LEVEL":
            return self.addLevel(**kwargs)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["LEVEL"])

    def addLevel(self, **kwargs):
        """ Add a new level to the project """
        level = Level(parentID = self.id, **kwargs)
        self.addNew(level)
        return level

    def addScene(self, **kwargs):
        """ Add a new scene to the project """
        scene = Scene(parentID = self.id, **kwargs)
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
        json.dump(objToDict(project), projectFile, default=objToDict)


def dict_to_project(proj_dict):   
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