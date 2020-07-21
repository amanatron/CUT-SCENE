from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from views.mainwindow_view_ui import Ui_MainWindow
import os

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

        # connect widgets to controller
        self._ui.levelsWidget.currentRowChanged.connect(self._main_controller.level_selected)
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # listen for model event signals
        self._model.projectLoaded.connect(self.on_ProjectLoad)
        self._model.activeLevelChanged.connect(self.on_levelChange)

        self.connect_actions()

        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

    def connect_actions(self):
        # self.actionNew.triggered.connect()
        self._ui.actionOpen.triggered.connect(self.openProject)
        # self.actionSave.triggered.connect()
        # self.actionSaveAs.triggered.connect()
        # self.actionExit.triggered.connect()
        # self.actionUndo.triggered.connect()
        # self.actionRedo.triggered.connect()

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


    def openProject(self):
        # toProceed = self.handleUnsavedChanges()
        toProceed = True
        if not toProceed:
            return
        projectPath = QFileDialog.getOpenFileName(self, 'Open Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self._main_controller.load_project(projectPath)

    def closeEvent(self, event):
        # Save window layout before closing
        self._settings.setValue("geometry", self.saveGeometry())
        self._settings.setValue("windowState", self.saveState())

    @Slot()
    def on_ProjectLoad(self):
        levels = self._model.get_levels()
        levelnames = [level.name for level in levels]
        self._ui.levelsWidget.addItems(levelnames)

    @Slot(int)
    def on_levelChange(self, value):
        self._ui.levelWidget.clear()
        level = self._model.get_levels()[value].get()
        levelitems = [item.name for item in level]
        self._ui.levelWidget.addItems(levelitems)

    # @Slot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)