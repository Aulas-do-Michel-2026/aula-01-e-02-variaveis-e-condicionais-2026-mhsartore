"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

nota_1 = float(input("Insira a primeira nota:"))
nota_2 = float(input("Insira a segunda nota:"))
nota_3 = float(input("Insira a terceira nota:"))

media_notas = round(((nota_1 + nota_2 + nota_3)/3), 2)

print(f"A média aritmética das notas {nota_1}, {nota_2}, {nota_3} é {media_notas}")
