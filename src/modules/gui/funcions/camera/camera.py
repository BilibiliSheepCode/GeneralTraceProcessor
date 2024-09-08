from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QWidget, 
                               QFrame,
                               QPushButton, 
                               QStyle, 
                               QVBoxLayout, 
                               QFileDialog,
                               QMessageBox,
                               QLabel)
from modules.gui.ui.Camera.new_ui import Ui_Form as New_Ui_From

import os
import yaml

class New(QWidget, New_Ui_From):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class CameraFunctions():
    def __init__(self) -> None:
        pass

    def new(self, mainwindow : QMainWindow):
        self.newWindow = New()
        self.newWindow.show()