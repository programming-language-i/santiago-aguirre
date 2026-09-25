""" Utlizamos el pool de hilos para que se ejecuten de manera concurrente 
y no se bloquee el hilo principal.
"""

from concurrent.futures import ThreadPoolExecutor


def dividir(a, b):
    return a / b


with ThreadPoolExecutor() as pool:
    futuro = pool.submit(dividir, 1, 0)
print("listo")
