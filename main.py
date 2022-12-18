import numpy
import random

# Dimensões do plano
WIDTH = 60
HEIGTH = 20

drunk = {
        'wallcount': random.randint(100, 500), # numero de lacunas
        'padding': 2,
        'x': random.randint(1, WIDTH-1),
        'y': random.randint(1, HEIGTH-1)
}

# Função de criação de linhas
def getLevelRow():
    return ['#'] * WIDTH

# Definição da matriz 
level = [getLevelRow() for _ in range(HEIGTH)]

# Estrutura de geração procedural
while drunk['wallcount'] >= 0:
    x = drunk['x']
    y = drunk['y']

    if level[y][x] == '#':
        level[y][x] = ' '
        drunk['wallcount'] -= 1

    roll = random.randint(1, 4) # carga aleatória

    # Movimentação do obj para uma direção aleatória
    if roll == 1 and x > drunk['padding']:
        drunk['x'] -= 1
    if roll == 2 and x < WIDTH - 1 - drunk['padding']:
        drunk['x'] += 1
    if roll == 3 and y > drunk['padding']:
        drunk['y'] -= 1
    if roll == 4 and y < HEIGTH - 1 - drunk['padding']:
        drunk['y'] += 1

for row in level:
    print(''.join(row))
