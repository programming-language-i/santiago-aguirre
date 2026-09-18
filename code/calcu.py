def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def multiplicacion(valor1, valor2):
    return valor1 * valor2

op = input("Ingrese la operacion a realizar (suma, resta, multiplicacion): ")

if op == "suma":
    print(suma(5,3))
elif op == "resta":
    print(resta(5,3))
elif op == "multiplicacion":
    print(multiplicacion(5,3))
else:
    print("Operacion no valida")