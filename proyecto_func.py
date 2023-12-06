#Importar modulos
import numpy as np
import pandas as pd
import matplotlib as plt

        # Funciones
def registro():
    # Solicitar al usuario que ingrese los valores para cada campo
    nombre = input('Ingrese su nombre: ')
    username = input('Ingrese su nombre de usuario: ')
    ocupacion = input('Ingrese a que se dedica su empresa: ')
    email = input('Ingrese su dirección de correo electrónico: ')
    password = input('Ingrese su contraseña: ')

    if '.com' not in email:
        print("")
        print('Error: El correo electrónico debe contener .com')
        print("")
        return

    # Leer el archivo CSV existente en un DataFrame
    try:
        df = pd.read_csv('intercambios.csv')
    except FileNotFoundError:
        # Si el archivo no existe, crear un DataFrame vacío con las columnas necesarias
        df = pd.DataFrame(columns=['Nombre', 'Username', 'Ocupacion', 'Email', 'Password', 'Ofrece', 'Desea', 'Bandeja', 'Ubicacion'])

    # Verificar si el nombre de usuario ya existe en el DataFrame
    if username in df['Username'].values:
        print("")
        print('Error: El nombre de usuario ya existe en el archivo.')
        print("")
        return

    # Crear un nuevo DataFrame con los datos del usuario
    data = pd.DataFrame({
        'Nombre': [nombre],
        'Username': [username],
        'Ocupacion': [ocupacion],
        'Email': [email],
        'Password': [password]
    })
    # Agregar el nuevo usuario al DataFrame existente
    df = pd.concat([df, data], ignore_index=True)
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv('intercambios.csv', index=False)

    print("")
    print("Te has registrado exitosamente!")
    print("Aviso: para iniciar sesion deben haber al menos 2 usuarios registrados en la base de datos")
    print("")

def iniciar_sesion():
    seguir_en_programa = True
    df = pd.read_csv('intercambios.csv')

    # Solicitar al usuario que ingrese su nombre de usuario y contraseña
    usuario = input('Nombre de usuario: ')
    contrasena = input('Contraseña: ')

    # Verificar si el usuario y la contraseña son válidos
    usuario_valido = df.loc[df['Username'] == usuario]
    if not usuario_valido.empty and usuario_valido['Password'].iloc[0] == contrasena:
        print("")
        print('¡Inicio de sesión exitoso!')
        print("")  
    else:
        print("")
        print('¡Nombre de usuario o contraseña incorrectos!')
        print("")
        return

    while seguir_en_programa:
        print('¿Qué deseas realizar?')
        print('1. Crear una nueva publicación')
        print('2. Ver mis publicaciones')
        print('3. Ver artículos disponibles para intercambiar')
        print('4. Bandeja de mensajes')
        print('5. Contratar un mensajero')
        print('6. Cerrar sesión')

        opcion = input("Seleccione una opción válida: ") 

        # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú 
        if not opcion.isdigit():
            print("Seleccione un tipo de valor válido")
            continue
        else:
            opcion = int(opcion)

        if opcion == 1:
            publicacion(usuario)

        elif opcion == 2:
            ver_mis_publicaciones(usuario)

        elif opcion == 3:
            articulos_disponibles()
            print("")
            print("¿Estás interesado en alguno?")
            print("1. Sí")
            print("2. No, salir")

            sub_opcion = input("Seleccione una opción válida: ") 

            # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú 
            if not sub_opcion.isdigit():
                print("Seleccione un tipo de valor válido") 
                continue
            else:
                sub_opcion = int(sub_opcion)

            if sub_opcion == 1:
                quiero = input("¿En cuál artículo estás interesado?: ")
                print("")
                print("Excelente eleccion! Nuestro equipo se pondrá en contacto con usted.")
                print("")
                df.loc[df['Ofrece'].str.strip() == quiero.strip(), 'Ofrece'] = np.nan
                df.to_csv('intercambios.csv', index=False)

            elif sub_opcion == 2: 
                print("")         
            else: 
                print("Seleccione una opción válida.")

        elif opcion == 4:
            mensajes(usuario)

        elif opcion == 5:
            delivery(usuario)

        elif opcion == 6:
            seguir_en_programa = False 
            print("")
            print("La sesion ha sido cerrada. Gracias por usar nuestro servicio.")
            print("")         
        else: 
            print("Seleccione una opción válida.")

def publicacion(usuario):
    df = pd.read_csv('intercambios.csv')

    # Verificar si el usuario ya existe en el DataFrame
    if str(usuario) in df['Username'].astype(str).values:
        # Si el usuario ya existe, obtener el índice de su fila
        index = df.index[df['Username'] == usuario].tolist()[0]

        print("")
        print('¡Preparemos tu publicación!')
        articulos = input('¿Qué artículo(s) estás ofreciendo? ')

        # Actualizar el valor de la columna 'Ofrece' para el usuario
        df.at[index, 'Ofrece'] = articulos
        
        articulo_deseado = input('¿Qué artículo deseas obtener a cambio? ')
        print("")

        # Actualizar el valor de la columna 'Desea' para el usuario
        df.at[index, 'Desea'] = articulo_deseado

        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv('intercambios.csv', index=False)
        print("")
        print('Su publicacion se ha publicado exitosamente. ¡Buena suerte encontrando un intercambio!')
        print("")
    else:
        print("")
        print('Error: El usuario no existe en el archivo.')
        print("")

def ver_mis_publicaciones(usuario):
    df = pd.read_csv('intercambios.csv')
    # Filtrar el DataFrame para mostrar solo las publicaciones del usuario
    df_usuario = df[df['Username'] == usuario]

    if df_usuario.empty:
        print("")
        print('No tienes publicaciones.')
        print("")
    else:
        print("")
        print('Mis publicaciones son: ')
        for index, row in df_usuario.iterrows():
            print(f'Ofrezco: {row["Ofrece"]}, Deseo: {row["Desea"]}')
            print("")

def articulos_disponibles():
    df = pd.read_csv('intercambios.csv')
    unicos = df['Ofrece'].unique()
    print("")
    print("Los articulos disponibles para intercambiar son:")
    print(unicos)
    print("")

def mensajes(usuario):
    df = pd.read_csv('intercambios.csv')
    mensajes = df.loc[df['Bandeja'] == usuario, 'Bandeja']
    if mensajes.empty:
        print("")
        print("No tienes mensajes en tu bandeja.")
        print("")
    else:
        print("")
        print("Tus mensajes en la bandeja son:")
        print("")
        for mensaje in mensajes:
            print(mensaje)

def delivery(usuario):
    df = pd.read_csv('intercambios.csv')
        # Verificar si el usuario ya existe en el DataFrame
    if str(usuario) in df['Username'].astype(str).values:
        # Si el usuario ya existe, obtener el índice de su fila
        index = df.index[df['Username'] == usuario].tolist()[0]

        print("")
        ubic = input('Ingrese su direccion para enviar al mensajero a esta ubicacion: ')

        # Actualizar el valor de la columna 'Ubicacion' para el usuario
        df.at[index, 'Ubicacion'] = ubic

        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv('intercambios.csv', index=False)
        print("")
        print('Su ubicacion se ha guardado exitosamente. ¡Su mensajero esta en camino!')
        print("")
    else:
        print("")
        print('Error: El usuario no existe en el archivo.')
        print("")