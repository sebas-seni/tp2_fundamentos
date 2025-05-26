#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "reporte.h"

bool validar_cant_argumentos(int argc) {
    return (argc == 2 || argc == 3);      
}

bool validar_arch_entrada(char *nombre_archivo) {
    //Intentar abrir el archivo de entrada
    //Validar formato, etc
}

int main(int argc, char *argv[]) {

    if (!validar_cant_argumentos(argc)) {
        fprintf(stderr, "Cantidad de argumentos incorrecta. Ingrese 1 (uno) ó 2 (dos) archivos. \n");
        return 1;
    }

    return 0;
}