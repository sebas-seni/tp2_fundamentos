#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "reporte.h"

bool validar_cant_argumentos(int argc) {
    return (argc == 2 || argc == 3);      
}

bool validar_arch_entrada(char *nombre_archivo) {
    FILE *archivo = fopen(nombre_archivo, "r");
    if (archivo == NULL) {
        fprintf(stderr, "Error al abrir el archivo %s.\n", nombre_archivo);
        return false;
    }
    fprintf(stderr, "Archivo de entrada %s validado correctamente.\n", nombre_archivo);
    fclose(archivo);
    return true;
}
    //TODO: Detectar errores de formato, etc. Eso quizas se haga en otra funcion


int main(int argc, char *argv[]) {

    if (!validar_cant_argumentos(argc)) {
        fprintf(stderr, "Cantidad de argumentos incorrecta. Ingrese 1 (uno) ó 2 (dos) archivos. \n");
        return 1;
    } 
    
    char *nombre_archivo = argv[1];
    if (validar_arch_entrada(nombre_archivo)) {
        // Si se pasa un segundo argumento, se asume que es el archivo de salida    
        fprintf(stderr, "Archivo de entrada %s validado correctamente.\n", argv[1]);
    }

    return 0;
}