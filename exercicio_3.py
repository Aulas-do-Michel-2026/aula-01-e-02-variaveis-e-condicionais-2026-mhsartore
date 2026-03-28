"""
#### Exercício 3

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

try:

    num = int(input("Insira um número inteiro:"))

    if num % 2 == 0:
        print(f"O número {num} é um número par.")
    else:
        print(f"O número {num} é um número impar.")

except ValueError:
    print("O número inserido não é um número inteiro.")
