package arboles

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestProbemos(t *testing.T) {
	izq := &Arbol{&Arbol{nil, nil, "L"}, &Arbol{nil, nil, "K"}, "C"}
	der := &Arbol{nil, &Arbol{&Arbol{nil, nil, "D"}, nil, "W"}, "H"}
	arbolito := &Arbol{izq, der, "A"}
	require.EqualValues(t, 4, arbolito.Altura())
	require.EqualValues(t, 4, arbolito.NodosInternos())
}
