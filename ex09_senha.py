"""Exercício 09: Analisador de Força de Senha
==============================================
Avalie a força de uma senha com base em 6 critérios de segurança.

ENTRADA:
  Uma linha com a senha (string, sem espaços).

SAÍDA:
  Exatamente uma das strings abaixo (a classificação):
  "Muito Fraca"  →  pontuação 0 ou 1
  "Fraca"        →  pontuação 2 ou 3
  "Media"        →  pontuação 4
  "Forte"        →  pontuação 5
  "Muito Forte"  →  pontuação 6

CRITÉRIOS DE PONTUAÇÃO (+1 ponto cada):
  1. len(senha) >= 6
  2. len(senha) >= 10
  3. Contém ao menos uma letra maiúscula (A-Z)
  4. Contém ao menos uma letra minúscula (a-z)
  5. Contém ao menos um dígito (0-9)
  6. Contém ao menos um caractere especial em: !@#$%^&*()-_=+[]{}

EXEMPLOS:
  Entrada: abc        →  pontuação: 1  →  Muito Fraca
  Entrada: Senha1     →  pontuação: 4  →  Media
  Entrada: Python@99! →  pontuação: 6  →  Muito Forte

DICA: use any(c.isupper() for c in senha) para verificar maiúsculas.

CONTEÚDO: for sobre strings, condicionais, funções, any()
"""

ESPECIAIS = "!@#$%^&*()-_=+[]{}"


def analisar_senha(senha):
    """Calcula a pontuação da senha e retorna a classificação de força."""
    pontuacao = 0

    # TODO: verifique cada um dos 6 critérios e some +1 por critério atendido
    # Dica: use any() para verificar presença de caracteres em categorias

    # TODO: retorne a classificação com base na pontuação:
    #   0-1 → "Muito Fraca"
    #   2-3 → "Fraca"
    #   4   → "Media"
    #   5   → "Forte"
    #   6   → "Muito Forte"
    pass


# --- programa principal ---
# TODO: leia a senha com input()
# TODO: chame analisar_senha e exiba o resultado
