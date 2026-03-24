"""Exercício 04: Classificador de Dia da Semana
================================================
Leia um inteiro de 1 a 7 (1 = Segunda-feira, 7 = Domingo).
Exiba o nome do dia e, na linha seguinte, o tipo.

ENTRADA:
  Um inteiro de 1 a 7 (ou outro valor para caso inválido).

SAÍDA:
  Linha 1: nome do dia (ex.: "Quarta-feira")
  Linha 2: tipo ("Dia util" ou "Fim de semana")
  Se o número for inválido: "Dia invalido"

MAPEAMENTO:
  1 → Segunda-feira  / Dia util
  2 → Terca-feira    / Dia util
  3 → Quarta-feira   / Dia util
  4 → Quinta-feira   / Dia util
  5 → Sexta-feira    / Dia util
  6 → Sabado         / Fim de semana
  7 → Domingo        / Fim de semana

EXEMPLOS:
  Entrada: 3  →  Quarta-feira / Dia util
  Entrada: 7  →  Domingo / Fim de semana
  Entrada: 9  →  Dia invalido

CONTEÚDO: match / case
"""

# TODO: leia o número com int(input())
# TODO: use match/case para tratar cada caso
# TODO: use case _ para o caso inválido
