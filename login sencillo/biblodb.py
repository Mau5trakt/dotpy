from pymongo import MongoClient
client = MongoClient('mongodb+srv://usuarios:RgvAZFpFu9LYm5RF@cluster0.8oeno.mongodb.net/ex01?retryWrites=true&w=majority')
import random
db = client['ex01']
col = db['corprueb']

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
                uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                bususer = col.find_one({'uname':uname})
                while bususer is not None:
                    uname = ((name[0:2]) + (surname[0:2]) + str(random.randint(0, 999))).lower()
                print(f"Su nombre de usario es: {uname}")
                col.insert_one({
                    'Nombre':name,
                    'Apellido':surname,
                    '# telefónico': num,
                    'uname':uname})
                print("Registro correcto")

    if op == 'I':
        init = ""
        while init != True:
            init = input("Ingrese su nombre de usuario: \n")
            a = col.find_one({'uname':init})
            if a is None:
                print("Usuario no encontrado")
            else:
                init = True
                print("Usted ha iniciado sesión correctamente")
                menu = ""
                while menu not in [1,2,3]:
                    menu = int(input(" -1 Buscar libro \n -2 Ver mis libros prestados \n -3 Salir "))

                    if menu == 1:
                        print("aqui va el buscador de la db para los libros")
                    elif menu == 2:
                        print("aqui va el buscador para los libros que ha prestado el usuario ")
                    elif menu == 3:
                        print("Usted salido del sistema")










