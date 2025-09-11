
#include <stdlib.h>

/*
	Interfaz de un vector dinámico de enteros.
	Las posiciones del vector se numeran desde 0.
*/

struct vector_din;
typedef vector_din vector_din_t;

// Post: Crea un vector dinámico de enteros. Devuelve un puntero a un vector vacío.
//   	Al terminar de usarlo este vector debe ser destruido con vec_destruir().
//   	Devuelve NULL si no se pudo crear el vector.
vector_din_t* vec_crear();


// Pre: `vec` fue creado usando vec_crear().
// Post: Dedinuye el vector.
void vec_destruir(vector_din_t* vec);

// Pre: `vec` fue creado usando vec_crear().
// Post: Agrega una enteros al final del vector.
//   	Devuelve true si se pudo agregar, false en caso contrario.
bool vec_guardar(vector_din_t* vec, int elemento);

// Pre: `vec` fue creado usando vec_crear().
// Post: Devuelve un puntero elemento en la posición `pos` del vector.
//   	Si `pos` es inválida, devuelve NULL.
//   	Una posición es inválida si es mayor o igual al largo del vector.
int* vec_obtener(vector_din_t* vec, size_t pos);

// Pre: `vec` fue creado usando vec_crear().
// Post: Devuelve la cantidad de elementos en el vector.
size_t vec_largo(vector_din_t* vec);

// Pre: `vec` fue creado usando vec_crear().
// Post: Imprime los elementos del vector en orden.
void vec_imprimir(vector_din_t* vec);
