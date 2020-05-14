#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os, numpy, PIL, csv
from PySide2 import QtCore, QtGui, QtWidgets
from PIL import Image, ImagePalette, ImageQt, ImageSequence

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle("ListView item move for drag and drop")
        self.view = FrameListView()
        self.setCentralWidget(self.view)
        self.show()

class FrameListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.model = MyStandardItemModel()
        self.setModel(self.model)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)

class MyStandardItemModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(self.__class__, self).__init__()
        for label in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            item = QtGui.QStandardItem(label)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
            self.appendRow(item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
