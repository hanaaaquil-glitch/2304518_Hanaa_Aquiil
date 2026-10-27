# AQUIL HANAA
# 2304518
# hanaaaquil-glitch

import argparse
import sys

from app.core.generator import PasswordGenerator

parser = argparse.ArgumentParser()

parser.add_argument("--no-gui", action="store_true")
parser.add_argument("--vault_file", default="vault.json")

parser.add_argument("--length", type=int, default=16)
parser.add_argument("--no-lower", action="store_true")
parser.add_argument("--no-upper", action="store_true")
parser.add_argument("--no-digits", action="store_true")
parser.add_argument("--no-symbols", action="store_true")
parser.add_argument("--validate", action="store_true")

args = parser.parse_args()

if args.no_gui:
    try:
        generateur = PasswordGenerator(
            args.length,
            not args.no_lower,
            not args.no_upper,
            not args.no_digits,
            not args.no_symbols,
            args.validate,
        )

        print(generateur.generate_password())

    except ValueError as erreur:
        print(f"Erreur : {erreur}")
        sys.exit()

else:
    from PySide6.QtWidgets import QApplication
    from app.ui.main_window import CoffreFenetre

    app = QApplication(sys.argv) #je dois peut etre enlever la liste

    fenetre = CoffreFenetre(args.vault_file)
    fenetre.show()

    sys.exit(app.exec())