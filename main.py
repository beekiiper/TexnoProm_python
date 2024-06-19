from PyQt5 import QtGui, QtCore, QtWidgets
import os
import design


class MyFileBrowser(design.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.context_menu)
        self.pushButton.clicked.connect(self.populate)
        self.listView.doubleClicked.connect(self.up)
        self.toolButton.clicked.connect(self.backspace)
        self.lineEdit.editingFinished.connect(self.text_edite)


    def text_edite(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.listView.setModel(self.model)
        self.path = self.lineEdit.text()
        self.listView.setRootIndex(self.model.index(self.path))
    def backspace(self):
        if not self.lineEdit.text() == "path":
             index = self.listView.rootIndex()
             temp = self.model.fileInfo(index).absoluteDir()
             temp.cdUp
             self.listView.setRootIndex(self.model.index(temp.path()))
             index = self.listView.rootIndex()
             self.lineEdit.setText(self.model.filePath(index))

    def up(self):
        index = self.listView.currentIndex()
        if not self.model.fileInfo(index).isFile():
            self.listView.setRootIndex(self.model.index(self.model.filePath(index)))
            self.lineEdit.setText(self.model.filePath(index))

    def populate(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.lineEdit.setText(self.path)
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.listView.setModel(self.model)
        self.listView.setRootIndex(self.model.index(self.path))



    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())


    def open_file(self):
        index = self.listView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
