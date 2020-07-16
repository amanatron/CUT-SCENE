# CUTSCENE
from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QAction, QMessageBox, QFileDialog
from PySide2.QtCore import QSettings, QRect
from PySide2.QtGui import QIcon
import cutscene
import os

class MainWindow(QMainWindow):
    def __init__(self, projectPath=None, default_window_size=(1500, 800)):
        # Initialise and Load settings
        super().__init__()
        self.settings = QSettings("AmanTrivedi", "CUTSCENE")

        # Load Project from projectPath
        self.projectPath = projectPath
        self.project = None
        if self.projectPath:
            self.project = cutscene.loadProject(self.projectPath)

        # Restore window geometry if it's saved in settings
        if any(self.settings.value(x) is None for x in ["geometry", "windowState"]):
            qtRectangle = QRect(0, 0, *default_window_size)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.setGeometry(qtRectangle)
        else:
            self.restoreGeometry(self.settings.value("geometry"))
            self.restoreState(self.settings.value("windowState"))

        # Create menubar and associated functions
        self.createMenu()

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        searchMenu = mainMenu.addMenu("Font")
        helpMenu = mainMenu.addMenu("Help")
        newAction = QAction("New", self)
        newAction.setShortcut("Ctrl+N")
        openAction = QAction("Open", self)
        openAction.setShortcut("Ctrl+O")
        saveAction = QAction("Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveasAction = QAction("Save As", self)
        saveasAction.setShortcut("Ctrl+Shift+S")
        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        newAction.triggered.connect(self.newProject)
        openAction.triggered.connect(self.openProject)
        saveAction.triggered.connect(self.saveApp)
        saveasAction.triggered.connect(self.saveasApp)
        exitAction.triggered.connect(self.exitApp)
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveasAction)
        fileMenu.addAction(exitAction)

    def exitApp(self):
        # Prompt user to save
        self.unsavedChanges()
        self.close()

    def unsavedChanges(self):
        if self.project:
            retval = self.showSaveOrClose()
            if retval == QMessageBox.Save:
                self.saveApp()
            elif retval == QMessageBox.Discard:
                pass
            elif retval == QMessageBox.Cancel:
                return

    def saveApp(self):
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

    def saveasApp(self):
        if not self.project:
            return
        projectPath = QFileDialog.getSaveFileName(self, 'Save Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            cutscene.saveProject(self.project, projectPath)
            self.projectPath = projectPath

    def newProject(self):
        self.unsavedChanges()
        params = {"name": "a", 
                  "description": "b", 
                  "genre": "c", 
                  "author": "d"}
        self.projectPath = None
        self.project = cutscene.CutSceneProject(**params)

    def openProject(self):
        self.unsavedChanges()
        projectPath = QFileDialog.getOpenFileName(self, 'Open Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self.project = cutscene.loadProject(self.projectPath)
            self.projectPath = projectPath

    def showSaveOrClose(self):
        msg = QMessageBox()
        msg.setText("Do you want to save your changes?")
        msg.setWindowTitle("CutScene")
        msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Save)
        return msg.exec_()

    def closeEvent(self, event):
        self.unsavedChanges()
        # Save window layout
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        QMainWindow.closeEvent(self, event)
 
