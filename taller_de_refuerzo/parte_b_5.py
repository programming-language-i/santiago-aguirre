""" El problema es que cada proceso entrega resultados independientes
por eso lal ista siempre estara vacia.
""" 

import multiprocessing

resultados = []


def calcular(n):
    resultados.append(n * n)


if __name__ == "__main__":
    procesos = [multiprocessing.Process(target=calcular, args=(n,)) for n in range(4)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    print(resultados)