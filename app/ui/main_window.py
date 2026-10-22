import argparse
import sys

from app.core import generator
from main import parser

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
    generator=generator.PasswordGenerator(
        args.length,
        not args.no_lower,
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
        args.validate
    )
    try:
        print(generator.generate_password())
    except ValueError as erreur :
        print(f"Erreur : {erreur}")
        sys.exit(1)
else:
    from PySide6.QtWidgets import QApplication
    from app.ui.generator_ui import GenerateurFenetre
    app = QApplication(sys.argv)
    fenetre = GenerateurFenetre()
    fenetre.show()
    sys.exit(app.exec_())
