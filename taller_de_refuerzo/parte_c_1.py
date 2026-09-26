"""El codigo falla inmediatamente 
Por que no se llama al constructor super de la clase padre y no se inicializa el hilo
Se debe agregar el constructor super
"""

import threading


class Descarga(threading.Thread):
    def __init__(self, archivo):
        self.archivo = archivo

    def run(self):
        print("descargando", self.archivo)


Descarga("a.zip").start()


