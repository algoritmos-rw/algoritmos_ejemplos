from ejemplos import catedra, catedra_dir
from pila import Pila
from grafo import Grafo


def dfs_puntos_articulacion(grafo, v, visitados, padre, orden, mas_bajo, ptos, es_raiz):
    hijos = 0
    mas_bajo[v] = orden[v]
    for w in grafo.adyacentes(v):
        if w not in visitados:
            hijos += 1
            orden[w] = orden[v] + 1
            padre[w] = v
            visitados.add(w)
            dfs_puntos_articulacion(grafo, w, visitados, padre, orden, mas_bajo, ptos, es_raiz=False)

            # Lo siguiente se ejecuta una vez ya aplicado a W, y recursivamente a sus hijos
            if mas_bajo[w] >= orden[v] and not es_raiz:
                # No hubo forma de pasar por arriba a este vertice, es punto de articulacion
                # se podría agregar como condicion "and v not in ptos" (ya que podria darse por mas de una rama)
                ptos.add(v)
            # Al volver me quedo con que puedo ir tan arriba como mi hijo, si es que me supera
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
        elif padre[v] != w: # evitamos considerar a la arista con el padre como una de retorno
            # Si es uno ya visitado, significa que puedo subir (si es que no podia ya ir mas arriba)
            mas_bajo[v] = min(mas_bajo[v], orden[w])

    if es_raiz and hijos > 1:
        ptos.add(v)


def puntos_articulacion(grafo):
    origen = grafo.random()
    origen = "A"
    puntos_articulacion = set()
    dfs_puntos_articulacion(grafo, origen, {origen}, {origen: None}, {origen: 0}, {}, puntos_articulacion, True)
    return puntos_articulacion


def dfs_cfc(grafo, v, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global):
    orden[v] = mas_bajo[v] = contador_global[0]
    contador_global[0] += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            # llamamos recursivamente
            dfs_cfc(grafo, w, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global)
        if w in apilados:
            # Nos tenemos que fijar que este entre los apilados y que no estemos viendo a un vertice visitado
            # en otro dfs hecho antes --> no son parte de la misma CFC porque habrian sido visitados en el mismo DFS
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])

    if orden[v] == mas_bajo[v]:
        # Se cumple condicion de cierre de CFC, armamos
        nueva_cfc = []
        while True: # porque python no tiene un do-while
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfcs.append(nueva_cfc)


def cfcs_grafo(grafo):
    resultados = []
    visitados = set()
    for v in grafo:
        if v not in visitados:
            dfs_cfc(grafo, v, visitados, {}, {}, Pila(), set(), resultados, [0])
    return resultados


def main():
    #print(puntos_articulacion(catedra))
    g = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H"])
    g.arista("A", "G")
    g.arista("A", "E")
    g.arista("A", "B")
    g.arista("A", "F")
    g.arista("E", "B")
    g.arista("B", "F")
    g.arista("B", "C")
    g.arista("B", "D")
    g.arista("C", "D")
    g.arista("D", "H")
    #print(puntos_articulacion(g))
    print(cfcs_grafo(catedra_dir))


if __name__ == "__main__":
    main()

