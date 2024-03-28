from ejemplos import fronteras
from grafo import Grafo
from heap import Heap
from union_find import UnionFind
import random


def mst_prim(grafo):
    v = random.choice(grafo.keys())
    visitados = set()
    visitados.add(v)
    q = Heap()
    for w in grafo.adyacentes(v):
        q.encolar((v, w), grafo.peso(v, w))
    arbol = Grafo(es_dirigido=False, lista_vertices=grafo.obtener_vertices())
    while not q.esta_vacio():
        (v, w), peso = q.desencolar()
        if w in visitados:
            continue
        arbol.agregar_arista(v, w, peso)
        visitados.add(w)
        for x in grafo.adyacentes(w):
            if x not in visitados:
                q.encolar((w, x), grafo.peso(w, x))
    return arbol


def obtener_aristas(grafo):
    aristas = []
    visitados = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            if w not in visitados:
                aristas.append((v, w, grafo.peso(v, w)))
        visitados.add(v)
    return aristas


PESO = 2


def mst_kruskal(grafo):
    conjuntos = UnionFind(grafo.obtener_vertices())
    aristas = sorted(obtener_aristas(grafo)) # ordeno de menor a mayor por peso de las aristas
    arbol = Grafo(False, grafo.obtener_vertices())
    for a in aristas: # > O(E log V)
        v, w, peso = a
        if conjuntos.find(v) == conjuntos.find(w):
            continue
        arbol.arista(v, w, peso)
        conjuntos.union(v, w)
    return arbol

