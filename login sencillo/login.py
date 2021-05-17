print("Bienvenido al sistema, ingrese sus credenciales a continuación")
login = {84289860}
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
            '''
            Bueno aqui es donde conecto la db y le paso los valores que salen en confir
            '''
        print("Usted se ha registrado satisfactoriamente")
    elif op == 'I':
        conf = ""
        while conf not in login:
            conf = int(input("Ingrese su número telefónico"))
            if conf in login:
                print("Bienvenido")

''''#aqui cargo la db y segun el numero obtengo el nombre
Bueno la verdad es que voy a hacerlo con el username y pass pero es de prueba para ver como funciona xD
Y ya después muestro el menu'''
