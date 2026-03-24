"""Exercício 11: Cifra de César
================================
Implemente a cifra de substituição histórica de Júlio César.
Cada letra maiúscula é deslocada k posições no alfabeto (circularmente).
Caracteres não-letra são mantidos sem alteração.

ENTRADA:
  Linha 1: mensagem em letras MAIÚSCULAS (pode conter espaços e números).
  Linha 2: deslocamento k (inteiro de 1 a 25).

SAÍDA:
  A mensagem cifrada (apenas o texto resultante).

FÓRMULA para cada letra maiúscula:
  letra_cifrada = chr((ord(letra) - ord('A') + k) % 26 + ord('A'))

EXEMPLOS:
  Entrada: PYTHON / 3         →  SBWKRQ
  Entrada: ALGORITMO / 1      →  BMHPSJUNP
  Entrada: ATAQUE AO AMANHECER / 13  →  NGNDHR NB NZNAULPRE

VERIFICAÇÃO MANUAL (PYTHON, k=3):
  P(15)+3=18 → S
  Y(24)+3=27 → 27%26=1 → B
  T(19)+3=22 → W
  H(7)+3=10  → K
  O(14)+3=17 → R
  N(13)+3=16 → Q
  Resultado: SBWKRQ

CONTEÚDO: for sobre strings, ord(), chr(), operador %, funções
"""


def cifrar_cesar(mensagem, deslocamento):
    """Cifra a mensagem usando a Cifra de César com o deslocamento dado.

    Apenas letras maiúsculas são cifradas. Outros caracteres passam
    sem alteração.

    Retorna a string cifrada.
    """
    resultado = ""
    # TODO: percorra cada caractere da mensagem com for
    # TODO: se o caractere for maiúsculo (use .isupper()):
    #         aplique a fórmula: chr((ord(c) - ord('A') + deslocamento) % 26 + ord('A'))
    # TODO: caso contrário, mantenha o caractere original
    # TODO: concatene em resultado e retorne
    pass


# --- programa principal ---
# TODO: leia a mensagem com input()
# TODO: leia o deslocamento com int(input())
# TODO: chame cifrar_cesar e exiba o resultado
