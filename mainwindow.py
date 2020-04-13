# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1340, 875)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(50, 500))
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionshowTruth = QAction(MainWindow)
        self.actionshowTruth.setObjectName(u"actionshowTruth")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.backButton)

        self.nextImageButton = QPushButton(self.centralwidget)
        self.nextImageButton.setObjectName(u"nextImageButton")
        sizePolicy1.setHeightForWidth(self.nextImageButton.sizePolicy().hasHeightForWidth())
        self.nextImageButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nextImageButton)

        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout.addWidget(self.removeButton)

        self.saveTruthButton = QPushButton(self.centralwidget)
        self.saveTruthButton.setObjectName(u"saveTruthButton")
        sizePolicy1.setHeightForWidth(self.saveTruthButton.sizePolicy().hasHeightForWidth())
        self.saveTruthButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.saveTruthButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.imageName = QListWidget(self.centralwidget)
        self.imageName.setObjectName(u"imageName")
        sizePolicy2.setHeightForWidth(self.imageName.sizePolicy().hasHeightForWidth())
        self.imageName.setSizePolicy(sizePolicy2)
        self.imageName.setMinimumSize(QSize(150, 0))
        self.imageName.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.imageName, 1, 0, 1, 1)

        self.directoryName = QLabel(self.centralwidget)
        self.directoryName.setObjectName(u"directoryName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.directoryName.sizePolicy().hasHeightForWidth())
        self.directoryName.setSizePolicy(sizePolicy3)
        self.directoryName.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.directoryName, 0, 0, 1, 1)

        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy4)
        self.info.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.info, 0, 2, 1, 1)

        self.imageView = QGraphicsView(self.centralwidget)
        self.imageView.setObjectName(u"imageView")
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setMinimumSize(QSize(400, 0))

        self.gridLayout.addWidget(self.imageView, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout.addWidget(self.label)

        self.armButton = QPushButton(self.centralwidget)
        self.armButton.setObjectName(u"armButton")

        self.verticalLayout.addWidget(self.armButton)

        self.unknownButton = QPushButton(self.centralwidget)
        self.unknownButton.setObjectName(u"unknownButton")
        self.unknownButton.setFlat(False)

        self.verticalLayout.addWidget(self.unknownButton)

        self.restButton = QPushButton(self.centralwidget)
        self.restButton.setObjectName(u"restButton")

        self.verticalLayout.addWidget(self.restButton)

        self.flatButton = QPushButton(self.centralwidget)
        self.flatButton.setObjectName(u"flatButton")

        self.verticalLayout.addWidget(self.flatButton)

        self.pouchButton = QPushButton(self.centralwidget)
        self.pouchButton.setObjectName(u"pouchButton")

        self.verticalLayout.addWidget(self.pouchButton)

        self.bagButton = QPushButton(self.centralwidget)
        self.bagButton.setObjectName(u"bagButton")

        self.verticalLayout.addWidget(self.bagButton)

        self.boxButton = QPushButton(self.centralwidget)
        self.boxButton.setObjectName(u"boxButton")

        self.verticalLayout.addWidget(self.boxButton)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.imageName_2 = QLabel(self.centralwidget)
        self.imageName_2.setObjectName(u"imageName_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imageName_2.sizePolicy().hasHeightForWidth())
        self.imageName_2.setSizePolicy(sizePolicy6)
        self.imageName_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.imageName_2, 0, 1, 1, 1)

        self.amountParcels = QLabel(self.centralwidget)
        self.amountParcels.setObjectName(u"amountParcels")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.amountParcels.sizePolicy().hasHeightForWidth())
        self.amountParcels.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.amountParcels, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1340, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.unknownButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionshowTruth.setText(QCoreApplication.translate("MainWindow", u"Show Truthdata", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"<< Back", None))
        self.nextImageButton.setText(QCoreApplication.translate("MainWindow", u"Next >>", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"remove", None))
        self.saveTruthButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_5.setText("")
        self.directoryName.setText(QCoreApplication.translate("MainWindow", u"<<Directory Name>>", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.label.setText("")
        self.armButton.setText(QCoreApplication.translate("MainWindow", u"Arm", None))
        self.unknownButton.setText(QCoreApplication.translate("MainWindow", u"Unkown", None))
        self.restButton.setText(QCoreApplication.translate("MainWindow", u"Rest (Trash)", None))
        self.flatButton.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.pouchButton.setText(QCoreApplication.translate("MainWindow", u"Pouch", None))
        self.bagButton.setText(QCoreApplication.translate("MainWindow", u"Bag", None))
        self.boxButton.setText(QCoreApplication.translate("MainWindow", u"Box", None))
        self.label_2.setText("")
        self.imageName_2.setText(QCoreApplication.translate("MainWindow", u"<<Image Name>>", None))
        self.amountParcels.setText(QCoreApplication.translate("MainWindow", u"<<Amount Parcels>>", None))
    # retranslateUi

