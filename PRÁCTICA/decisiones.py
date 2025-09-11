# 4.1 a)

# def es_par(n):
#     return n % 2 == 0

# print(es_par(90))


# 4.2

# def calcular_val_abs(n):
#     if n > 0:
#         return n
#
#     return -n

# print(calcular_val_abs(-10))


# 4.3

# def imprimir_matriz_identidad(dimension):
#     for i in range(dimension):
#         for j in range(dimension):
#             if i == j:
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")

#         print()

# imprimir_matriz_identidad(2)


# 4.5 a)


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 != 0)


# print(es_bisiesto(2024))


# b)
# no hecha
# def devolver_dias_correspondientes(mes, anio):
#     if (mes == "febrero"):
#         if es_bisiesto:
#             return 29
#         else:
#             return 28
