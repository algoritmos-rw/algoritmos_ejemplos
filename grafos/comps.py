def unir_amigues(grafo):
    pto_articulacion = pto_articulacion(grafo)
    adyacentes_pto = grafo.adyacentes(pto_articulacion)
    grafo.eliminar_vertice(pto_articulacion)
    comps = vertices_x_componente(grafo)
    for (i = 0; i < len(comps); i++):
            for (j = i + 1; j < len(comps); j++):
                primero = random(comps[i])
                segundo = random(comps[j])
                grafo.arista(primero, segundo)
    grafo.agregar_vertice(pto_articulacion)
    for v in adyacentes_pto:
        grafo.arista(pto_articulacion, v)

