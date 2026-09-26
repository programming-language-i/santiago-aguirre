""" El codigo falla abrutamente o se bloquea
Falta la proteccion el bloque if __name__ == "__main__"
Faltaria agregar el bloque if __name__ == "__main__" para proteger la ejecucion del codigo.
"""

from concurrent.futures import ProcessPoolExecutor


def cuadrado(n):
    return n * n


with ProcessPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(cuadrado, range(4))))