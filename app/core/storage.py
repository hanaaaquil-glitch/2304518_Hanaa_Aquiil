import json
class Storage:
    def __init__(self,fichier="vault.json"):
        self.fichier = fichier

    def charger(self):
        try:
            with open(self.fichier, "r",encoding="utf-8") as fichier:
                entrees =json.load(fichier)

        except FileNotFoundError:
            return []

        if not isinstance(entrees, list):
            raise ValueError("le coffre doit avoir au moins une liste")
        for entree in entrees:
            if not isinstance(entree, dict):
                raise ValueError("Une entrée du coffre est invalide")
            if "email" not in entree or "mot_de_passe" not in entree:
                raise ValueError(
                    "une entrée doit contenir un e-mail et un mot de passe "
                                )
            if not isinstance(entree["email"], str):
                raise ValueError("L'email doir etre du texte")
            if not isinstance(entree["mot_de_passe"], str):
                raise ValueError("Le mot de passe doit etre du texte")
            return entrees

    def sauvegarder(self,entrees):
        with open(self.fichier, "w",encoding="utf-8") as fichier:
            json.dump(entrees, fichier, ensure_ascii=False, indent=4)