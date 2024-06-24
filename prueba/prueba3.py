import funciones3 as fn
#importando funciones
pedidos = []

while True:
    #menu principal
    print("Bienvenidos a Gaxplosive")
    print("***********************")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        print()
        if opcion == 1:
            fn.registrar_Pedido(pedidos)
            print()
        elif opcion == 2:
            fn.listar_Pedidos(pedidos)
            print("listado pedidos: ")
        elif opcion == 3:
            fn.imprimir_Hoja_Ruta(pedidos)
            print()
        elif opcion == 4:
            print("saliendo.....")
            break
        else:
            print("Opción no válida, intente nuevamente")
    except ValueError:
        print("error, ingrese opcion valida")

    