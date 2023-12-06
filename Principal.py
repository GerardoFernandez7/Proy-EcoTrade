# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2005 - Algortimos y programación básica
# Cristian Sebastian Túnchez Castellanos (231359)
# Gerardo Andre Fernández Cruz (23763)
# Luis Fernando Palacios López (23933)
# Eddy Abigahil Giron Rodas (23073)

from Login import *
from Intercambios import *
from Stadistics import *

# Crear un ciclo para mostrar el menú principal hasta que se seleccione una opción válida
while True:
    print("\n----------# ¡Bienvenido al App de Intercambios! #----------")
    print("Elige una opción para iniciar:")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")
    menu_option = int(input("Ingresa tu opción: "))

    if menu_option == 1:
        crear_cuenta()    

    elif menu_option == 2:
        user = iniciar_sesion()
        
        while True:
            print("\n--------------------# Menú Principal #--------------------")
            print("¿Qué deseas realizar?")
            print("1. Editar infromación de tu cuenta")
            print("2. Ofrecer artículos")
            print("3. Ver mis publicaciones")
            print("4. Ver artículos disponbles")
            print("5. Bandeja de mensajes")
            print("6. Contratar un mensajero")
            print("7. Ver estadísticas del App (Administradores)")
            print("8. Cerrar sesión")
            menu2_option = int(input("Ingresa tu opción: "))

            if menu2_option == 1:
                editar_cuenta(user)
            
            elif menu2_option == 2:
                publicar(user)

            elif menu2_option == 3:
                my_posts(user)

            elif menu2_option == 4:
                all_posts(user)
            
            elif menu2_option == 5:
                mensajes(user)

            elif menu2_option == 6:
                mensajero()

            elif menu2_option == 7:
                validar_rol(user)

            elif menu2_option == 8:
                print("Sesión cerrada.")
                print("Volviendo al Menú inicial...")
                break
            else:
                print("No es una opción válida.")
        
    elif menu_option == 3:
        print("Gracias por cuidar el planeta. ¡Ten un lindo día!")
        break
    else:
        print("Tu opción no es válida, intenta de nuevo.")
