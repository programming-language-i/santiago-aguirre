import pickle


mensaje = {
    "emisor": "Juan",
    "contenido": "Hola clase",
    "etiquetas":("a", "b")
}

datos = pickle.dumps(mensaje)


copia = pickle.loads(datos)
print(copia)