import os
from PyQt5 import QtWidgets, QtGui

class EmptyFolderFinder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.start_dir = ""
        self.empty_folders = []

        self.folder_input = QtWidgets.QLineEdit()
        self.folder_input.setPlaceholderText("Enter start directory")
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.list_widget = QtWidgets.QListWidget()
        self.delete_button = QtWidgets.QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.folder_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def search(self):
        self.start_dir = self.folder_input.text()
        self.empty_folders = []

        for root, dirs, files in os.walk(self.start_dir):
            for dir in dirs:
                if os.listdir(os.path.join(root, dir)) == []:
                    self.empty_folders.append(os.path.join(root, dir))

        self.list_widget.clear()
        self.list_widget.addItems(self.empty_folders)

    def delete(self):
        for folder in self.empty_folders:
            try:
                os.rmdir(folder)
                self.list_widget.takeItem(self.empty_folders.index(folder))
                self.empty_folders.remove(folder)
            except PermissionError:
                pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = EmptyFolderFinder()
    window.show()
    app.exec_()
