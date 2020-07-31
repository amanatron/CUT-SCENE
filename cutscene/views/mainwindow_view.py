from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot, QItemSelectionModel
from views.mainwindow_view_ui import Ui_MainWindow

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

class MainView(QMainWindow):
    def __init__(self, model, main_controller, settings, defaultWindowSize=(1500, 800)):
        super().__init__()

        self._model = model
        self._settings = settings
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # Restore window geometry if it's saved in settings
        if any(self._settings.value(x) is None for x in ["geometry", "windowState"]):
            qtRectangle = QRect(0, 0, *defaultWindowSize)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.setGeometry(qtRectangle)
        else:
            self.restoreGeometry(self._settings.value("geometry"))
            self.restoreState(self._settings.value("windowState"))

        # listen for model event signals
        self._model.levelsChanged.connect(self.on_LevelModelChanged)
        self._model.projectLoaded.connect(self.on_ProjectLoad)

        self.connect_actions()


    def levelsViewClicked(self, index):
        """ Expand items in the levelsView on single click rather than double click """
        if self._ui.levelsView.isExpanded(index):
            self._ui.levelsView.collapse(index)
        else:
            self._ui.levelsView.expand(index)

    def connect_actions(self):
        self._ui.buttonAddLevel.clicked.connect(self._main_controller.newLevel)
        self._ui.buttonAddSubLevel.clicked.connect(self._main_controller.newSubLevel)
        self._ui.buttonAddScene.clicked.connect(self._main_controller.newScene)
        self._ui.actionNew.triggered.connect(self._main_controller.newProject)
        self._ui.actionOpen.triggered.connect(self._main_controller.openProject)
        self._ui.actionSave.triggered.connect(self._main_controller.saveProject)
        self._ui.actionSaveAs.triggered.connect(self._main_controller.saveProjectAs)
        # self._ui.actionExit.triggered.connect(self._main_controller)
        self._ui.actionUndo.triggered.connect(self._main_controller.undo)
        self._ui.actionRedo.triggered.connect(self._main_controller.redo)

    def handleUnsavedChanges(self):
        if self._model.get_project():
            retval = self.saveCloseDialogue()
            if retval == QMessageBox.Save:
                print("Implement save project")
                return True # Save, okay to proceed
            elif retval == QMessageBox.Discard:
                return True # No save, okay to proceed
            elif retval == QMessageBox.Cancel:
                return False # No save, not okay to proceed

    def closeEvent(self, event):
        # Save window layout before closing
        self._settings.setValue("geometry", self.saveGeometry())
        self._settings.setValue("windowState", self.saveState())

    @Slot()
    def on_ProjectLoad(self):
        # manually select root item for convenience and connection some signals to slots
        self._ui.levelsView.setModel(self._model.levels_model)
        self._ui.levelsView.expandToDepth(0)
        self._ui.levelsView.selectionModel().currentChanged.connect(self._main_controller.levelItemSelected)
        self._ui.levelsView.selectionModel().currentChanged.connect(self.on_LevelItemChanged)
        self._ui.levelsView.clicked.connect(self.levelsViewClicked)
        idx = self._model.levels_model.index(0,0)
        self._ui.levelsView.selectionModel().select(idx, QItemSelectionModel.SelectCurrent)
        self._ui.buttonAddLevel.setEnabled(True)
        self._ui.buttonAddSubLevel.setEnabled(False)
        self._ui.buttonAddScene.setEnabled(False)
        print("new project loaded")

    @Slot()
    def on_LevelModelChanged(self):
        pass
        # 
        # levels = self._model.get_levels()
        # levelnames = [level.name for level in levels]
        # self._ui.levelsView.addItems(levelnames)

    @Slot(str)
    def on_LevelItemChanged(self, index):
        item = self._model.levels_model.itemFromIndex(index)
        if item.type == "CUTSCENEPROJECT":
            self._ui.buttonAddLevel.setEnabled(True)
            self._ui.buttonAddSubLevel.setEnabled(False)
            self._ui.buttonAddScene.setEnabled(False)
        else:
            self._ui.buttonAddLevel.setEnabled(True)
            self._ui.buttonAddSubLevel.setEnabled(True)
            self._ui.buttonAddScene.setEnabled(True)
        # elif itemType == "LEVEL":
        #     self._ui.buttonAddLevel.setEnabled(True)
        #     self._ui.buttonAddSubLevel.setEnabled(True)
        #     self._ui.buttonAddScene.setEnabled(True)
        # elif itemType == "SUBLEVEL":
        #     self._ui.buttonAddLevel.setEnabled(True)
        #     self._ui.buttonAddSubLevel.setEnabled(True)
        #     self._ui.buttonAddScene.setEnabled(True)
        # elif itemType == "SCENE":
        #     self._ui.buttonAddLevel.setEnabled(True)
        #     self._ui.buttonAddSubLevel.setEnabled(True)
        #     self._ui.buttonAddScene.setEnabled(True)

    # @Slot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)