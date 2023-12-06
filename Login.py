# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2005 - Algortimos y programación básica
# Cristian Sebastian Túnchez Castellanos (231359)
# Gerardo Andre Fernández Cruz (23763)
# Luis Fernando Palacios López (23933)
# Eddy Abigahil Giron Rodas (23073)

import pandas as pd
import hashlib

# Crear cuenta
def crear_cuenta():
    usuarios = pd.read_csv("Users.csv", index_col=0)
    while True:
        nombre_usuario = input("Ingresa un nombre de usuario: ")
        if nombre_usuario in usuarios.index:
            print("El nombre de usuario ya existe, por favor intenta con otro.")
        else:
            break
    contraseña = input("Ingrese su contraseña: ")
    password = encriptar_contraseña(contraseña)
    nombre = input("Ingresa un Nombre y Apellido: ")
    trabajo = input("¿Cuál es su ocupación?: ")
    email = input("Correo electrónico: ")
    while True:
        fecha = int(input("Ingresa el número de mes actual (1-12): "))
        if 0 < fecha < 13:
            break
        else:
            print("\nIngresa un número válido.\n")
    usuario_nuevo = pd.DataFrame({'Nombre': [nombre], 'Ocupacion': [trabajo], 'contraseña': [password], 'Correo': [email], 'Fecha': [fecha], 'Rol': "usuario"}, index=[nombre_usuario])
    usuarios = pd.concat([usuarios, usuario_nuevo])
    usuarios.to_csv("Users.csv")
    print("Usuario creado exitosamente.")

# Encriptar la contraseña
def encriptar_contraseña(contraseña):
    # Crear un objeto de hash utilizando el algoritmo SHA-256
    sha256 = hashlib.sha256()

    # Convertir la contraseña a bytes (ya que la función de hash requiere una entrada en bytes)
    contraseña_bytes = contraseña.encode('utf-8')

    # Encriptar la contraseña
    sha256.update(contraseña_bytes)

    # Obtener la representación hexadecimal del hash encriptado
    contraseña_encriptada = sha256.hexdigest()

    return contraseña_encriptada

# Iniciar sesión
def iniciar_sesion():
    usuarios = pd.read_csv("Users.csv", index_col=0)
    while True:
        user = input("Ingrese su nombre de usuario: ")
        if user not in usuarios.index:
            print("Nombre de usuario no encontrado, por favor intenta de nuevo.")
        else:
            break
    while True:
        contraseña = input("Contraseña: ")
        password = encriptar_contraseña(contraseña)
        if usuarios.loc[user, 'contraseña'] != password: # type: ignore
            print("Contraseña incorrecta, por favor intenta de nuevo.")
        else:
            break
    print("Inicio de sesión exitoso.")
    return user

# Editar información de la cuenta
def editar_cuenta(user):
    usuarios = pd.read_csv("Users.csv", index_col=0)
    while True:
        print("¿Qué deseas editar?")
        print("1. Contraseña\n2. Nombre\n3. Ocupación\n4. Correo\n5. Regresar")
        opt_menu = int(input("Ingresa tu opción: "))

        if opt_menu == 1:
            contraseña = input("Ingresa una nueva contraseña: ")
            password = encriptar_contraseña(contraseña)
            usuarios.loc[user, 'contraseña'] = password
            usuarios.to_csv("Users.csv")
            print("Contraseña cambiada")

        elif opt_menu == 2:
            nombre = input("Ingresa un nuevo Nombre y Apellido: ")
            usuarios.loc[user, 'Nombre'] = nombre
            usuarios.to_csv("Users.csv")
            print("Nombre cambiado")

        elif opt_menu == 3:
            trabajo = input("Ingresa tu nueva ocupación: ")
            usuarios.loc[user, 'Ocupacion'] = trabajo
            usuarios.to_csv("Users.csv")
            print("Ocupación cambiada")

        elif opt_menu == 4:
            email = input("Ingresa tu nuevo correo electrónico: ")
            usuarios.loc[user, 'Correo'] = email
            usuarios.to_csv("Users.csv")
            print("Correo cambiado")

        elif opt_menu == 5:
            print("Regresando al menú principal...")
            break
        else:
            print("No es una opción válida")