package puerta

type Puerta interface {

	// Abrir abre la puerta
	Abrir()

	// Cerrar cierra la puerta
	Cerrar()

	// EstaAbierta nos devuelve true si la puerta esta abierta, o false en caso contrario
	EstaAbierta() bool
}
