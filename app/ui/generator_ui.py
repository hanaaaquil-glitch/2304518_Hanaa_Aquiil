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

    def init_ui(self):
        layout = QVBoxLayout()
        self.titre = QLabel("Générateur de mots de passe")
        self.miniscule = QCheckBox("Miniscule")
        self.majuscule = QCheckBox("Majuscule")
        self.chiffre = QCheckBox("Chiffre")
        self.symboles = QCheckBox("Symbole")
        self.validation = QCheckBox("Veuillez choisir au moins un caractere de chaque type choisi")

        self.resultat = QLabel("Sélectionne les types de caracteres")
        self.bouton_generer = QPushButton("generer")
        self.bouton_generer.clicked.connect(self.generer)

        layout.addWidget(self.titre)
        layout.addWidget(self.miniscule)
        layout.addWidget(self.majuscule)
        layout.addWidget(self.chiffre)
        layout.addWidget(self.symboles)
        layout.addWidget(self.validation)
        layout.addWidget(self.resultat)
        layout.addWidget(self.bouton_generer)
        self.setLayout(layout)

    def generer(self):
        generateur = PasswordGenerator(
            16,
            self.miniscule.isChecked(),
            self.majuscule.isChecked(),
            self.chiffre.isChecked(),
            self.symboles.isChecked(),
            self.validation.isChecked(),

        )
        try:
            mot_de_passe = generateur.generate_password()
            self.resultat.setText(mot_de_passe)
        except ValueError as erreur :
            self.resultat.setText(str(erreur))