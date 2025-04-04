package dyc_pico

func PosicionPico(arr []int, ini, fin int) int {
	if ini == fin {
		return ini
	}

	medio := (ini + fin) / 2

	// Encontré la posición del pico.
	if arr[medio] > arr[medio+1] && arr[medio] > arr[medio-1] {
		return medio
	}
	// Si no encontré el pico evalúo en que extremo estoy,
	// o bien "en subida" o "en bajada".
	if arr[medio] > arr[medio+1] {
		return PosicionPico(arr, ini, medio)
	} else {
		return PosicionPico(arr, medio+1, fin)
	}
}

// Justificación de complejidad

// Como es un algoritmo de DyC podemos calcular su complejidad
// utilizando el Teorema Maestro ya que cumple con la siguiente ec.
// de recurrencia:

// T(n) = A * T(n / B) + O(n ** c) donde:

// A -> 1 (Cantidad de llamados recursivos)
// B -> 2 (Proporción del tamaño original con el que se ejecuta cada llamado)
// C -> 0 => O(n ** c) = O(1) (El costo de juntar las partes / cantidad de trabajo entre llamados)

// OJO con el valor de C. Suele ocurrir que ponen C = 1 queriendo decir que en cada llamado se
// realiza una cantidad de trabajo constante -> O(1). Como C es un exponente poner C = 1
// implica que la cantidad de trabajo es lineal, lo cuál cambia la complejidad y, en este caso,
// está mal.

// Como log_B(A) = C => O(n ** C * log_B(n)) => O(log n).
// Entonces, la complejidad del algoritmo es O(log n) siendo n la cantidad de elementos en el
// arreglo.
