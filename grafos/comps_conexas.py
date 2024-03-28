from cola import Cola
from ejemplos import fronteras
import random

# Implementar un algoritmo que reciba un grafo dirigido, un vértice V y un número N,
# y devuelva una lista con todos los vértices que se encuentren a exactamente N aristas
# de distancia del vértice V. Indicar el tipo de recorrido utilizado y el orden del algoritmo. Justificar.


def bfs_aristas_n(grafo, origen, n):
    pass


def es_conexo(grafo):
    visitados = set()
    cola = Cola()
    origen = random.choice(grafo.keys())
    visitados.add(origen)
    cola.encolar(origen)
    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                cola.encolar(w)
                visitados.add(w)
    return len(visitados) == len(grafo)


def dfs_comps(grafo, v, visitados, componente):
    visitados.add(v)
    componente.append(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs_comps(grafo, w, visitados, componente)


def contar_aristas(grafo):
    contador = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            contador += 1
    return contador // 2


def contar_componetes_conexas(grafo):
    visitados = set()
    comps = 0
    resultado = []
    for v in grafo:
        if v not in visitados:
            nueva_componente = []
            resultado.append(nueva_componente)
            comps += 1
            dfs_comps(grafo, v, visitados, nueva_componente)
    return resultado


def es_arbol(grafo):
    return es_conexo(grafo) and \
           contar_aristas(grafo) == len(grafo) - 1


if __name__ == "__main__":
    print(es_arbol(fronteras))
