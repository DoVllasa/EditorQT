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

        self.imageName_2 = QLabel(self.centralwidget)
        self.imageName_2.setObjectName(u"imageName_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageName_2.sizePolicy().hasHeightForWidth())
        self.imageName_2.setSizePolicy(sizePolicy2)
        self.imageName_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.imageName_2, 0, 1, 1, 1)

        self.amountParcels = QLabel(self.centralwidget)
        self.amountParcels.setObjectName(u"amountParcels")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.amountParcels.sizePolicy().hasHeightForWidth())
        self.amountParcels.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.amountParcels, 2, 2, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy5)
        self.info.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.info, 0, 2, 1, 1)

        self.imageView = QGraphicsView(self.centralwidget)
        self.imageView.setObjectName(u"imageView")
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setMinimumSize(QSize(400, 0))

        self.gridLayout.addWidget(self.imageView, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.directoryName = QLabel(self.centralwidget)
        self.directoryName.setObjectName(u"directoryName")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.directoryName.sizePolicy().hasHeightForWidth())
        self.directoryName.setSizePolicy(sizePolicy7)
        self.directoryName.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.directoryName, 0, 0, 1, 1)

        self.imageName = QListWidget(self.centralwidget)
        self.imageName.setObjectName(u"imageName")
        sizePolicy6.setHeightForWidth(self.imageName.sizePolicy().hasHeightForWidth())
        self.imageName.setSizePolicy(sizePolicy6)
        self.imageName.setMinimumSize(QSize(150, 0))
        self.imageName.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.imageName, 1, 0, 1, 1)


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
        self.imageName_2.setText(QCoreApplication.translate("MainWindow", u"<<Image Name>>", None))
        self.amountParcels.setText(QCoreApplication.translate("MainWindow", u"<<Amount Parcels>>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"<<Info>>", None))
        self.label_5.setText("")
        self.directoryName.setText(QCoreApplication.translate("MainWindow", u"<<Directory Name>>", None))
    # retranslateUi

