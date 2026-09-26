# Se esta ejecutando dos veces el mismo hilo 

import threading

hilo = threading.Thread(target=print, args=("hola",))
hilo.start()
hilo.join()
print(hilo.is_alive())
hilo.start()