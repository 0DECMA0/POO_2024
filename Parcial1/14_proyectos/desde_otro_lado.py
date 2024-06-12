

def agregar_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"'{pelicula}' ha sido agregada a la lista.")

def eliminar_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"'{pelicula}' ha sido eliminada de la lista.")
    else:
        print(f"'{pelicula}' no se encuentra en la lista.")

def actualizar_peliculas(peliculas):
    pelicula_a_actualizar = input("Ingrese el nombre de la película que desea actualizar: ")
    if pelicula_a_actualizar in peliculas:
        indice = peliculas.index(pelicula_a_actualizar)
        nueva_pelicula = input("Ingrese el nuevo nombre de la película: ")
        peliculas[indice] = nueva_pelicula
        print(f"La película '{pelicula_a_actualizar}' ha sido actualizada a '{nueva_pelicula}'.")
    else:
        print(f"La película '{pelicula_a_actualizar}' no se encuentra en la lista.")


def consultar_peliculas(peliculas):
    if peliculas:
        print("\nLista de películas:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")
    else:
        print("\nNo hay películas en la lista.")

def vaciar_peliculas(peliculas):
    if peliculas:
        peliculas.clear()
        print("La lista de películas ha sido vaciada .")
    else:
        print("La lista de películas ya está vacía.")
