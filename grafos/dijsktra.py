from heap import Heap
from ejemplos import fronteras


def camino_minimo_dijkstra(grafo, origen, destino):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = float("inf")
    dist[origen] = 0
    padre[origen] = None
    q = Heap()
    q.encolar((0, origen))
    while not q.esta_vacio():
        _, v = q.desencolar()
        if v == destino:
            return padre, dist
        for w in grafo.adyacentes(v):
            distancia_por_aca = dist[v] + grafo.peso(v, w)
            if distancia_por_aca < dist[w]:
                dist[w] = distancia_por_aca
                padre[w] = v
                q.encolar((dist[w], w))
                # o: q.actualizar(w, dist[w])
    return padre, dist


def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v, w, grafo.peso(v, w)))
    return aristas


# Bellman-Ford
def camino_minimo_bf(grafo, origen):
    distancia = {}
    padre = {}
    for v in grafo:                     # O(V)
        distancia[v] = float("inf")
    distancia[origen] = 0
    padre[origen] = None
    aristas = obtener_aristas(grafo) # O(V + E)
    for i in range(len(grafo)): # for i:= 0; i < len(grafo); i++
        cambio = False
        for origen, destino, peso in aristas:
            if distancia[origen] + peso < distancia[destino]:
                cambio = True
                padre[destino] = origen
                distancia[destino] = distancia[origen] + peso
        if not cambio:
            return padre, distancia

    for v, w, peso in aristas:
        if distancia[v] + peso < distancia[w]:
            return None  # Hay un ciclo negativo (lanzar excep) panic(AAAAAAAAA)
    return padre, distancia


def main():
    p, d = camino_minimo_bf(fronteras, "ARG")
    print(p)
    print(d)


if __name__ == "__main__":
    main()
