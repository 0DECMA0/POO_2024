

def agregar_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"'{pelicula}' ha sido agregada a la lista.")

def remover_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"'{pelicula}' ha sido removida de la lista.")
    else:
        print(f"'{pelicula}' no se encuentra en la lista.")

def consultar_peliculas(peliculas):
    if peliculas:
        print("\nLista de películas:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")
    else:
        print("\nNo hay películas en la lista.")