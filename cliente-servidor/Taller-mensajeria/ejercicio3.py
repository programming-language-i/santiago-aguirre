import json

mensaje = {
    "emisor": "Juan",
    "contenido": "Hola clase",
    "etiquetas":("a", "b")
}


texto = json.dumps(mensaje, ensure_ascii=False)

copia = json.loads(texto)
print(f"Texto cargado: {copia}")

print("\n")

print(f"Son iguales: {mensaje==copia}")