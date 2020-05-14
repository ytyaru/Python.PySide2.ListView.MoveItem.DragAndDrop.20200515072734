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
        self.widget = FrameListView()
        self.setCentralWidget(self.widget)
        self.show()

class FrameListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.model = FrameListModel()
        self.setModel(self.model)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)

class FrameListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.__datas = []
        for label in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            d = {}; d[QtCore.Qt.DisplayRole] = label;
            self.__datas.append(d)
    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid(): return 0
        return len(self.__datas)
    def data(self, index, role=QtCore.Qt.DisplayRole):# https://doc.qt.io/qtforpython/PySide2/QtCore/Qt.html
        if role == QtCore.Qt.DisplayRole:
            return self.__datas[index.row()][role]
    def appendRow(self, value=None):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        d = {}; d[QtCore.Qt.DisplayRole] = value if value else 'Z';
        self.__datas.append(d)
        self.endInsertRows()
    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction
    def flags(self, index): # http://www.walletfox.com/course/qtreorderablelist.php
        defaultFlags = super(self.__class__, self).flags(index)
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled  | defaultFlags

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

