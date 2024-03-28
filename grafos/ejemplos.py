from grafo import Grafo
from lazy import LazyValue


def _fuerza_bruta():
    g1 = Grafo(False, range(8))
    g1.arista(0, 1)
    g1.arista(1, 2)
    g1.arista(1, 5)
    g1.arista(2, 3)
    g1.arista(3, 5)
    g1.arista(3, 4)
    g1.arista(5, 4)
    g1.arista(7,4)
    g1.arista(5, 6)
    g1.arista(7, 6)
    return g1


def _n_reinas(n):
    casillero = lambda i, j: str(i + 1) + chr(ord('a') + j)
    g = Grafo()
    for i in range(n):
        for j in range(n):
            g.agregar_vertice(casillero(i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j, n):
                g.arista(casillero(i, j), casillero(i, k))
    # Agrego por columnas
    for j in range(n):
        for i in range(n):
            for k in range(i, n):
                g.arista(casillero(i, j), casillero(k, j))

    # agrego por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(n - max((i, j))):
                g.arista(casillero(i, j), casillero(i + k, j + k))
            for k in range(min(n-i, j)):

                g.arista(casillero(i, j), casillero(i + k, j - k))
    return g


def _fronteras():
    PAISES = ["ARG", "BRA", "URU", "CHI", "PER", "PAR", "BOL", "ECU", "VEN", "COL", "SUR", "GUY", "GUF", "POL", "ALE", "FRA", "AUS"]
    g = Grafo(False, PAISES)
    g.arista("ARG", "URU")
    g.arista("ARG", "CHI")
    g.arista("ARG", "BOL")
    g.arista("ARG", "BRA")
    g.arista("ARG", "PAR")
    g.arista("BRA", "URU")
    g.arista("BRA", "PAR")
    g.arista("BRA", "BOL")
    g.arista("BRA", "SUR")
    g.arista("BRA", "GUF")
    g.arista("BRA", "GUY")
    g.arista("BRA", "VEN")
    g.arista("BRA", "COL")
    g.arista("BRA", "PER")
    g.arista("CHI", "BOL")
    g.arista("CHI", "PER")
    g.arista("PAR", "BOL")
    g.arista("PER", "BOL")
    g.arista("ECU", "PER")
    g.arista("ECU", "COL")
    g.arista("COL", "PER")
    g.arista("COL", "VEN")
    g.arista("VEN", "GUY")
    g.arista("SUR", "GUY")
    g.arista("SUR", "GUF")
    g.arista("POL", "ALE")
    g.arista("ALE", "FRA")
    return g


def _actores():
    actores_por_pelicula = {}
    actores = set()
    with open("actores_test.csv") as f:
        for l in f:
            splitted = l.strip().split(",")
            actor = splitted[0]
            actores.add(actor)
            peliculas = splitted[1:]
            for peli in peliculas:
                if peli not in actores_por_pelicula:
                    actores_por_pelicula[peli] = []
                actores_por_pelicula[peli].append(actor)

    g = Grafo()
    for peli in actores_por_pelicula:
        if len(actores_por_pelicula[peli]) < 2:
            continue
        for i in range(len(actores_por_pelicula[peli])):
           for j in range(i + 1, len(actores_por_pelicula[peli])):
                if actores_por_pelicula[peli][i] not in g:
                    g.agregar_vertice(actores_por_pelicula[peli][i])
                if actores_por_pelicula[peli][j] not in g:
                    g.agregar_vertice(actores_por_pelicula[peli][j])
                g.arista(actores_por_pelicula[peli][i], actores_por_pelicula[peli][j])
    return g


def _ej_topologico():
    MATERIAS = ["Introducción al Desarrollo de Software", "Fundamentos de Programación",
                "Algoritmos y Estructuras de Datos", "Análisis Matemático II",
                "Álgebra Lineal", "Organización del Computador", "Paradigmas de Programación",
                "Probabilidad y Estadística", "Teoría de Algoritmos", "Sistemas Operativos",
                "Base de Datos", "Modelación Numérica", "Taller de Programación",
                "Ingeniería de Software I", "Ciencia de Datos", "Gestión del Desarrollo de Sistemas Informáticos",
                "Programación Concurrente", "Redes", "Ingeniería de Software II", "Sistemas Distribuidos I",
                "Taller de Seguridad Informática"]
    g = Grafo(True, MATERIAS)
    g.arista("Introducción al Desarrollo de Software", "Paradigmas de Programación")
    g.arista("Fundamentos de Programación", "Algoritmos y Estructuras de Datos")
    g.arista("Fundamentos de Programación", "Organización del Computador")
    g.arista("Introducción al Desarrollo de Software", "Teoría de Algoritmos")
    g.arista("Algoritmos y Estructuras de Datos", "Paradigmas de Programación")
    g.arista("Algoritmos y Estructuras de Datos", "Teoría de Algoritmos")
    g.arista("Algoritmos y Estructuras de Datos", "Modelación Numérica")
    g.arista("Análisis Matemático II", "Probabilidad y Estadística")
    g.arista("Análisis Matemático II", "Modelación Numérica")
    g.arista("Álgebra Lineal", "Probabilidad y Estadística")
    g.arista("Álgebra Lineal", "Modelación Numérica")
    g.arista("Organización del Computador", "Sistemas Operativos")
    g.arista("Organización del Computador", "Taller de Programación")
    g.arista("Organización del Computador", "Base de Datos")
    g.arista("Paradigmas de Programación", "Taller de Programación")
    g.arista("Paradigmas de Programación", "Base de Datos")
    g.arista("Paradigmas de Programación", "Ingeniería de Software I")
    g.arista("Sistemas Operativos", "Redes")
    g.arista("Sistemas Operativos", "Programación Concurrente")
    g.arista("Taller de Programación", "Programación Concurrente")
    g.arista("Teoría de Algoritmos", "Ciencia de Datos")
    g.arista("Probabilidad y Estadística", "Ciencia de Datos")
    g.arista("Base de Datos", "Ciencia de Datos")
    g.arista("Modelación Numérica", "Ciencia de Datos")
    g.arista("Base de Datos", "Ingeniería de Software II")
    g.arista("Ingeniería de Software I", "Ingeniería de Software II")
    g.arista("Ingeniería de Software I", "Gestión del Desarrollo de Sistemas Informáticos")
    g.arista("Redes", "Sistemas Distribuidos I")
    g.arista("Redes", "Taller de Seguridad Informática")
    g.arista("Programación Concurrente", "Sistemas Distribuidos I")
    return g


def _camino_minimo():
    g = Grafo(False, [1, 2, 3, 4, 5, 6])
    g.arista(1, 2, 7)
    g.arista(1, 6, 14)
    g.arista(1, 3, 9)
    g.arista(2, 3, 10)
    g.arista(2, 4, 15)
    g.arista(3, 4, 11)
    g.arista(3, 6, 2)
    g.arista(4, 5, 6)
    g.arista(5, 6, 9)
    return g


def ejemplo_ptos():
    g = Grafo(False, ["Jorge", "Dato", "Cami", "Nacho", "Mati", "Jas", "Eze", "Rosita", "Martin", "Fede", "Pablo"])
    g.arista("Jorge", "Martin")
    g.arista("Jorge", "Dato")
    g.arista("Jorge", "Cami")
    g.arista("Jorge", "Nacho")
    g.arista("Jorge", "Jas")
    g.arista("Pablo", "Martin")
    g.arista("Fede", "Martin")
    g.arista("Fede", "Pablo")
    g.arista("Jas", "Eze")
    g.arista("Rosita", "Eze")
    g.arista("Mati", "Dato")
    g.arista("Mati", "Nacho")
    g.arista("Nacho", "Cami")
    return g


def ejemplo_cfcs():
    g = Grafo(True, ["Jorge", "Dato", "Cami", "Nacho", "Mati", "Jas", "Eze", "Rosita", "Martin", "Fede", "Pablo"])
    g.arista("Pablo", "Fede")
    g.arista("Fede", "Pablo")
    g.arista("Fede", "Martin")
    g.arista("Martin", "Pablo")
    g.arista("Jorge", "Martin")
    g.arista("Jorge", "Jas")
    g.arista("Eze", "Jas")
    g.arista("Jas", "Eze")
    g.arista("Eze", "Rosita")
    g.arista("Jorge", "Dato")
    g.arista("Jorge", "Cami")
    g.arista("Dato", "Mati")
    g.arista("Mati", "Nacho")
    g.arista("Nacho", "Jorge")
    g.arista("Cami", "Nacho")
    return g


fronteras = _fronteras()
actores_lazy = LazyValue(lambda: _actores())
correlativas = _ej_topologico()
wiki_camino_minimo = _camino_minimo()
catedra = ejemplo_ptos()
catedra_dir = ejemplo_cfcs()
