package puerta

type mipuerta struct {
	abierta bool
}

type miOtraPuerta struct {
	estado int
}

func CrearMiImplementacionDePuerta() Puerta {
	return &mipuerta{abierta: false}
}

func CrearMiOtraImplementacionDePuerta() Puerta {
	return &miOtraPuerta{estado: 0}
}

func (puerta *mipuerta) Abrir() {
	puerta.abierta = true
}

func (puerta *mipuerta) Cerrar() {
	puerta.abierta = false
}

func (puerta *mipuerta) EstaAbierta() bool {
	return puerta.abierta
}

func (puerta *miOtraPuerta) Abrir() {
	puerta.estado = 0
}

func (puerta *miOtraPuerta) Cerrar() {
	puerta.estado = 1
}

func (puerta *miOtraPuerta) EstaAbierta() bool {
	return puerta.estado == 0
}
