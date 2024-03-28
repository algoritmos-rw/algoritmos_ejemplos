package main

import "fmt"

func ordenar_por(arr []int, criterio func(int) int) []int {
	frecuencias := make([]int, 10)
	for _, elem := range arr {
		frecuencias[criterio(elem)]++
	}
	acum := make([]int, 10)
	for i := 1; i < len(acum); i++ {
		acum[i] = acum[i-1] + frecuencias[i-1]
	}
	final := make([]int, len(arr))
	for _, elem := range arr {
		final[acum[criterio(elem)]] = elem
		acum[criterio(elem)]++
	}
	return final
}

func ordenar(arr []int) []int {
	arr = ordenar_por(arr, func(elem int) int { return elem / 10 % 10 })
	arr = ordenar_por(arr, func(elem int) int { return elem / 100 })
	arr = ordenar_por(arr, func(elem int) int { return elem % 10 })
	return arr
}

func main() {
	arr := [8]int{122, 369, 332, 180, 486, 349, 326, 101}
	fmt.Println(ordenar(arr[:]))
}
