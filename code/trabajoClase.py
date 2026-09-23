import threading
import time
from tabulate import tabulate


def sensor (numero, temperatura):
    print(f"{numero} sensor")
    
    for i in range(5):
        print(tabulate([[f"{numero} - {i+1} temperatura {temperatura} centigrados"]]))
        time.sleep(1)
        
        print("termino sensor")

if __name__ == "__main__":
    # SE CREAN LOS HILOS______________________________________________________
    threads = [ 
            threading.Thread(target=sensor, args=(1, 90)),
            threading.Thread(target=sensor, args=(2, 80)),
            threading.Thread(target=sensor, args=(3, 70)),
            threading.Thread(target=sensor, args=(4, 60)),
            threading.Thread(target=sensor, args=(5, 50)),
            ]

    
    # SE INICIAN LOS HILOS______________________________________________________
    for thread in threads:
        thread.start()
    
    # SE ESPERA A QUE TERMINEN LOS HILOS______________________________________________________
    for thread in threads:
        thread.join()

    print("Finalizaron todos los hilos")
    











