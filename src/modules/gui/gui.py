from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QWidget, 
                               QFrame, 
                               QPushButton, 
                               QStyle, 
                               QVBoxLayout, 
                               QLabel)
from PySide6.QtCore import (Qt, 
                            Signal)
from PySide6.QtGui import (QAction)

from modules.gui.funcions.file import file

import sys

from modules.gui.ui.MainWindow.MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    fileNewSignal = Signal(QMainWindow)
    fileOpenSignal = Signal(QMainWindow)
    fileOpenRecentSignal = Signal(QMainWindow)
    fileSaveSignal = Signal(QMainWindow)
    fileSaveAsSignal = Signal(QMainWindow)
    fileSaveCopySignal = Signal(QMainWindow)
    fileImportSignal = Signal(QMainWindow)
    fileExportSignal = Signal(QMainWindow)
    fileQuitSignal = Signal(QMainWindow)

    editUndoSignal = Signal(QMainWindow)
    editRedoSignal = Signal(QMainWindow)
    editPreferencesSignal = Signal(QMainWindow)

    def __init__(self) -> None:
        # init
        super().__init__()
        self.setupUi(self)

        self.fileFunctions = file.FileFunctions()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.actionUndo)
        self.addAction(self.actionRedo)

        self.toolList = QFrame(self)
        self.toolList.setGeometry(0, self.menubar.frameSize().height(), 90, self.frameSize().height() - self.menubar.frameSize().height())
        self.toolListLayout = QVBoxLayout(self)
        self.toolListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.toolListLayout.addWidget(QPushButton('Edit'))
        self.toolList.setLayout(self.toolListLayout)

        self.bind()

        

    def bind(self):
        # File-New
        self.fileNewSignal.connect(self.fileFunctions.new)
        self.actionNew.triggered.connect(lambda : self.fileNewSignal.emit(self))

        # File-Open
        self.fileOpenSignal.connect(self.fileFunctions.open)
        self.actionOpen.triggered.connect(lambda : self.fileOpenSignal.emit(self))

        # File-Open Recent
        self.fileOpenRecentSignal.connect(self.fileFunctions.openRecent)
        self.actionOpen_Recent.triggered.connect(lambda : self.fileOpenRecentSignal.emit(self))

        # File-Save
        self.fileSaveSignal.connect(self.fileFunctions.save)
        self.actionSave.triggered.connect(lambda : self.fileSaveSignal.emit(self))

        # File-Save As
        self.fileSaveAsSignal.connect(self.fileFunctions.saveAs)
        self.actionSave_As.triggered.connect(lambda : self.fileSaveAsSignal.emit(self))

        # File-Save Copy
        self.fileSaveCopySignal.connect(self.fileFunctions.saveCopy)
        self.actionSave_Copy.triggered.connect(lambda : self.fileSaveCopySignal.emit(self))

        # File-Import
        self.fileImportSignal.connect(self.fileFunctions.importProject)
        self.actionImport.triggered.connect(lambda : self.fileImportSignal.emit(self))

        # File-Export
        self.fileExportSignal.connect(self.fileFunctions.exportProject)
        self.actionExport.triggered.connect(lambda : self.fileExportSignal.emit(self))

        # File-Quit
        self.fileQuitSignal.connect(self.fileFunctions.quit)
        self.actionQuit.triggered.connect(lambda : self.fileQuitSignal.emit(self))
