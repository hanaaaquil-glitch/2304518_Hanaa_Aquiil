#Hanaa Aquil
#2304518
#hanaaaquil-glitch
import string
from random import randint


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

    def generate_password(self):
        self.verifier_options()
        types = []
        if self.miniscule :
            types.append("abcdefghijklmnopqrstuvwxyz")
        if self.majuscule :
            types.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if self.chiffre :
            types.append("0123456789")
        if self.symboles :
            types.append("!@#$%&*?")
        if self.validate and self.longueur < len(types):
            raise ValueError (
                "la longueur est trop petite pour les types sélectionnés"
            )
        caracteres = "".join(types)
        valide = False

        while not valide:
            lettres = []
            for i in range(self.longueur):
                indice = randint(0,len(caracteres)-1)
                lettres.append(caracteres[indice])
            mot_de_passe = "".join(lettres)
            valide = True

            if self.validate:
                for type in types :
                    present = False

                    for caractere in mot_de_passe:
                        if caractere in type :
                            present = True
                    if not present:
                        valide = False
            return mot_de_passe


