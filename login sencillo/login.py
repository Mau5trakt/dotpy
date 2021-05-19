import random
print("Bienvenido al sistema, ingrese sus credenciales a continuación")
users = ["enal986"]
op = ""
while op not in ['R', 'I']:
    op = input('Registrarse o Iniciar sesion[R/I]: ')
    if op == 'R':
        confir = ""
        while confir not in ['S']:
            name = input("Ingrese su nombre: ")
            surname = input("Ingrese su apellido: ")
            num = input("Ingrese su número de telefono: ")
            confir = input(f"¿Su nombre es {name} {surname} y su número telefónico es {num}?[S/N]:")
            uname = ((name[0:2])+(surname[0:2])+str(random.randint(0, 999))).lower()
            while uname in users:
                uname =((name[0:2])+(surname[0:2])+str(random.randint(0, 999)))

            users.append(uname)
            print(f"sus datos de acesso son:\n Usuario:{uname}\n Contraseña: (aqui le voy a meter una contraseña cifrada)")
            

            '''
            Bueno aqui es donde conecto la db y le paso los valores que salen en confir
            '''
        num = int(num)    
        if num in users: 
            print("Usted ya se encuentra registrado en el sistema \n por favor inicie sesion")
        elif num not in users:
            print("Usted se ha registrado satisfactoriamente")
            users.append(num)
            #print(users)
    elif op == 'I':
        conf = ""
        while conf not in users:
            conf = int(input("Ingrese su número telefónico"))
            if conf in users:
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
            else: 
                print("id incorrecto o no existente en el sistema")
        

''''#aqui cargo la db y segun el numero obtengo el nombre
Bueno la verdad es que voy a hacerlo con el username y pass pero es de prueba para ver como funciona xD
Y ya después muestro el menu'''
