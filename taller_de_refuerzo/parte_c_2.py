"""Al ejecutarlo se desarrolla de forma secuencial tarda 3.179 segundos
Por que la poner start en ves de run se destruye la clase padre y no se llama el constructor super
Se debe cambiar el metodo start por run y agregar el constructor super
"""

import threading
import time


class Tarea(threading.Thread):
    def start(self):
        time.sleep(1)
        print(self.name, "lista")


inicio = time.perf_counter()
tareas = [Tarea(name=f"t{i}") for i in range(3)]
for t in tareas:
    t.start()
print(f"{time.perf_counter() - inicio:.1f} s")
for t in tareas:
    t.join()