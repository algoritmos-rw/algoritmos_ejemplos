from cola import Cola
from ejemplos import fronteras
import sys
sys.setrecursionlimit(10000)


def bfs(grafo, origen):
    visitados = set()
    padres = {} # diccionario en python
    orden = {}
    padres[origen] = None # None == nil
    orden[origen] = 0 # orden.Guardar(origen, 0)
    visitados.add(origen)
    q = Cola()  # usar deque de collections, NO QUEUE!!
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.encolar(w)
    return padres, orden


def _dfs(grafo, v, visitados, padres, orden):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            padres[w] = v
            orden[w] = orden[v] + 1
            _dfs(grafo, w, visitados, padres, orden)


def dfs(grafo, origen):
    padres = {}
    orden = {}
    visitados = set()
    padres[origen] = None
    orden[origen] = 0
    visitados.add(origen)
    _dfs(grafo, origen, visitados, padres, orden)
    return padres, orden


def recorrido_dfs_completo(grafo):
    visitados = set()
    padres = {}
    orden = {}
    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            padres[v] = None
            orden[v] = 0
            _dfs(grafo, v, visitados, padres, orden)
    return padres, orden


def reconstruir_camino(padres, destino):
    recorrido = []
    while destino is not None:
        recorrido.append(destino)
        destino = padres[destino]
    return recorrido[::-1]


if __name__ == "__main__":
    padres, orden = bfs(fronteras, "ARG")
    #print(padres)
    #print(orden)
    print(" -> ".join(reconstruir_camino(padres, "ECU")))

