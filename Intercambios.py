# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2005 - Algortimos y programación básica
# Cristian Sebastian Túnchez Castellanos (231359)
# Gerardo Andre Fernández Cruz (23763)
# Luis Fernando Palacios López (23933)
# Eddy Abigahil Giron Rodas (23073)

import pandas as pd

# Función para facilitar opciones de materiales
def opt_mats(material):
    if material == 1:
        material = "Papel"
    elif material == 2:
        material = "Cartón"
    elif material == 3:
        material = "Plástico"
    elif material == 4:
        material = "Metales"
    elif material == 5:
        material = "Químicos"
    elif material == 6:
        material = "Electrónica"
    return material

#Función para publicar un artículo
def publicar(user):
    posts = pd.read_csv("Publicaciones.csv")
    articulo = input("¿Qué artículo estás ofreciendo? (Nombre): ")
    print("Listado de Materiales válidos para intercambios")
    print("1. Papel\n2. Cartón\n3. Plástico\n4. Metales\n5. Químicos\n6. Electrónica")
    material = int(input("¿De qué material está hecho su artículo? (No. 1-6): "))
    material = opt_mats(material)
    material2 = int(input("¿Qué material desea obtener a cambio? (No. 1-6): "))
    material2 = opt_mats(material2)
    post_nuevo = pd.DataFrame({'Usuario': [user], 'Articulo': [articulo], 'Material Ofrecido': [material], 'Material Deseado': [material2], 'Estado': "Disponible"})
    posts = posts.append(post_nuevo, ignore_index=True) # type: ignore
    posts.to_csv("Publicaciones.csv", index=False)
    print("¡Tu artículo fue publicado exitosamente!")

# Función auxiliar para eliminar una publicación
def remove_post(posts, index_to_remove):
    try:
        posts.drop(index=index_to_remove, inplace=True)
        posts.reset_index(drop=True, inplace=True)
        posts.to_csv('Publicaciones.csv', index=False)  # Agregar esta línea para guardar los cambios en el archivo CSV
        return True
    except KeyError:
        return False

# Función auxiliar para verificar a los usuarios
def check_user_exist(username):
    users = pd.read_csv("Users.csv", index_col=0)
    return username in users.index

# Función auxiliar para evaluar a los usuarios
def rate_user(username):
    rating = None
    while rating is None:
        try:
            print("\n# Escoge una calificación basada en tu experiencia #")
            print("★: Terrible")
            print("★★: Malo")
            print("★★★: Intermedio")
            print("★★★★: Bueno")
            print("★★★★★: Excelente")
            rating = int(input("\nIngresa la cantidad de estrellas para el usuario {}: ".format(username)))
            if rating < 1 or rating > 5:
                print("Calificación inválida. Debe ser un número entre 1 y 5.")
                rating = None
        except ValueError:
            print("Calificación inválida. Debe ser un número entero.")
            rating = None
    return rating

# Función auxiliar para promediar la evaluación a los usuarios
def update_user_rating(username, rating):
    users = pd.read_csv("Users.csv", index_col=0)
    current_rating = users.loc[username, "Rating"]
    num_ratings = users.loc[username, "NumRatings"]

    new_rating = (current_rating * num_ratings + rating) // (num_ratings + 1) # type: ignore
    users.loc[username, "Rating"] = new_rating
    users.loc[username, "NumRatings"] += 1 # type: ignore

    users.to_csv("Users.csv")

# Función para gestionar las publicaciones de los usuarios
def my_posts(user):
    posts = pd.read_csv("Publicaciones.csv")
    my_posts = posts.loc[posts['Usuario'] == user, ['Articulo', 'Material Ofrecido', 'Material Deseado', 'Estado']]
    if my_posts.empty:
        print("\nNo tienes publicaciones aún.")
    else:
        print("\n---------------# Tus Publicaciones #---------------")
        print(my_posts.to_string(index=False))
        
        while True:
            print("\n¿Deseas realizar algo más?")
            print("1. Eliminar una publicación")
            print("2. Marcar una publicación como 'Intercambiado'")
            print("3. Regresar")
            option = int(input("Ingresa tu opción: "))
            
            # Eliminar una publicación
            if option == 1:
                print("\n# Selecciona el número de la publicación que deseas eliminar #\n")
                for i, post in enumerate(my_posts.iterrows()):
                    print(i + 1, post[1]['Articulo'], post[1]['Material Ofrecido'], post[1]['Material Deseado'], post[1]['Estado'])
                idx = int(input("\nIngresa tu opción: "))
                if idx > 0 and idx <= len(my_posts):
                    index_to_remove = my_posts.index[idx-1]
                    if my_posts.loc[index_to_remove, 'Estado'] == "Intercambiado": # type: ignore
                        print("No puedes eliminar una publicación que ha sido marcada como 'Intercambiado'.")
                    else:
                        if remove_post(posts, index_to_remove):
                            print("\nPublicación eliminada correctamente.")
                        else:
                            print("\nOpción inválida. Intenta de nuevo.")
                else:
                    print("\nOpción inválida. Intenta de nuevo.")
            
            elif option == 2:
                print("\n# Selecciona el número de la publicación que deseas marcar como 'Intercambiado' #\n")
                for i, post in enumerate(my_posts.iterrows()):
                    print(i + 1, post[1]['Articulo'], post[1]['Material Ofrecido'], post[1]['Material Deseado'], post[1]['Estado'])
                idx = int(input("\nIngresa tu opción: "))
                if idx > 0 and idx <= len(my_posts):
                    index_to_update = my_posts.index[idx-1]
                    if my_posts.loc[index_to_update, 'Estado'] == "Intercambiado": # type: ignore
                        print("Esta publicación ya ha sido marcada como 'Intercambiado'.")
                    else:
                        other_username = input("\nIngresa el nombre de usuario de la otra persona involucrada en el intercambio: ")
                        if check_user_exist(other_username):
                            rating = rate_user(other_username)
                            update_user_rating(other_username, rating)
                            posts.loc[index_to_update, 'Estado'] = "Intercambiado"
                            posts.to_csv("Publicaciones.csv", index=False)
                            print("\nPublicación marcada como 'Intercambiado'")
                            print("Calificación recibida. ¡Gracias por tu retroalimentación!")
                        else:
                            print("El nombre de usuario del otro usuario no existe.")
                else:
                    print("Opción inválida. Intenta de nuevo.")
 
            elif option == 3:
                print("Volviendo al menú principal...")
                break
            
            else:
                print("Opción inválida. Intenta de nuevo.")

# Función para acceder a todas las publicaciones
def all_posts(user):
    posts = pd.read_csv("Publicaciones.csv")
    all_posts = posts.loc[posts['Usuario'] != user]
    print("\n-------------------------# Todas las Publicaciones #-------------------------")
    print(all_posts)

# Función para manejar los mensajes en la app
def mensajes(user):
    usuarios = pd.read_csv("Users.csv", index_col=0)
    mensajeria = pd.read_csv("Mensajeria.csv")
    
    while True:
        print("\n---------------# Bandeja de Entrada #---------------")
        print("¿Qué deseas hacer?")
        print("1. Enviar mensaje")
        print("2. Ver bandeja de entrada")
        print("3. Regresar")
        menu_opt = int(input("Ingresa tu opción: "))

        if menu_opt == 1:
            destinario = input("Destinario (usuario): ")
            if destinario not in usuarios.index:
                print("No hemos podido encontrar el usuario ingresado.")
            else:
                mensaje = input("Ingresa tu mensaje:\n")
                mensaje_nuevo = pd.DataFrame({'Emisor': [user], 'Destinario': [destinario], 'Mensaje': [mensaje]})
                mensajeria = mensajeria.append(mensaje_nuevo) # type: ignore
                mensajeria.to_csv("Mensajeria.csv", index=False)
                print("Mensaje enviado correctamente.")

        elif menu_opt == 2:
            my_messages = mensajeria.loc[mensajeria['Destinario'] == user, ['Emisor', 'Mensaje']]
            if my_messages.empty:
                print("\nNo tienes mensajes.")
            else:
                print("\n--------------------# Tus Mensajes #--------------------")
                print(my_messages)

        elif menu_opt == 3:
            print("Volviendo al menú principal...")
            break
        else:
            print("No es una opción válida.")

# Función para contratar un mensajero
def mensajero():
    print("\n--------------# Servicio de Mensajería #--------------")
    address1 = input("Ingrese la dirección de recogida: ")
    address2 = input("Ingrese la dirección de entrega: ")
    print("Tu solicitud fue enviada. Recibirás un mensaje cuando un mensajero acepte tu petición.")
