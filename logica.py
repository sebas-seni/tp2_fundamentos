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


def pedir_opcion():
    while True:
        opcion_elegida = input()

        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if 1 <= opcion_elegida < 7:
                return opcion_elegida
            elif opcion_elegida == 7:
                print(constantes.MSG_FIN)
                break

        print(constantes.MSG_INPUT_INVALIDO)
        imprimir_menu_principal()


# Implementar crear_cuenta (acordarse de que "**" retrocede al menu principal)
