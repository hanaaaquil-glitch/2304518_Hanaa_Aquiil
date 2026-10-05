#AQUIL HANAA
#2304518
#hanaaaquil-glitch
import argparse

from app.core import generator

parser = argparse.ArgumentParser()

parser.add_argument("--length",type=int,default=16)
parser.add_argument("--no-lower", action="store_true")
parser.add_argument("--no-upper", action="store_true")
parser.add_argument("--no-digits", action="store_true")
parser.add_argument("--no-symbols", action="store_true")
parser.add_argument("--validate", action="store_true")

args = parser.parse_args()

try:
    generateur = generator.PasswordGenerator(
        args.length,
        not args.no_lower,
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
        args.validate
    )
    print(generateur.generate_password())
except ValueError as erreur :
    print(erreur)