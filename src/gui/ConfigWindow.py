
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QDesktopWidget, QFileDialog


class ConfigWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setGeometry(500, 500, 600, 100)

        # centrer la fenetre
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.entryPath = QLineEdit()
        bBrowsePath = QPushButton("Parcourir...")
        bBrowsePath.clicked.connect(self.selectPath)

        bAccept = QPushButton("Ok")
        bAccept.clicked.connect(self.acceptModifications)
        bCancel = QPushButton("Annuler")
        bCancel.clicked.connect(self.cancelModifications)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layoutPath = QHBoxLayout()
        layoutPath.addWidget(self.entryPath)
        layoutPath.addWidget(bBrowsePath)

        layoutBottom = QHBoxLayout()
        layoutBottom.addStretch()
        layoutBottom.addWidget(bAccept)
        layoutBottom.addWidget(bCancel)

        layout.addLayout(layoutPath)
        layout.addStretch()
        layout.addLayout(layoutBottom)

    def selectPath(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select directory')
        self.entryPath.setText(folder)

    def acceptModifications(self):
        folder = self.entryPath.text()
        print(folder)
        self.close()

    def cancelModifications(self):
        self.close()
