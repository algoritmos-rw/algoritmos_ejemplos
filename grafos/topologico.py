from ejemplos import correlativas
from cola import Cola
from pila import Pila


def grados_entrada(grafo):
    g_ent = {}
    for v in grafo:
        g_ent[v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            g_ent[w] += 1
    return g_ent


def topologico_grados(grafo):
    g_ent = grados_entrada(grafo)
    q = Cola()
    resultado = []
    for v in grafo: # O(V)
        if g_ent[v] == 0:
            q.encolar(v)

    while not q.esta_vacia():
        v = q.desencolar()
        resultado.append(v)
        for w in grafo.adyacentes(v):
            g_ent[w] -= 1
            if g_ent[w] == 0:
                q.encolar(w)
    return resultado


def _dfs(grafo, v, visitados, pila):
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            _dfs(grafo, w, visitados, pila)
    pila.apilar(v)


def topologico_dfs(grafo):
    visitados = set()
    pila = Pila()
    for v in grafo:
        if v not in visitados:
            visitados.add(v)
            _dfs(grafo, v, visitados, pila)
    return pila_a_lista(pila)


def pila_a_lista(pila):
    lista = []
    while not pila.esta_vacia():
        lista.append(pila.desapilar())
    return lista


if __name__ == "__main__":
    print(topologico_dfs(correlativas))
