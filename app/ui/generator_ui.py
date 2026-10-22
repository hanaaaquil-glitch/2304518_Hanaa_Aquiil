from PySide6.QtWidgets import (
QWidget,
QVBoxLayout,
QLabel,
QPushButton,
QCheckBox,
)
from app.core.generator import PasswordGenerator

class GenerateurFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generateur de mot de passe")
        self.resize(450,400)
        self.init_ui()
