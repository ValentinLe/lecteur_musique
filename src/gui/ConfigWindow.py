
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QDesktopWidget, QFileDialog, QLabel
from util.Config import Config


class ConfigWindow(QWidget):
    def __init__(self, board, parent=None):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.b = board
        self.config = Config("config/config.conf")

        # centrer la fenetre
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        labPath = QLabel("Chemin des musiques :")
        self.entryPath = QLineEdit()
        path = self.config.getValueOf("path")
        if path:
            self.entryPath.setText(path)
        bBrowsePath = QPushButton("Parcourir...")
        bBrowsePath.clicked.connect(self.selectPath)

        bAccept = QPushButton("Ok")
        bAccept.setProperty("class", "specialButton")
        bAccept.clicked.connect(self.acceptModifications)
        bCancel = QPushButton("Annuler")
        bCancel.setProperty("class", "specialButton")
        bCancel.clicked.connect(self.cancelModifications)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layoutPath = QHBoxLayout()
        layoutPath.addWidget(self.entryPath)
        layoutPath.addWidget(bBrowsePath)
        layoutLabEntry = QVBoxLayout()
        layoutLabEntry.addWidget(labPath)
        layoutLabEntry.addLayout(layoutPath)

        layoutBottom = QHBoxLayout()
        layoutBottom.addStretch()
        layoutBottom.addWidget(bAccept)
        layoutBottom.addWidget(bCancel)

        layout.addLayout(layoutLabEntry)
        layout.addStretch()
        layout.addLayout(layoutBottom)

    def selectPath(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select directory')
        if folder:
            self.entryPath.setText(folder)

    def acceptModifications(self):
        folder = self.entryPath.text()
        self.config.setValueOf("path", folder)
        self.config.save()
        self.b.setDirectory(folder)
        self.close()

    def cancelModifications(self):
        self.close()

    def close(self):
        QWidget.close(self)
        self.parent.close()
