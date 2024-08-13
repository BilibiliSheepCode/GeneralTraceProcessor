from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QWidget, 
                               QFrame, 
                               QPushButton, 
                               QStyle, 
                               QVBoxLayout, 
                               QLabel)
from PySide6.QtCore import (Qt, 
                            Signal,
                            QSize)
from PySide6.QtGui import (QAction,
                           QPixmap)

from modules.gui.funcions.file import file
from modules.gui.funcions.render import render

import sys
import icon_rc

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
        self.pltRender = render.render()

        self.separator = QAction(self)
        self.separator.setSeparator(True)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.actionCopy)
        self.addAction(self.actionPaste)
        self.addAction(self.actionDelete)
        self.addAction(self.separator)
        self.addAction(self.actionUndo)
        self.addAction(self.actionRedo)

        self.toolList = QFrame(self)
        self.toolList.setGeometry(0, self.menubar.frameSize().height(), 64, self.frameSize().height() - self.menubar.frameSize().height())
        self.toolListLayout = QVBoxLayout(self)
        self.toolListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.buttonCopy = QPushButton(QPixmap(':/icons/copy'), '')
        self.buttonCopy.setIconSize(QSize(32, 32))
        self.buttonCopy.clicked.connect(self.actionCopy.trigger)

        self.buttonPaste = QPushButton(QPixmap(':/icons/paste'), '')
        self.buttonPaste.clicked.connect(self.actionPaste.trigger)
        self.buttonPaste = QPushButton(QPixmap(':/icons/paste'), '')
        self.buttonPaste.setIconSize(QSize(32, 32))
        self.buttonPaste.clicked.connect(self.actionPaste.trigger)

        self.buttonDelete = QPushButton(QPixmap(':/icons/delete'), '')
        self.buttonDelete.clicked.connect(self.actionDelete.trigger)
        self.buttonDelete = QPushButton(QPixmap(':/icons/delete'), '')
        self.buttonDelete.setIconSize(QSize(32, 32))
        self.buttonDelete.clicked.connect(self.actionDelete.trigger)

        self.toolListLayout.addWidget(self.buttonCopy)
        self.toolListLayout.addWidget(self.buttonPaste)
        self.toolListLayout.addWidget(self.buttonDelete)
        self.toolList.setLayout(self.toolListLayout)

        self.renderFrame = QFrame(self)
        self.renderFrame.setGeometry(64, self.menubar.frameSize().height(), self.frameSize().width() - 64, self.frameSize().height() - self.menubar.frameSize().height())
        self.renderFrameLayout = QVBoxLayout(self)
        renderWindow, renderToolBar = self.pltRender.render(self)
        self.renderFrameLayout.addWidget(renderWindow)
        self.renderFrameLayout.addWidget(renderToolBar)
        self.renderFrame.setLayout(self.renderFrameLayout)


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
