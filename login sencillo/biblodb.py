from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://usuarios:RgvAZFpFu9LYm5RF@cluster0.8oeno.mongodb.net/ex01?retryWrites=true&w=majority')
import random

db = client['ex01']
col = db['corprueb']
lib = db['libros']

print("Bienvenido al sistema, ingrese sus credenciales a continuación")
op = ""
while op not in ['R', 'I']:
    op = input("¿Registrarse o Iniciar sesión?[R/I]: ")
    if op == 'R':
        confir = ""
        while confir != 'S':
            name = input("Ingrese su nombre: ")
            surname = input("Ingrese su apellido: ")
            num = int(input("Ingrese su número de telefono: "))
            busn = col.find_one({'# telefónico': num})
            if busn is not None:
                print("Usted se encuentra registrado en el sistema, por favor inicie sesión")


            else:
                confir = input(f"Su nombre es {name}, su apellido es {surname} y su número de telefono es {num}?[S/N]")
                # Funcion que crea el nombre de usuario
                uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                bususer = col.find_one({'uname': uname})  # Buscar el nombre de usuario generado
                while bususer is not None:  # Si el nombre de usuario ya existe en el sistema se genera otro
                    uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                print(f"Su nombre de usario es: {uname}")

                col.insert_one({  # Insertar el nombre de usuario en la db
                    'Nombre': name,
                    'Apellido': surname,
                    '# telefónico': num,
                    'uname': uname})
                print("Registro correcto")
                confir = ""

    if op == 'I':
        init = ""
        while init != True:
            init = input("Ingrese su nombre de usuario: \n")
            c = init
            b = col.find_one({'uname': init}) # Buscar el nombre de usuario en la db
            if b is None:
                print("Usuario no encontrado")
            else:
                init = True
                print("Usted ha iniciado sesión correctamente")
                menu = ""
                while menu not in [1, 2, 3]:  # Opciones al ingresar
                    menu = int(input(" -1 Buscar libro \n -2 Ver mis libros prestados \n -3 Salir \n"))

                    if menu == 1:
                        otp = ""
                        while otp not in [1, 2, 3, 4, 5]:
                            otp = int(input("Ingrese el número según la búsqueda que desee hacer\n"
                                            "1- Busqueda por título de libro \n"
                                            "2- Busqueda por autor de libro \n"
                                            "3- Busqueda por categoría\n"
                                            "4- Busqueda por id:\n"
                                            "5- Salir \n"))

                            if otp == 1:
                                bsc = input("Ingrese el título del libro:")
                                for libro in lib.find({"título": bsc},
                                                      {"Autor": 1, "Categoría": 1, "Edicion": 1, "título": 1,
                                                       "registro": 1, "_id": 0}):  # Metodo de búsqueda
                                    a = libro
                                    print(a)
                                rw = ""
                                while rw not in [1, 2, 3]:
                                    rw = int(input("Ingrese: \n"
                                                   "-1  Hacer otra busqueda\n"
                                                   "-2  Prestar un libro\n"
                                                   "-3  Salir del sistema\n"))
                                    if rw == 1:
                                        otp = ""
                                    elif rw == 2:
                                        id = int(input("Ingrese el # de registro del libro que desea prestar: "))
                                        d = lib.find({"registro":id})
                                        if d is None:
                                            print("Libro no existente en el sistema")
                                            break

                                        else:
                                            for libro in lib.find({"registro": id}):

                                                a = libro
                                                if a['disponibles'] > 2:
                                                    libname = a['título']
                                                    lided = a['Edicion']
                                                    autor = a['Autor']
                                                    reg = a['registro']

                                                    print("Este libro se encuentra disponible para su préstamo") #Query de prestamo
                                                    prestar = input(f"¿desea prestar {libname}, {lided} edición, del autor {autor} y registro {reg}?[S/N]")
                                                    if prestar == 'S':
                                                        for user in col.find({'uname': c}):
                                                            z = user
                                                            if z['libros en prestamo'] <3:
                                                                # base de datos de los usuarios
                                                                col.update_one(
                                                                    {"uname": c} ,
                                                                    {"$inc":{
                                                                        "libros en prestamo":1,
                                                                        "libros prestados":1
                                                                    }}
                                                                ),
                                                                lib.update_one( #Base de datos de los libros
                                                                    {"registro":id},
                                                                    {"$inc":{
                                                                        "disponibles":-1,
                                                                        "en prestamo": 1,
                                                                        "veces prestado": 1

                                                                    }}
                                                                )
                                                                print("Libro prestado con éxito, su fecha de entrega es: (aqui para cualdo logre hacer lo de las fechas aaaaaaaaa)")





                                                            else:
                                                                print("Usted tiene en préstamo 3 libros, devuelva al menos 1 libro para hacer el nuevo préstamo.")

                                                    else:
                                                        rec = ""
                                                        while rec not in [1,2,3,4]:
                                                            rec =int(input("Ingrese:\n"
                                                                       "-1 para prestar otro libro\n"
                                                                       "-2 para hacer otra búsqueda\n"
                                                                       "-3 para regresar al menú principal\n"
                                                                       "-4 para salir:"))

                                                            if rec == 1:
                                                                rw = ""

                                                            elif rec == 2:
                                                                otp = ""

                                                            elif rec == 3:
                                                                menu = ""

                                                            elif rec == 4:
                                                                print("Usted ha salido del sistema")
                                                                break
                                                                #working on this part at @30/05/21 12: 33 i hope come back at 15:00h

                                                else:
                                                    print("Este libro no se encuentra disponible para su prestamo")


                                    elif rw == 3:
                                        break

                            elif otp == 2:
                                bsc = input("Ingrese el autor del libro:")
                                for libro in lib.find({"Autor": bsc},
                                                      {"Autor": 1, "Categoría": 1, "Edición": 1, "título": 1,
                                                       "registro": 1, "_id": 0}):
                                    a = libro
                                    print(a)
                                rw = ""
                                while rw not in [1, 2, 3]:
                                    rw = int(input("Ingrese: \n"
                                                   "-1  Hacer otra busqueda\n"
                                                   "-2  Prestar un libro\n"
                                                   "-3  Salir del sistema\n"))
                                    if rw == 1:
                                        otp = ""
                                    elif rw == 2:
                                        id = int(input("Ingrese el # de registro del libro que desea prestar: "))
                                        d = lib.find({"registro": id})
                                        if d is None:
                                            print("Libro no existente en el sistema")
                                            break

                                        else:
                                            for libro in lib.find({"registro": id}):

                                                a = libro
                                                if a['disponibles'] > 2:
                                                    libname = a['título']
                                                    lided = a['Edicion']
                                                    autor = a['Autor']
                                                    reg = a['registro']

                                                    print(
                                                        "Este libro se encuentra disponible para su préstamo")  # Query de prestamo
                                                    prestar = input(
                                                        f"¿desea prestar {libname}, {lided} edición, del autor {autor} y registro {reg}?[S/N]")
                                                    if prestar == 'S':
                                                        for user in col.find({'uname': c}):
                                                            z = user
                                                            if z['libros en prestamo'] < 3:
                                                                # base de datos de los usuarios
                                                                col.update_one(
                                                                    {"uname": c},
                                                                    {"$inc": {
                                                                        "libros en prestamo": 1,
                                                                        "libros prestados": 1
                                                                    }}
                                                                ),
                                                                lib.update_one(  # Base de datos de los libros
                                                                    {"registro": id},
                                                                    {"$inc": {
                                                                        "disponibles": -1,
                                                                        "en prestamo": 1,
                                                                        "veces prestado": 1

                                                                    }}
                                                                )
                                                                print(
                                                                    "Libro prestado con éxito, su fecha de entrega es: (aqui para cualdo logre hacer lo de las fechas aaaaaaaaa)")





                                                            else:
                                                                print(
                                                                    "Usted tiene en préstamo 3 libros, devuelva al menos 1 libro para hacer el nuevo préstamo.")

                                                    else:
                                                        rec = ""
                                                        while rec not in [1, 2, 3, 4]:
                                                            rec = int(input("Ingrese:\n"
                                                                            "-1 para prestar otro libro\n"
                                                                            "-2 para hacer otra búsqueda\n"
                                                                            "-3 para regresar al menú principal\n"
                                                                            "-4 para salir:"))

                                                            if rec == 1:
                                                                rw = ""

                                                            elif rec == 2:
                                                                otp = ""

                                                            elif rec == 3:
                                                                menu = ""

                                                            elif rec == 4:
                                                                print("Usted ha salido del sistema")
                                                                break
                                                                # working on this part at @30/05/21 12: 33 i hope come back at 15:00h

                                                else:
                                                    print("Este libro no se encuentra disponible para su prestamo")


                                    elif rw == 3:
                                        break

                            elif otp == 3:
                                bsc = input("Ingrese el la categoría del libro:")
                                for libro in lib.find({"Categoría": bsc},
                                                      {"Autor": 1, "Categoría": 1, "Edición": 1, "título": 1,
                                                       "registro": 1, "_id": 0}):
                                    a = libro
                                    print(a)
                                rw = ""
                                while rw not in [1, 2, 3]:
                                    rw = int(input("Ingrese: \n"
                                                   "-1  Hacer otra busqueda\n"
                                                   "-2  Prestar un libro\n"
                                                   "-3  Salir del sistema\n"))
                                    if rw == 1:
                                        otp = ""
                                    elif rw == 2:
                                        id = int(input("Ingrese el # de registro del libro que desea prestar: "))
                                        d = lib.find({"registro": id})
                                        if d is None:
                                            print("Libro no existente en el sistema")
                                            break

                                        else:
                                            for libro in lib.find({"registro": id}):

                                                a = libro
                                                if a['disponibles'] > 2:
                                                    libname = a['título']
                                                    lided = a['Edicion']
                                                    autor = a['Autor']
                                                    reg = a['registro']

                                                    print(
                                                        "Este libro se encuentra disponible para su préstamo")  # Query de prestamo
                                                    prestar = input(
                                                        f"¿desea prestar {libname}, {lided} edición, del autor {autor} y registro {reg}?[S/N]")
                                                    if prestar == 'S':
                                                        for user in col.find({'uname': c}):
                                                            z = user
                                                            if z['libros en prestamo'] < 3:
                                                                # base de datos de los usuarios
                                                                col.update_one(
                                                                    {"uname": c},
                                                                    {"$inc": {
                                                                        "libros en prestamo": 1,
                                                                        "libros prestados": 1
                                                                    }}
                                                                ),
                                                                lib.update_one(  # Base de datos de los libros
                                                                    {"registro": id},
                                                                    {"$inc": {
                                                                        "disponibles": -1,
                                                                        "en prestamo": 1,
                                                                        "veces prestado": 1

                                                                    }}
                                                                )
                                                                print(
                                                                    "Libro prestado con éxito, su fecha de entrega es: (aqui para cualdo logre hacer lo de las fechas aaaaaaaaa)")





                                                            else:
                                                                print(
                                                                    "Usted tiene en préstamo 3 libros, devuelva al menos 1 libro para hacer el nuevo préstamo.")

                                                    else:
                                                        rec = ""
                                                        while rec not in [1, 2, 3, 4]:
                                                            rec = int(input("Ingrese:\n"
                                                                            "-1 para prestar otro libro\n"
                                                                            "-2 para hacer otra búsqueda\n"
                                                                            "-3 para regresar al menú principal\n"
                                                                            "-4 para salir:"))

                                                            if rec == 1:
                                                                rw = ""

                                                            elif rec == 2:
                                                                otp = ""

                                                            elif rec == 3:
                                                                menu = ""

                                                            elif rec == 4:
                                                                print("Usted ha salido del sistema")
                                                                break
                                                                # working on this part at @30/05/21 12: 33 i hope come back at 15:00h

                                                else:
                                                    print("Este libro no se encuentra disponible para su prestamo")


                                    elif rw == 3:
                                        break

                            elif otp == 4:
                                bsc = int(input("Ingrese el id del libro:"))
                                for libro in lib.find({"registro": bsc},
                                                      {"Autor": 1, "Categoría": 1, "Edición": 1, "título": 1,
                                                       "registro": 1, "_id": 0}):
                                    a = libro
                                    print(a)

                                rw = ""
                                while rw not in [1, 2, 3]:
                                    rw = int(input("Ingrese: \n"
                                                   "-1  Hacer otra busqueda\n"
                                                   "-2  Prestar un libro\n"
                                                   "-3  Salir del sistema\n"))
                                    if rw == 1:
                                        otp = ""
                                    elif rw == 2:
                                        id = int(input("Ingrese el # de registro del libro que desea prestar: "))
                                        d = lib.find({"registro": id})
                                        if d is None:
                                            print("Libro no existente en el sistema")
                                            break

                                        else:
                                            for libro in lib.find({"registro": id}):

                                                a = libro
                                                if a['disponibles'] > 2:
                                                    libname = a['título']
                                                    lided = a['Edicion']
                                                    autor = a['Autor']
                                                    reg = a['registro']

                                                    print(
                                                        "Este libro se encuentra disponible para su préstamo")  # Query de prestamo
                                                    prestar = input(
                                                        f"¿desea prestar {libname}, {lided} edición, del autor {autor} y registro {reg}?[S/N]")
                                                    if prestar == 'S':
                                                        for user in col.find({'uname': c}):
                                                            z = user
                                                            if z['libros en prestamo'] < 3:
                                                                # base de datos de los usuarios
                                                                col.update_one(
                                                                    {"uname": c},
                                                                    {"$inc": {
                                                                        "libros en prestamo": 1,
                                                                        "libros prestados": 1
                                                                    }}
                                                                ),
                                                                lib.update_one(  # Base de datos de los libros
                                                                    {"registro": id},
                                                                    {"$inc": {
                                                                        "disponibles": -1,
                                                                        "en prestamo": 1,
                                                                        "veces prestado": 1

                                                                    }}
                                                                )
                                                                print(
                                                                    "Libro prestado con éxito, su fecha de entrega es: (aqui para cualdo logre hacer lo de las fechas aaaaaaaaa)")





                                                            else:
                                                                print(
                                                                    "Usted tiene en préstamo 3 libros, devuelva al menos 1 libro para hacer el nuevo préstamo.")

                                                    else:
                                                        rec = ""
                                                        while rec not in [1, 2, 3, 4]:
                                                            rec = int(input("Ingrese:\n"
                                                                            "-1 para prestar otro libro\n"
                                                                            "-2 para hacer otra búsqueda\n"
                                                                            "-3 para regresar al menú principal\n"
                                                                            "-4 para salir:"))

                                                            if rec == 1:
                                                                rw = ""

                                                            elif rec == 2:
                                                                otp = ""

                                                            elif rec == 3:
                                                                menu = ""

                                                            elif rec == 4:
                                                                print("Usted ha salido del sistema")
                                                                break
                                                                # working on this part at @30/05/21 12: 33 i hope come back at 15:00h

                                                else:
                                                    print("Este libro no se encuentra disponible para su prestamo")


                                    elif rw == 3:
                                        break


                            elif otp == 5:
                                print("Usted ha salido del sistema")
                                break


                    elif menu == 2:
                        print("aqui va el buscador para los libros que ha prestado el usuario ")
                    elif menu == 3:
                        print("Usted salido del sistema")
