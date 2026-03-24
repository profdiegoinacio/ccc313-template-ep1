"""Exercício 10: Gerador de Números Primos
==========================================
Use math.sqrt para implementar um verificador eficiente de primos
e liste todos os primos até o limite informado.

ENTRADA:
  Um inteiro n (limite superior, inclusive).

SAÍDA:
  Cada primo encontrado em uma linha separada.
  Última linha: "Total: X primos"

EXEMPLOS:
  Entrada: 10  →  2 / 3 / 5 / 7 / Total: 4 primos
  Entrada: 20  →  2/3/5/7/11/13/17/19 / Total: 8 primos

POR QUÊ math.sqrt? Para verificar se n é primo, basta testar
divisores até sqrt(n): reduz complexidade de O(n) para O(√n).

CONTEÚDO: for, math.sqrt, int(), funções booleanas, break
"""

import math


def eh_primo(n):
    """Retorna True se n for primo, False caso contrário.

    Algoritmo:
      - n < 2 nunca é primo
      - Teste divisores de 2 até int(math.sqrt(n)) + 1
      - Se algum divide n sem resto → False
      - Se nenhum divide → True
    """
    # TODO: trate o caso n < 2 (retorne False)
    # TODO: use for com range(2, int(math.sqrt(n)) + 1)
    # TODO: se n % divisor == 0, retorne False
    # TODO: ao final do loop, retorne True
    pass


# --- programa principal ---
# TODO: leia n com int(input())
# TODO: percorra de 2 a n com for, chamando eh_primo para cada número
# TODO: guarde e exiba os primos encontrados
# TODO: exiba f"Total: {total} primos" ao final
