"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""

peso_kg = int(input("Insira seu peso (kg):"))
dose_medicamento_mg = peso_kg * 2

print(f"A dose de medicamento indicada para {peso_kg}kg é de {dose_medicamento_mg}mg.")
