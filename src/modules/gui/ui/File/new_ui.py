# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/icons/new", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEditProjectName = QLineEdit(Form)
        self.lineEditProjectName.setObjectName(u"lineEditProjectName")

        self.horizontalLayout.addWidget(self.lineEditProjectName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEditInputDirectory = QLineEdit(Form)
        self.lineEditInputDirectory.setObjectName(u"lineEditInputDirectory")

        self.horizontalLayout_2.addWidget(self.lineEditInputDirectory)

        self.pushButtonSelectDirectory = QPushButton(Form)
        self.pushButtonSelectDirectory.setObjectName(u"pushButtonSelectDirectory")

        self.horizontalLayout_2.addWidget(self.pushButtonSelectDirectory)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonOK = QPushButton(Form)
        self.pushButtonOK.setObjectName(u"pushButtonOK")

        self.horizontalLayout_3.addWidget(self.pushButtonOK)

        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_3.addWidget(self.pushButtonCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"New Project", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Project Name", None))
        self.label.setText(QCoreApplication.translate("Form", u"Storage Directory", None))
        self.pushButtonSelectDirectory.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButtonOK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

