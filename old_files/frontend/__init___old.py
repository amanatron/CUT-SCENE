# CUTSCENE
from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QAction, QMessageBox, QFileDialog, QUndoStack, QUndoCommand
from PySide2.QtCore import QSettings, QRect
from PySide2.QtGui import QIcon
import cutscene
from frontend.commands import *
import os

class MainWindow(QMainWindow):
    def __init__(self, projectPath=None, defaultWindowSize=(1500, 800)):
        # Initialise and Load settings
        super().__init__()
        self.settings = QSettings("AmanTrivedi", "CUTSCENE")
        self.setWindowTitle("CutScene")

        # Load Project from projectPath
        self.projectPath = projectPath
        self.project = None
        if self.projectPath:
            self.project = cutscene.loadProject(self.projectPath)

        # Restore window geometry if it's saved in settings
        if any(self.settings.value(x) is None for x in ["geometry", "windowState"]):
            qtRectangle = QRect(0, 0, *defaultWindowSize)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.setGeometry(qtRectangle)
        else:
            self.restoreGeometry(self.settings.value("geometry"))
            self.restoreState(self.settings.value("windowState"))

        # Create undo stack
        self.undoStack = QUndoStack(self)
        # Create actions (open, new, save, etc)
        self.createActions()
        # Create menubar (file, view, etc)
        self.createMenu()

    def createActions(self):
        self.newAction = QAction("New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setToolTip("Create a new project")
        self.newAction.triggered.connect(self.newProject)
        self.openAction = QAction("Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setToolTip("Open an existing project")
        self.openAction.triggered.connect(self.openProject)
        self.saveAction = QAction("Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setToolTip("Save this project")
        self.saveAction.triggered.connect(self.saveProject)
        self.saveAsAction = QAction("Save As", self)
        self.saveAsAction.setShortcut("Ctrl+Shift+S")
        self.saveAsAction.setToolTip("Save a copy of this project")
        self.saveAsAction.triggered.connect(self.saveProjectAs)
        self.exitAction = QAction("Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setToolTip("Exit CutScene")
        self.exitAction.triggered.connect(self.exitApp)
        self.undoAction = QAction("Undo", self)
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.setToolTip("Undo most recent action")
        self.undoAction.triggered.connect(self.undoStack.undo)
        self.redoAction = QAction("Redo", self)
        self.redoAction.setShortcut("Ctrl+Shift+Z")
        self.redoAction.setToolTip("Redo most recent action")
        self.redoAction.triggered.connect(self.undoStack.redo)

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        searchMenu = mainMenu.addMenu("Search")
        helpMenu = mainMenu.addMenu("Help")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.saveAsAction)
        fileMenu.addAction(self.exitAction)
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.redoAction)

    def exitApp(self):
        self.close()

    def handleUnsavedChanges(self):
        if self.project:
            retval = self.saveCloseDialogue()
            if retval == QMessageBox.Save:
                self.saveProject()
                return True # Save, okay to proceed
            elif retval == QMessageBox.Discard:
                return True # No save, okay to proceed
            elif retval == QMessageBox.Cancel:
                return False # No save, not okay to proceed

    def saveProject(self):
        if not self.project:
            return
        if self.projectPath:
            projectPath = self.projectPath
        else:
            projectPath = QFileDialog.getSaveFileName(self, 'Save Project', 
                    os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            cutscene.saveProject(self.project, projectPath)
            self.projectPath = projectPath

    def saveProjectAs(self):
        if not self.project:
            return
        projectPath = QFileDialog.getSaveFileName(self, 'Save Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            cutscene.saveProject(self.project, projectPath)
            self.projectPath = projectPath

    def newProject(self):
        toProceed = self.handleUnsavedChanges()
        if not toProceed:
            return
        params = {"name": "a", 
                  "description": "b", 
                  "genre": "c", 
                  "author": "d"}
        self.projectPath = None
        self.project = cutscene.CutSceneProject(**params)

    def openProject(self):
        toProceed = self.handleUnsavedChanges()
        if not toProceed:
            return
        projectPath = QFileDialog.getOpenFileName(self, 'Open Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self.project = cutscene.loadProject(self.projectPath)
            self.projectPath = projectPath

    def saveCloseDialogue(self):
        msg = QMessageBox()
        msg.setText("Do you want to save your changes?")
        msg.setWindowTitle("CutScene")
        msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Save)
        return msg.exec_()

    def closeEvent(self, event):
        # Prompt user to save
        toProceed = self.handleUnsavedChanges()
        if not toProceed:
            event.ignore()
        # Save window layout before closing
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
 
