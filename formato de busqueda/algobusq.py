# Tipo de busqueda afin en el que se introduce una palabra y si no encuentra nada le quita una letra y vuelve a buscar
objetos = ["camara", "camaron", "camarones", "camarero"]
# busqueda = input("ingrese lo que desea buscar: ".lower())
busqueda = "cama"
if busqueda in objetos:
    print("Encontdo")
else:
    palabras = []
    for i in range(1, len(busqueda) + 1):
        a = busqueda[0:i]
        palabras.append(a)

    palabras.sort(reverse=True)
    print(palabras)
