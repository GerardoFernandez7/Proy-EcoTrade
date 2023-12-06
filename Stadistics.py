# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2005 - Algortimos y programación básica
# Cristian Sebastian Túnchez Castellanos (231359)
# Gerardo Andre Fernández Cruz (23763)
# Luis Fernando Palacios López (23933)
# Eddy Abigahil Giron Rodas (23073)

import pandas as pd
import matplotlib.pyplot as plt

# Grafica de barras de los residuos más intercambiados
def grafica_residuos_intercambiados():
    # Cargar el archivo CSV
    df = pd.read_csv("Publicaciones.csv")

    # Filtrar las filas con estado "Intercambiado"
    intercambiado_df = df[df['Estado'] == 'Intercambiado']

    # Contar la frecuencia de cada tipo de residuo en la columna "Material Ofrecido"
    frecuencia_residuos = intercambiado_df['Material Ofrecido'].value_counts()

    # Crear la gráfica de barras
    frecuencia_residuos.plot(kind='bar')

    # Personalizar la gráfica
    plt.xlabel('Tipo de Residuo')
    plt.ylabel('Cantidad de Intercambios')
    plt.title('Distribución de Tipos de Residuos Más Intercambiados')

    # Mostrar la gráfica
    plt.show()

# Gráfica de líneas de la evolución de usuarios registrados por mes
def grafica_registros_por_mes():
    # Cargar el archivo CSV con index_col=0
    df = pd.read_csv('Users.csv', index_col=0)

    # Obtener la frecuencia de registros por mes
    registros_por_mes = df['Fecha'].value_counts().sort_index()

    # Crear la gráfica de líneas
    plt.plot(registros_por_mes.index, registros_por_mes.values, marker='o')

    # Configurar los títulos y etiquetas de la gráfica
    plt.title('Evolución del Número de Nuevos Registros por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Número de Nuevos Registros')

    # Mostrar la gráfica
    plt.show()

# Gráfica de barras de los ratings más usados por los usuarios
def rating_mas_usado():
    # Cargar el archivo CSV
    df = pd.read_csv("Users.csv", index_col=0)

    # Calcular la frecuencia de cada valor de la columna "Rating"
    rating_counts = df['Rating'].value_counts().sort_index()

    # Crear el gráfico de barras
    plt.bar(rating_counts.index, rating_counts.values) # type: ignore
    plt.xlabel('Rating')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Calificaciones')
    plt.show()

# Función para tener acceso a las gráficas (permisos de administrador)
def validar_rol(user):
    # Cargar el archivo CSV con index_col=0
    df = pd.read_csv("Users.csv", index_col=0)

    # Buscar el usuario en el archivo
    user = df.loc[user]

    if pd.isnull(user).all():
        print("Usuario no encontrado.")
    else:
        # Obtener el valor de la columna "Rol" para el usuario
        role = user['Rol']

        if role == 'admin':
            # Realizar la acción deseada para el usuario con rol "Admin"
            while True:
                print("\n---------- # ¿Qué gráfica deseas ver? #----------")
                print("1. Residuos más intercambiados")
                print("2. Registro de usuarios por mes")
                print("3. Calificaciones de usuarios más usuadas")
                print("4. Regresar")
                menu_opt = int(input("Ingresa tu opción: "))

                if menu_opt == 1:
                    grafica_residuos_intercambiados()
                elif menu_opt == 2:
                    grafica_registros_por_mes()
                elif menu_opt == 3:
                    rating_mas_usado()
                elif menu_opt == 4:
                    print("Volviendo al Menú Principal...")
                    break
                else:
                    print("No es una opción válida.")
        else:
            print("Lo siento, esta opción es solo para administradores.")
