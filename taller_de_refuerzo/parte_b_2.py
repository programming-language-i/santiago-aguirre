""" Como el hilo secundario esta utilizando daemon, no espera a que se ejecute
y hace que se cierre abrutamente al terminar el hilo principal.
"""

import threading
import time


def guardar():
    try:
        time.sleep(2)
        print("guardado")
    finally:
        print("archivo cerrado")


threading.Thread(target=guardar, daemon=True).start()
time.sleep(0.5)
print("fin")

