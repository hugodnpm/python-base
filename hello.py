#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a correspondnete.
Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execucação:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Hugo Carvalho"
__license__ = "unlicense"

import os


# Script hello World 
# - comentário de linha
#snake case = snake_case
#Pascal Case = PascalCase
current_language = os.getenv("LANG","en_US")[:5] 
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mongo!"

print(msg)
