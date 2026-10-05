#Hanaa Aquil
#2304518
#hanaaaquil-glitch
import string


class PasswordGenerator:
    def __init__(self, longueur , miniscule , majuscule , chiffre , symboles , validate):
        self.longueur = longueur
        self.miniscule = miniscule
        self.majuscule = majuscule
        self.chiffre = chiffre
        self.symboles = symboles
        self.validate = validate

    def verifier_options(self):
        if self.longueur <= 0 :
            raise ValueError (
                "La longueur doit etre superieur a 0"
            )
        if not (
            self.miniscule or self.majuscule or self.chiffre or self.symboles
        ):
            raise ValueError (
                "Il faut sélectionner au moins un type de caratere "
            )

