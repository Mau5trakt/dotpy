print("Bienvenido al sistema usted ha ingresado como usuario")
elec = ""
while elec not in ["Q", "1", "2"]:
    elec= input("Ingrese: \n -1 para entrar a la busqueda de libros \n -2 para ver sus libros que ha prestado \n -Q para salir del sistema: \n ")
if elec == "1":
    print("ayeye chiquito") #Aqui conecto la db de mongo y muestro los libros 
elif elec == "2":
    print("ayeye grande ") #Aquí según el id del usuario muestro los libros que ha prestado haciendo un artilugio con MongoDB y viendo a ver que onda como le hago con los días xDDD ta heavy 
elif elec == "Q": 
    print("Usted ha salido exitosamente")