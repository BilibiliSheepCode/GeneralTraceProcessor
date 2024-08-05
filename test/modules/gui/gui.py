from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from PySide6.QtCore import (Qt, Signal)

from file import file

import sys

from gui.ui.MainWindows_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    quitSignal = Signal(QMainWindow)

    def __init__(self) -> None:
        # init
        super().__init__()
        self.setupUi(self)

        self.classfile = file.File_GTP()

        self.bind()

        

    def bind(self):
        # File-Quit
        self.quitSignal.connect(self.classfile.quit)
        self.actionQuit.triggered.connect(lambda : self.quitSignal.emit(self))