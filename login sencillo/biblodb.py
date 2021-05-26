from pymongo import MongoClient
client = MongoClient('mongodb+srv://usuarios:RgvAZFpFu9LYm5RF@cluster0.8oeno.mongodb.net/ex01?retryWrites=true&w=majority')
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
                break

            else:
                confir = input(f"Su nombre es {name}, su apellido es {surname} y su número de telefono es {num}?[S/N]")
                #Funcion que crea el nombre de usuario
                uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                bususer = col.find_one({'uname':uname}) #Buscar el nombre de usuario generado
                while bususer is not None:  #Si el nombre de usuario ya existe en el sistema se genera otro
                    uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                print(f"Su nombre de usario es: {uname}")

                col.insert_one({                            #Insertar el nombre de usuario en la db
                    'Nombre':name,
                    'Apellido':surname,
                    '# telefónico': num,
                    'uname':uname})
                print("Registro correcto")

    if op == 'I':
        init = ""
        while init != True:
            init = input("Ingrese su nombre de usuario: \n")
            a = col.find_one({'uname':init})                #Buscar el nombre de usuario en la db
            if a is None:
                print("Usuario no encontrado")
            else:
                init = True
                print("Usted ha iniciado sesión correctamente")
                menu = ""
                while menu not in [1,2,3]: #Opciones al ingresar
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
                                for libro in lib.find({"título":bsc}): #Metodo de búsqueda
                                    a = libro
                                    print(a)
                                rw =input("¿Desea hacer otra busqueda? [S/N]")
                                if rw == 'S':
                                    otp = ""
                                else:
                                    break

                            elif otp == 2:
                                bsc = input("Ingrese el autor del libro:")
                                for libro in lib.find({"Autor": bsc}):
                                    a = libro
                                    print(a)
                                rw = input("¿Desea hacer otra busqueda? [S/N]")
                                if rw == 'S':
                                    otp = ""
                                else:
                                    break

                            elif otp == 3:
                                bsc = input("Ingrese el la categoría del libro:")
                                for libro in lib.find({"Categoría": bsc}):
                                    a = libro
                                    print(a)
                                rw = input("¿Desea hacer otra busqueda? [S/N]")
                                if rw == 'S':
                                    otp = ""
                                else:
                                    break

                            elif otp == 4:
                                bsc = input("Ingrese el id del libro:")
                                for libro in lib.find({"registro": bsc}):
                                    a = libro
                                    print(a)
                                rw = input("¿Desea hacer otra busqueda? [S/N]")
                                if rw == 'S':
                                    otp = ""
                                else:
                                    break

                            elif otp == 5:
                                print("Usted ha salido del sistema")
                                break


                    elif menu == 2:
                        print("aqui va el buscador para los libros que ha prestado el usuario ")
                    elif menu == 3:
                        print("Usted salido del sistema")










