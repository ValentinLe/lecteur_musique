
from os.path import expanduser
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QDesktopWidget, QFileDialog, QLabel
from util.Config import Config


class ConfigWindow(QWidget):
    '''
    fenetre de configuration du lecteur

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    '''

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

        # zone pour changer le dossier contenant les musiques
        labPath = QLabel("Chemin des musiques :")
        self.entryPath = QLineEdit()
        path = self.config.getValueOf("path")
        if path:
            self.entryPath.setText(path)
        bBrowsePath = QPushButton("Parcourir...")
        bBrowsePath.clicked.connect(self.selectPath)

        # zone en bas a droite pour valider ou non les changements
        bAccept = QPushButton("Valider")
        bAccept.setProperty("class", "specialButton")
        bAccept.clicked.connect(self.acceptModifications)
        bCancel = QPushButton("Annuler")
        bCancel.setProperty("class", "specialButton")
        bCancel.clicked.connect(self.cancelModifications)

        # disposition de la fenetre

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
        ''' demande a l'utilisateur de choisir un dossier et rentre le chemin dans l'input '''
        folder = QFileDialog.getExistingDirectory(
            self, 'Select directory', expanduser("~"))
        if folder:
            self.entryPath.setText(folder)

    def acceptModifications(self):
        ''' met en place les parametres et ferme la fenetre '''
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
