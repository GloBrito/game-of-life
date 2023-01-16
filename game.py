import time
import os

def tabuleiro():
    return [
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0,0, 0, 0, 0, 0, 0, 0, 0,],
    ]

os.system("clear")

def desenha(m):
    formas = {0:0, 1:1}
    for i in range(len(m)):
        print(''.join([formas[e]for e in m[i]]))

def conta_vizinhos_vivos(m, i, y):
    return 0 

def atualiza(m):
    nm= [(0 for e in linha) for linha in m]
    for i in range(len(m)):
        for y in range(len(m[i])):
            conta_vizinhos_vivos = conta_vizinhos_vivos(m, i, y)
            if m[i][y] == i:
                if conta_vizinhos_vivos in {0, 1}:
                    nm[i][y] = 0
                elif conta_vizinhos_vivos >= 4:
                    nm[i][y] = 0
                else:
                    nm[i][y] = 1
            else:
                if conta_vizinhos_vivos == 3:
                    nm[i][y] = 1
                else:
                    nm[i][y] = 0
    return nm

def pausa():
    time.sleep(i)

m = tabuleiro()

while True:
    os.system("clear")
    desenha(m)
    pausa()
    m = atualiza(m)

