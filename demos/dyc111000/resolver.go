package main

import "fmt"

func unosYCerosRec(arr []int, inicio int, fin int) int {
	if inicio == fin {
		return inicio
	}

	medio := (inicio + fin) / 2
	if arr[medio] == 0 && arr[medio-1] == 1 {
		return medio
	}
	if arr[medio] == 1 {
		return unosYCerosRec(arr, medio+1, fin)
	} else {
		return unosYCerosRec(arr, inicio, medio)
	}
}

func unosYCeros(arr []int) int {
	if len(arr) == 0 {
		return -1
	}
	if arr[0] == 0 {
		return 0
	} else if arr[len(arr)-1] == 1 {
		return -1
	}
	return unosYCerosRec(arr, 0, len(arr)-1)
}

func main() {
	fmt.Println(unosYCeros([]int{}))
}
