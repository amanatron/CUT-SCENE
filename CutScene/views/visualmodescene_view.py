from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Slot
from views.visualmodeelement_view import VisualModeElement

# Use Qt designer to create the .ui layout files to the extent that you assign variables names to widgets and adjust their basic properties. 
# Don't bother adding signals or slots as it's generally easier just to connect them to functions from within the view class.
# 
# The .ui layout files are converted to .py layout files when processed with pyuic or pyside-uic. 
# The .py view files can then import the relevant auto-generated classes from the .py layout files.
# 
# The view class(es) should contain the minimal code required to connect to the signals coming from the widgets in your layout. 
# View events can call and pass basic information to a method in the view class and onto a method in a controller class, where any logic should be. 
# 
# The view doesn't do much apart from link widget events to the relevant controller function, 
# and listen for changes in the model, which are emitted as Qt signals.

class VisualModeScene(QGraphicsScene):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        # self._ui = Ui_MainWindow()
        # self._ui.setupUi(self)

        # listen for model event signals
        self._model.levelsChanged.connect(self.on_LevelModelChanged)
        self._model.projectLoaded.connect(self.on_ProjectLoad)

        self.connectActions()


    def connectActions(self):
        # connect any actions to the controller here
        pass

    def loadScene(self, scene):
        self.scene = self._model.getInstByID(scene.id)
        for element in self.scene.elements:
            widget = VisualModeElement(element)
            self.addWidget(widget)

    @Slot()
    def on_ProjectLoad(self):
        # might need this
        pass

    @Slot()
    def on_LevelModelChanged(self):
        # might need this
        pass

    @Slot(str)
    def on_LevelItemChanged(self, index):
        item = self._model.levels_model.itemFromIndex(index)

        if item.type == "SCENE":
            self.loadScene(item)
            print("load a new scene")