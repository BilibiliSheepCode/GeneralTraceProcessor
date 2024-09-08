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
import yaml

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
            elif os.path.exists(parent.lineEditInputDirectory.text() + '/' + parent.lineEditProjectName.text()):
                QMessageBox.critical(parent, 'Error When Creating Project', "Project Already Exists!")
                return
            else:
                self.projectName = parent.lineEditProjectName.text()
                self.projectLocate = parent.lineEditInputDirectory.text()
                self.projectDir = self.projectLocate + '/' + self.projectName
                os.mkdir(self.projectDir)
                os.mkdir(self.projectDir + '/cameras')  
                os.mkdir(self.projectDir + '/operates')
                os.mkdir(self.projectDir + '/traceData')
                open(self.projectDir + '/config.yml', "w").close()
                open(self.projectDir + '/cameras' + '/cameras.yml', "w").close()
                open(self.projectDir + '/traceData' + '/traces.yml', "w").close()
                open(self.projectDir + '/operates' + '/operates.yml', "w").close()
            parent.close()
            self.open(mainwindow, self.projectDir)
        self.newWindow.pushButtonSelectDirectory.clicked.connect(lambda : getDir(self.newWindow))
        self.newWindow.pushButtonCancel.clicked.connect(self.newWindow.close)
        self.newWindow.pushButtonOK.clicked.connect(lambda : checkAndSubmit(self.newWindow))

    def open(self, mainwindow : QMainWindow, projectDir = None):
        def load():

            with open(self.projectDir + '/config.yml', 'r') as f:
                data = yaml.safe_load(f)
                self.configYmlData = data
            with open(self.projectDir + '/cameras' + '/cameras.yml', 'r') as f:
                data = yaml.safe_load(f)
                self.camerasYmlData = data
            with open(self.projectDir + '/traceData' + '/traces.yml', 'r') as f:
                data = yaml.safe_load(f)
                self.tracesYmlData = data
            with open(self.projectDir + '/operates' + '/operates.yml', 'r') as f:
                data = yaml.safe_load(f)
                self.operatesYmlData = data

        if projectDir == None:
            self.projectDir = QFileDialog.getExistingDirectory(mainwindow, 'Select Project Directory', './data')
            self.projectLocate, self.projectName = self.projectDir.rsplit('/', 1)
            load()
            return
        else:
            load()

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
    