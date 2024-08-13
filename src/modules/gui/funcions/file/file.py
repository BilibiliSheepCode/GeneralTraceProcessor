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
from modules.gui.ui.File.new_ui import Ui_Form as New_Ui_From

import os
import icon_rc

class New(QWidget, New_Ui_From):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)


class FileFunctions():
    def __init__(self) -> None:
        pass

    def new(self, mainwindow : QMainWindow):
        self.newWindow = New()
        self.newWindow.show()
        def getDir(parent : QWidget):
            parent.dir = QFileDialog.getExistingDirectory(parent, 'Select Saving Directory', './data')
            parent.lineEditInputDirectory.setText(parent.dir)
        def checkAndSubmit(parent : QWidget):
            if parent.lineEditProjectName.text() == '':
                QMessageBox.critical(parent, 'Error When Creating Project', "Project Name Can't be Empty!")
                return
            elif parent.lineEditInputDirectory.text() == '':
                QMessageBox.critical(parent, 'Error When Creating Project', "Saving Directory Can't be Empty!")
                return
            else:
                self.projectDir = parent.lineEditInputDirectory.text() + '/' + parent.lineEditProjectName.text()
                os.mkdir(self.projectDir)
                os.mkdir(self.projectDir + '/cameraParam')  
                os.mkdir(self.projectDir + '/operates')
                os.mkdir(self.projectDir + '/traceData')
                open(self.projectDir + '/config.yml', "w").close()
            parent.close()
            open(mainwindow, self.projectDir)
        self.newWindow.pushButtonSelectDirectory.clicked.connect(lambda : getDir(self.newWindow))
        self.newWindow.pushButtonCancel.clicked.connect(self.newWindow.close)
        self.newWindow.pushButtonOK.clicked.connect(lambda : checkAndSubmit(self.newWindow))

    def open(self, mainwindow : QMainWindow, projectDir = None):
        if projectDir == None:
            pass
        else:
            pass

    def openRecent(self, mainwindow : QMainWindow):
        pass

    def save(self, mainwindow : QMainWindow):
        pass

    def saveAs(self, mainwindow : QMainWindow):
        pass

    def saveCopy(self, mainwindow : QMainWindow):
        pass

    def importProject(self, mainwindow : QMainWindow):
        pass

    def exportProject(self, mainwindow : QMainWindow):
        pass

    def quit(self, mainwindow : QMainWindow):
        mainwindow.close()
        pass
    