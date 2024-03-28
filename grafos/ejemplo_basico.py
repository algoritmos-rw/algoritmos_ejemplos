from ejemplos import fronteras, correlativas
from grafo import Grafo


def obtener_aristas(grafo): # O(V + E)
    resultado = []
    visitados = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            if w not in visitados:
                resultado.append((v, w))
        visitados.add(v)
    return resultado


def grados(grafo):
    gr = {}
    for v in grafo:
        gr[v] = len(grafo.adyacentes(v))
    return gr


def grados_salida(grafo):
    return grados(grafo)


def grados_entrada(grafo):
    gr_entrada = {}
    for v in grafo:
        gr_entrada[v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            gr_entrada[w] += 1
    return gr_entrada


def placeholder_hacer_ejercicio_1_guia():
    pass


def traspuesto(grafo):
    g_t = Grafo(es_dirigido=True)
    for v in grafo:
        g_t.agregar_vertice(v)
    for v in grafo:
        for w in grafo.adyacentes(v):
            g_t.arista(w, v)
    return g_t


def placeholder_hacer_ejercicio_16_guia():
    pass


# Otros ejercicios que pueden hacer: 2, 12, 13, 14, 17, 21 (dejar para ver en clase)


def main():
    print(traspuesto(correlativas))


if __name__ == "__main__":
    main()
