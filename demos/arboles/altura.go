package arboles

type Arbol struct {
	izq  *Arbol
	der  *Arbol
	dato string
}

func maximo(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func (ab *Arbol) Altura() int {
	if ab == nil {
		return 0
	}

	return 1 + maximo(ab.izq.Altura(), ab.der.Altura())
}

func (ab *Arbol) NodosInternos() int {
	if ab == nil {
		return 0
	}
	if ab.izq == nil && ab.der == nil {
		return 0
	}
	return 1 + ab.izq.NodosInternos() + ab.der.NodosInternos()
}
