import constantes


def imprimir_menu_principal():
    opciones = [
        "Crear cuenta",
        "Ingresar dinero",
        "Transferir dinero",
        "Otorgar préstamo",
        "Pagar préstamo",
        "Ver resumen",
        "Salir",
    ]

    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}) {opcion}")


def guardar_opcion():

    opcion_elegida = input()

    if opcion_elegida.isdigit():
        return int(opcion_elegida)
    else:
        return None


def gestionar_errores():
    opcion_guardada = guardar_opcion()

    # Prox: Mientras el valor ingresado no sea correcto, se debe mostrar el menu principal
    # Si el input es 7, finaliza el programa

    if (
        (type(opcion_guardada) is not int)
        or (opcion_guardada < 1)
        or (opcion_guardada > 7)
    ):
        print(constantes.MSG_INPUT_INVALIDO)


# def finalizar_programa():
#     print(constantes.MSG_FIN) if guardar_opcion == 7 else
