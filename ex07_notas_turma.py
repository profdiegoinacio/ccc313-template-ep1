"""Exercício 07: Processador de Notas da Turma
===============================================
Leia n notas, calcule a média e determine a situação do aluno.

ENTRADA:
  Linha 1: número de notas n (inteiro)
  Linhas 2 a n+1: uma nota por linha (float)

SAÍDA:
  "Media: X.XX"
  "Situacao: Aprovado"  ou  "Situacao: Reprovado"

CRITÉRIO: media >= 6.0 → Aprovado, caso contrário → Reprovado

EXEMPLOS:
  Entrada: 3 / 7.0 / 8.0 / 9.0  →  Media: 8.00 / Situacao: Aprovado
  Entrada: 2 / 4.0 / 5.0        →  Media: 4.50 / Situacao: Reprovado

CONTEÚDO: for, funções compostas, if/else
"""


def calcular_media(notas):
    """Recebe uma lista de floats e retorna a média aritmética."""
    # TODO: some todos os elementos da lista e divida pelo total
    pass


def classificar(media):
    """Retorna 'Aprovado' se media >= 6.0, 'Reprovado' caso contrário."""
    # TODO: use if/else
    pass


# --- programa principal ---
# TODO: leia n com int(input())
# TODO: leia n notas em um laço for e guarde em uma lista
# TODO: chame calcular_media e classificar
# TODO: exiba: f"Media: {media:.2f}"
# TODO: exiba: f"Situacao: {situacao}"
