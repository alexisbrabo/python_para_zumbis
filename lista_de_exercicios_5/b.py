"""
Quantas vezes o trecho de pseudocódigo imprime oi
"""

oi_quantidade = 0

for i in range(0, 9):
    if i != 3:
        for j in range(0, 6):
            print("oi")
            oi_quantidade += 1

print(oi_quantidade)
