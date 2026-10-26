from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QCheckBox,
    QSlider, QHBoxLayout,
)
from PySide6.QtCore import Qt
from app.core.generator import PasswordGenerator


class GenerateurFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generateur de mot de passe")
        self.longueur = 16
        self.label_longueur = QLabel(
            f"Longueur : {self.longueur}"
        )
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1,64)
        self.slider.setValue(self.longueur)
        self.slider.valueChanged.connect(
            self.changer_longueur
        )
        bouton_moins = QPushButton("-")
        bouton_plus = QPushButton("+")

        bouton_moins.clicked.connect(self.diminuer_longueur)
        bouton_plus.clicked.connect(self.augmenter_longueur)

        self.ligne_longueur = QHBoxLayout()
        self.ligne_longueur.addWidget(bouton_moins)
        self.ligne_longueur.addWidget(self.slider)
        self.ligne_longueur.addWidget(bouton_plus)




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

        layout.addWidget(self.label_longueur)
        layout.addLayout(self.ligne_longueur)

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
            self.longueur,
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

    def changer_longueur(self, valeur):
        self.longueur = valeur

        self.label_longueur.setText(
            f"Longueur : {self.longueur}"
        )

    def diminuer_longueur(self):
        if self.longueur > 1:
            self.slider.setValue(self.longueur - 1)

    def augmenter_longueur(self):
        if self.longueur < 64:
            self.slider.setValue(self.longueur + 1)

