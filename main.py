import sys
from enum import Enum
from functools import partial

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from mainwindow import Ui_MainWindow
from os import listdir
import os
from os.path import isfile, join


class PolygonAnnotation(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, parent=None):
        super(PolygonAnnotation, self).__init__(parent)
        self.m_points = []
        # self.setZValue(10)
        self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2))
        self.setAcceptHoverEvents(True)

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)

        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.m_items = []

    def number_of_points(self):
        return len(self.m_items)

    def addPoint(self, p):
        self.m_points.append(p)
        # print('MPoints', self.m_points)
        self.setPolygon(QtGui.QPolygonF(self.m_points))
        item = ImageView(self, len(self.m_points) - 1)
        self.scene().addItem(item)
        self.m_items.append(item)
        # print('MITEMS', self.m_items)
        item.setPos(p)

    def removeLastPoint(self):
        if self.m_points:
            self.m_points.pop()
            self.setPolygon(QtGui.QPolygonF(self.m_points))
            it = self.m_items.pop()
            self.scene().removeItem(it)
            del it


    def movePoint(self, i, p):
        if 0 <= i < len(self.m_points):
            self.m_points[i] = self.mapFromScene(p)
            self.setPolygon(QtGui.QPolygonF(self.m_points))

    def move_item(self, index, pos):
        if 0 <= index < len(self.m_items):
            item = self.m_items[index]
            item.setEnabled(False)
            item.setPos(pos)
            item.setEnabled(True)

    def itemChange(self, change, value):
        # print('CHANGE', change)
        # print('VALUE', value)
        if change == QtWidgets.QGraphicsItem.ItemPositionHasChanged:
            for i, point in enumerate(self.m_points):
                self.move_item(i, self.mapToScene(point))
        return super(PolygonAnnotation, self).itemChange(change, value)

    def hoverEnterEvent(self, event):
        self.setBrush(QtGui.QColor(255, 0, 0, 100))
        super(PolygonAnnotation, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))
        super(PolygonAnnotation, self).hoverLeaveEvent(event)


class Instructions(Enum):
    No_Instruction = 0
    Polygon_Instruction = 1


class ImageScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(ImageScene, self).__init__(parent)
        self.image_item = QtWidgets.QGraphicsPixmapItem()
        self.image_item.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.addItem(self.image_item)
        self.current_instruction = Instructions.No_Instruction

    def load_image(self, filename):
        self.image_item.setPixmap(QtGui.QPixmap(filename))
        self.setSceneRect(self.image_item.boundingRect())

    def setCurrentInstruction(self, instruction):
        self.current_instruction = instruction
        self.polygon_item = PolygonAnnotation()
        self.addItem(self.polygon_item)

    def onDeleteItem(self):
        print("POINTS" , self.polygon_item.m_points)
        # print("ITEMS" , ImageScene.image_item)
        for i, point in enumerate(self.polygon_item.m_points):
            self.removeItem(self.polygon_item.m_items[i])

    def mousePressEvent(self, event):
        if self.current_instruction == Instructions.Polygon_Instruction:
            self.polygon_item.removeLastPoint()
            self.polygon_item.addPoint(event.scenePos())
            # movable element
            self.polygon_item.addPoint(event.scenePos())
        super(ImageScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.current_instruction == Instructions.Polygon_Instruction:
            self.polygon_item.movePoint(self.polygon_item.number_of_points() - 1, event.scenePos())
        super(ImageScene, self).mouseMoveEvent(event)

    def onTestCall(self):
        print('SELECTED', self.selectedItems())
        for i in self.selectedItems():
            self.removeItem(i)a
        print('SELECTED', self.selectedItems())
        super(ImageScene, self)

class ImageView(QtWidgets.QGraphicsPathItem):
    circle = QtGui.QPainterPath()
    circle.addEllipse(QtCore.QRectF(-10, -10, 20, 20))
    square = QtGui.QPainterPath()
    square.addRect(QtCore.QRectF(-15, -15, 30, 30))

    def __init__(self, annotation_item, index):
        super(ImageView, self).__init__()
        self.m_annotation_item = annotation_item
        self.m_index = index
        self.setPath(ImageView.circle)
        self.setBrush(QtGui.QColor("blue"))
        self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2))
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setAcceptHoverEvents(True)
        # self.setZValue(11)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def hoverEnterEvent(self, event):
        self.setPath(ImageView.square)
        self.setBrush(QtGui.QColor("blue"))
        super(ImageView, self).hoverEnterEvent(event)


    def hoverLeaveEvent(self, event):
        self.setPath(ImageView.circle)
        self.setBrush(QtGui.QColor("blue"))
        super(ImageView, self).hoverLeaveEvent(event)

    def mouseReleaseEvent(self, event):
        self.setSelected(False)
        super(ImageView, self).mouseReleaseEvent(event)


    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemPositionChange and self.isEnabled():
            self.m_annotation_item.movePoint(self.m_index, value)
        return super(ImageView, self).itemChange(change, value)
    

class NextOrBack(Enum):
    BackItem = 0
    NextItem = 1


class MainWindow(QMainWindow):
    factor = 2.0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Truth Data generator Parcels")
        self.ui.imageView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        self.ui.imageView.setMouseTracking(True)
        self.counterImages = 0
        self.m_view = self.ui.imageView
        self.m_scene = ImageScene(self)
        self.m_view.setScene(self.m_scene)
        self.directory = '/Users/dominim/Desktop/TestData'
        self.filenames = [f for f in listdir(self.directory) if isfile(join(os.path.realpath(self.directory), f))]
        self.realpathImages = []
        for index, filename in enumerate(self.filenames):
            self.realpathImages.append(self.directory + '/' + filename)
            self.ui.imageName.addItem(filename)
        self.load_image(NextOrBack.BackItem)
        self.ui.nextImageButton.clicked.connect(partial(self.load_image, NextOrBack.NextItem.value))
        self.ui.backButton.clicked.connect(partial(self.load_image, NextOrBack.BackItem.value))
        self.ui.removeButton.clicked.connect(self.m_scene.onTestCall)

        QtWidgets.QShortcut(QtGui.QKeySequence.ZoomIn, self.m_view, self.zoomIn)
        QtWidgets.QShortcut(QtGui.QKeySequence.ZoomOut, self.m_view, self.zoomOut)




        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self.m_view,
                            activated=partial(self.m_scene.setCurrentInstruction, Instructions.No_Instruction))

        QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_A), self.m_view,
                            activated=partial(self.m_scene.setCurrentInstruction, Instructions.Polygon_Instruction))

    @QtCore.Slot()
    def zoomIn(self):
        self.zoom(2)

    @QtCore.Slot()
    def zoomOut(self):
        self.zoom(1 / 2)

    def zoom(self, f):
        self.m_view.scale(f, f)
        if self.m_view.scene() is not None:
            self.m_view.centerOn(self.m_view.scene().image_item)

    @QtCore.Slot()
    def load_image(self, imageNavigation):
        if imageNavigation == 1 and self.counterImages < self.realpathImages.__len__() - 1:
            self.counterImages = self.counterImages + 1
        elif imageNavigation == 0 and self.counterImages > 0:
            self.counterImages = self.counterImages - 1
        else:
            self.counterImages = 0

        if self.realpathImages[self.counterImages]:
            self.m_scene.load_image(self.realpathImages[self.counterImages])
            self.m_view.fitInView(self.m_scene.image_item, QtCore.Qt.KeepAspectRatio)
            self.m_view.centerOn(self.m_scene.image_item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
