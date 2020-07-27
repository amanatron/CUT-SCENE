import cutscene


# The model class stores program data and state and some minimal logic for announcing changes to this data. 
# This model shouldn't be confused with the Qt model (see http://qt-project.org/doc/qt-4.8/model-view-programming.html) as it's not really the same thing.
# 
# The model might look like:
# 
# Writes to the model automatically emit signals to any listening views via code in the setter decorated functions. 
# Alternatively the controller could manually trigger the signal whenever it decides.
# 
# In the case where Qt model types (e.g. QStringListModel) have been connected with a widget then the view containing 
# that widget does not need to be updated at all; this happens automatically via the Qt framework.


class Model(object):
    def __init__(self):
        super().__init__()
        self.project = None
        self.projectPath = None

    def newProject(self, params):
        self.project = cutscene.CutSceneProject(**params)
        #  name="Demo Project",
        #  description="my first project",
        #  genre="demo genre",
        #  author="Matthew Bowley"

    def getProject(self):
        return self.project

    def getLevels(self):
        return self.project.get()

    def loadProject(self, projectPath):
        self.project = cutscene.loadProject(projectPath)
        self.projectPath = projectPath

    def addLevel(self, **params):
        self.project.new("LEVEL", **params)


    # def initSceneModel(self, scene):

    #     # item here refers to sceneElement
    #     def newItemEntry(element, parent_item):
    #         item_dict = element.dict()
    #         new_item = StandardItem(element, item_dict["__type__"])
    #         parent_item.appendRow(new_item)
    #         if item_dict["__type__"] in ["ANIMATION", "SCENE"]:
    #             for item in element.get():
    #                 newItemEntry(item, new_item)

    #     self.scene_model = QStandardItemModel()
    #     parent_item = self.scene_model.invisibleRootItem()
    #     newItemEntry(scene, parent_item)



        # self._even_odd = ''
        # self._enable_reset = False
