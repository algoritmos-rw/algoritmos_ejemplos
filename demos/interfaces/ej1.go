package main

import (
	"fmt"
	"interfaces/puerta"
)

func jugarConLaPuerta(puerta puerta.Puerta) {
	fmt.Println(puerta.EstaAbierta())
	puerta.Abrir()
	fmt.Println(puerta.EstaAbierta())
	puerta.Abrir()
	fmt.Println(puerta.EstaAbierta())
	puerta.Cerrar()
	fmt.Println(puerta.EstaAbierta())
}

func main() {
	fmt.Println("Holis")
	p := puerta.CrearMiImplementacionDePuerta()
	jugarConLaPuerta(p)
}
