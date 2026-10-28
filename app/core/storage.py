#Hanaa Aquil
#2304518
#hanaaaquil-glitch
import json
class Storage:
    def __init__(self,fichier="vault.json"):
        self.fichier = fichier

    def charger(self):
        try:
            with open(self.fichier, "r",encoding="utf-8") as fichier:
                loaded_data =json.load(fichier)  # loaded_data =json.load(fichier)


        except FileNotFoundError:
            return []


        if not isinstance(loaded_data, list):
            raise ValueError("le coffre doit avoir au moins une liste")

        for data in loaded_data:
            if not isinstance(data, dict):
                raise ValueError("Une entrée du coffre est invalide")
            if "email" not in data or "mot_de_passe" not in data:
                raise ValueError(
                    "une entrée doit contenir un e-mail et un mot de passe "
                                )
            if not isinstance(data["email"], str):
                raise ValueError("L'email doir etre du texte")

            if not isinstance(data["mot_de_passe"], str):
                raise ValueError("Le mot de passe doit etre du texte")
        return loaded_data

    def sauvegarder(self,entrees):
        with open(self.fichier, "w",encoding="utf-8") as fichier:
            json.dump(entrees, fichier, ensure_ascii=False, indent=4)