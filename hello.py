#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a correspondnete.
Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI argument "--lang"

Ou o usuário terá que digitar.

Execucação:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Hugo Carvalho"
__license__ = "unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value




# Script hello World 
# - comentário de linha
#snake case = snake_case
#Pascal Case = PascalCase
current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
         current_language = os.getenv("LANG")
    else:
        current_language = input("Choose your language:")

current_language = current_language[:5]
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}


print(msg[current_language] * int(arguments["count"]))
