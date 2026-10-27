# Hanaa Aquil
# 2304518
# hanaaaquil-glitch

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QDialog,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
)

from app.core.storage import Storage
from app.core.generator import PasswordGenerator
from app.ui.generator_ui import GenerateurFenetre
from PySide6.QtCore import Signal

class EntreeWidget(QWidget):
    modifie_demande = Signal(object)
    supprime_demande = Signal(object)
    def __init__(self,entree):
        super().__init__()
        self.entree = entree
        layout = QHBoxLayout()
        label = QLabel(self.entree["email"]+"- *******")
        bouton_modifier = QPushButton("Modifier")
        bouton_supprimer = QPushButton("Supprimer")

        bouton_modifier.clicked.connect(self.demander_modification)
        bouton_supprimer.clicked.connect(self.demander_suppression)
        layout.addWidget(label)
        layout.addWidget(bouton_modifier)
        layout.addWidget(bouton_supprimer)

        self.setLayout(layout)
    def demander_modification(self):
        self.modifie_demande.emit(self.entree) # pour émettre le signal
    def demander_suppression(self):
        self.supprime_demande.emit(self.entree)





class CoffreFenetre(QMainWindow):
    def __init__(self, fichier="vault.json"):
        super().__init__()

        self.setWindowTitle("Mon coffre-fort")
        self.resize(600, 450)

        self.storage = Storage(fichier)
        self.entrees = []
        self.entree_modifiee = None
        self.chargement_reussi = False
        self.erreur_chargement = ""

        try:
            self.entrees = self.storage.charger()
            self.chargement_reussi = True

        except ValueError as erreur:
            self.erreur_chargement = (
                f"Les données sont invalides : {erreur}"
            )

        except Exception as erreur:
            self.erreur_chargement = (
                f"Impossible de lire le fichier : {erreur}"
            )

        self.init_ui()

    def init_ui(self):
        contenu = QWidget()
        layout = QVBoxLayout(contenu)

        titre = QLabel("Mon coffre-fort")
        layout.addWidget(titre)

        self.message = QLabel(self.erreur_chargement)
        layout.addWidget(self.message)

        self.bouton_ajouter = QPushButton("Ajouter")
        self.bouton_ajouter.clicked.connect(self.ouvrir_ajout)
        self.bouton_ajouter.setEnabled(self.chargement_reussi)
        layout.addWidget(self.bouton_ajouter)


        bouton_generateur = QPushButton(
            "Ouvrir le générateur"
        )

        bouton_generateur.clicked.connect(
            self.ouvrir_generateur
        )

        layout.addWidget(bouton_generateur)
        bouton_trier = QPushButton("Trier par e-mail")
        bouton_trier.clicked.connect(self.trier_entrees)
        layout.addWidget(bouton_trier)

        self.zone = QScrollArea()
        self.zone.setWidgetResizable(True)
        layout.addWidget(self.zone)

        self.setCentralWidget(contenu)

        self.afficher_entrees()

    def afficher_entrees(self):
        liste = QWidget()
        layout_liste = QVBoxLayout(liste)

        if not self.entrees:
            layout_liste.addWidget(
                QLabel("Aucune entrée à afficher.")
            )

        for entree in self.entrees:
           ligne = EntreeWidget(entree)
           ligne.modifie_demande.connect(self.ouvrir_modification)
           ligne.supprime_demande.connect(self.supprimer_entree)
           layout_liste.addWidget(ligne)
        layout_liste.addStretch()
        self.zone.setWidget(liste)

    def ouvrir_ajout(self):
        self.entree_modifiee = None
        self.dialogue = QDialog(self)
        self.dialogue.setWindowTitle("Ajouter une entrée")

        layout = QVBoxLayout(self.dialogue)

        self.champ_email = QLineEdit()
        self.champ_mot_de_passe = QLineEdit()

        self.message_ajout = QLabel("")

        bouton_generer = QPushButton("Générer")
        bouton_generer.clicked.connect(self.generer_pour_entree)

        bouton_ajouter = QPushButton("Enregistrer")
        bouton_ajouter.clicked.connect(self.enregistrer_entree)

        layout.addWidget(QLabel("E-mail :"))
        layout.addWidget(self.champ_email)

        layout.addWidget(QLabel("Mot de passe :"))
        layout.addWidget(self.champ_mot_de_passe)

        layout.addWidget(bouton_generer)
        layout.addWidget(self.message_ajout)
        layout.addWidget(bouton_ajouter)

        self.dialogue.exec()

    def generer_pour_entree(self):
        generateur = PasswordGenerator(
            16,
            True,
            True,
            True,
            True,
            True,
        )

        try:
            mot_de_passe = generateur.generate_password()
            self.champ_mot_de_passe.setText(mot_de_passe)
            self.message_ajout.setText("")

        except ValueError as erreur:
            self.message_ajout.setText(str(erreur))

    def enregistrer_entree(self):
        email = self.champ_email.text().strip()
        mot_de_passe = self.champ_mot_de_passe.text()

        if email == "" or mot_de_passe == "":
            self.message_ajout.setText(
                "Remplis l'e-mail et le mot de passe."
            )
            return

        if self.entree_modifiee is None:
            entree = {
                "email": email,
                "mot_de_passe": mot_de_passe,
            }


            self.entrees.append(entree)

        else:
            self.entree_modifiee["email"] = email
            self.entree_modifiee["mot_de_passe"] = (mot_de_passe)
        self.dialogue.accept()
        self.afficher_entrees()

    def ouvrir_generateur(self):
        self.fenetre_generateur = GenerateurFenetre()
        self.fenetre_generateur.show()

    def trier_entrees(self):
        for i in range(len(self.entrees)):
            for j in range(i + 1, len(self.entrees)):
                email1 = self.entrees[i]["email"].lower()
                email2 = self.entrees[j]["email"].lower()

                if email1 > email2:
                    temporaire = self.entrees[i]
                    self.entrees[i] = self.entrees[j]
                    self.entrees[j] = temporaire

        self.afficher_entrees()

    def ouvrir_modification(self, entree):
        self.entree_modifiee = entree
        self.dialogue = QDialog(self)
        self.dialogue.setWindowTitle("Modifier une entrée")

        layout = QVBoxLayout(self.dialogue)

        self.champ_email = QLineEdit()
        self.champ_email.setText(entree["email"])

        self.champ_mot_de_passe = QLineEdit()
        self.champ_mot_de_passe.setText(entree["mot_de_passe"])
        self.message_ajout = QLabel("")
        bouton_generer = QPushButton("Générer")

        bouton_generer.clicked.connect(self.generer_pour_entree)
        bouton_enregistrer = QPushButton("Enregistrer")
        bouton_enregistrer.clicked.connect(self.enregistrer_entree )

        layout.addWidget(QLabel("E-mail :"))
        layout.addWidget(self.champ_email)
        layout.addWidget(QLabel("Mot de passe :"))
        layout.addWidget(self.champ_mot_de_passe)

        layout.addWidget(bouton_generer)
        layout.addWidget(self.message_ajout)
        layout.addWidget(bouton_enregistrer)

        self.dialogue.exec()

    def supprimer_entree(self, entree):
        reponse = QMessageBox.question(
            self,
            "Supprimer une entrée",
            "Veux-tu supprimer cette entrée ?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reponse == QMessageBox.StandardButton.Yes:
           nouvelles_entrees = []
           entree_retiree = False

           for element in self.entrees:
               if element == entree and not entree_retiree:
                   entree_retiree = True
               else:
                   nouvelles_entrees.append(element)
           self.entrees = nouvelles_entrees
           self.afficher_entrees()


    def closeEvent(self, event):
        if self.chargement_reussi:
            try:
                self.storage.sauvegarder(self.entrees)

            except Exception as erreur:
                self.message.setText(
                    f"Impossible de sauvegarder : {erreur}"
                )
                event.ignore()
                return

        event.accept()