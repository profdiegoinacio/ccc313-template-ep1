"""Exercício 12: Oráculo Binário
==================================
O computador usa busca binária para adivinhar um número secreto
entre 1 e 127. Você implementa o algoritmo.

A busca binária garante encontrar qualquer número em no máximo
log2(127) ≈ 7 tentativas — enquanto uma busca linear precisaria
de até 127.

ENTRADA:
  Um inteiro entre 1 e 127 (o número secreto).

SAÍDA:
  Uma linha por tentativa no formato:
    "Tentativa X: chuto Y... Muito baixo!"
    "Tentativa X: chuto Y... Muito alto!"
    "Tentativa X: chuto Y... Encontrei em X tentativa(s)!"

EXEMPLOS:
  Entrada: 64
    Tentativa 1: chuto 64... Encontrei em 1 tentativa(s)!

  Entrada: 100
    Tentativa 1: chuto 64... Muito baixo!
    Tentativa 2: chuto 96... Muito baixo!
    Tentativa 3: chuto 112... Muito alto!
    Tentativa 4: chuto 104... Muito alto!
    Tentativa 5: chuto 100... Encontrei em 5 tentativa(s)!

ALGORITMO DA BUSCA BINÁRIA:
  1. baixo = 1, alto = 127, tentativas = 0
  2. Enquanto True:
       chute = (baixo + alto) // 2
       tentativas += 1
       Se chute == numero_secreto: exiba acerto e pare
       Se chute < numero_secreto:  exiba "Muito baixo!", baixo = chute + 1
       Se chute > numero_secreto:  exiba "Muito alto!",  alto  = chute - 1

REFLEXÃO: qual número entre 1 e 127 exige mais tentativas?

CONTEÚDO: while, funções, if/elif/else, lógica de busca binária
"""


def busca_binaria(numero_secreto):
    """Usa busca binária para adivinhar numero_secreto no intervalo [1, 127].

    Exibe cada tentativa e o resultado.
    """
    baixo = 1
    alto = 127
    tentativas = 0

    # TODO: implemente o laço while True (ou while baixo <= alto)
    # TODO: calcule chute = (baixo + alto) // 2
    # TODO: incremente tentativas
    # TODO: compare chute com numero_secreto e:
    #         - se igual: exiba acerto e use break
    #         - se menor: exiba "Muito baixo!" e ajuste baixo
    #         - se maior: exiba "Muito alto!" e ajuste alto
    # TODO: use plural correto: "1 tentativa" vs "N tentativas"
    pass


# --- programa principal ---
# TODO: leia o número secreto com int(input())
# TODO: chame busca_binaria(numero_secreto)
