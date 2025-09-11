# 6.1 a)

# def imprimir_primeros_dos(string):
#     print(cadena[:2])

# b

# def imprimir_ultimos_tres(string):
#     print(cadena[-3:])


# #c

# def imprimir_cada_dos(cadena):
#     print(cadena[::2])


# 6.2 #a


def insertar_caracter(cadena, separador):
    # join(): Le paso un iterable y un caracter y me junta todos los elementos del iterable separados por ese caracter

    aux = []

    for c in cadena:
        aux.append(c)
    return separador.join(aux)


# b
def reemplazar_espacios(cadena, caracter):
    aux = ""
    for c in cadena:
        if c == " ":
            aux += caracter
        else:
            aux += c
    # Tambien se puede hacer con split() y join()


# c
def reemplazar_digitos(cadena, caracter):
    aux = ""
    for c in cadena:
        if c.isdigit():
            aux += caracter
        else:
            aux += c
    return aux


# Eliminar elementos en posicion par


# def eliminar_pares(list):
#     # Uso range porque me interesa la posicion y no el elemento

#     # for i in range(len(list)):
#     #     if i % 2 == 0:
#     #         list.pop(i)
#     # Esto itera la lista mientras la modificamos =>IndexError

#     i = 0

#     while i < len(list):
#         list.pop(i)
#         i += 1

# 6.5 a)

# def abreviar(string):
#     aux = ""
#     string_sep = cadena.split(" ")

#     for palabra in string_sep:
#         aux+= palabra[0]
#     return aux


# 7.10


# def sumar_matrices(m1, m2):
#     aux = []

#     for i, fila in enumerate(m1):
#         nueva_fila = []
#         for j, _columna in enumerate(m2):
#             nueva_fila.append(m1[i][j] + m2[i][j])
#         aux.append(nueva_fila)
#     return aux


# 7.11


def plegar(frase, n):
    palabras = frase.split(" ")

    resultado = []

    aux = " "

    for palabra in palabras:
        #aux +=  " " + palabra
