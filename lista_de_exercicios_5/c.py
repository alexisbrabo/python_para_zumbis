"""
Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis
por 7?
"""

count = 0

for i in range(1067, 3628):
    if not i % 2 and not i % 7:
        count += 1

print(count)
