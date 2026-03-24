"""Exercício 01: Verificador de Ano Bissexto
============================================
Um ano é bissexto se for divisível por 400, OU se for divisível
por 4 mas NÃO por 100.

Regra simplificada:
  bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ENTRADA:
  Uma linha com um inteiro representando o ano.

SAÍDA:
  "Bissexto"      →  ano bissexto
  "Nao bissexto"  →  ano não bissexto

EXEMPLOS:
  Entrada: 2024  →  Saída: Bissexto     (divisível por 4, não por 100)
  Entrada: 1900  →  Saída: Nao bissexto (divisível por 100, não por 400)
  Entrada: 2000  →  Saída: Bissexto     (divisível por 400)
  Entrada: 2023  →  Saída: Nao bissexto

CONTEÚDO: if / else, operadores and / or / not
"""

# TODO: leia o ano com int(input())
# TODO: use a condição composta: (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
# TODO: exiba "Bissexto" ou "Nao bissexto" com print()
