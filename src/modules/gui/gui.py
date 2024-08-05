from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from PySide6.QtCore import (Qt, Signal)

from modules.file import file

import sys

from modules.gui.ui.MainWindows_ui import Ui_MainWindow

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

        self.fileObject = file.File_GTP()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.actionUndo)
        self.addAction(self.actionRedo)

        self.bind()

        

    def bind(self):
        # File-New
        self.fileNewSignal.connect(self.fileObject.new)
        self.actionNew.triggered.connect(lambda : self.fileNewSignal.emit(self))

        # File-Open
        self.fileOpenSignal.connect(self.fileObject.open)
        self.actionOpen.triggered.connect(lambda : self.fileOpenSignal.emit(self))

        # File-Open Recent
        self.fileOpenRecentSignal.connect(self.fileObject.openRecent)
        self.actionOpen_Recent.triggered.connect(lambda : self.fileOpenRecentSignal.emit(self))

        # File-Save
        self.fileSaveSignal.connect(self.fileObject.save)
        self.actionSave.triggered.connect(lambda : self.fileSaveSignal.emit(self))

        # File-Save As
        self.fileSaveAsSignal.connect(self.fileObject.saveAs)
        self.actionSave_As.triggered.connect(lambda : self.fileSaveAsSignal.emit(self))

        # File-Save Copy
        self.fileSaveCopySignal.connect(self.fileObject.saveCopy)
        self.actionSave_Copy.triggered.connect(lambda : self.fileSaveCopySignal.emit(self))

        # File-Import
        self.fileImportSignal.connect(self.fileObject.importProject)
        self.actionImport.triggered.connect(lambda : self.fileImportSignal.emit(self))

        # File-Export
        self.fileExportSignal.connect(self.fileObject.exportProject)
        self.actionExport.triggered.connect(lambda : self.fileExportSignal.emit(self))

        # File-Quit
        self.fileQuitSignal.connect(self.fileObject.quit)
        self.actionQuit.triggered.connect(lambda : self.fileQuitSignal.emit(self))
