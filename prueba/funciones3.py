comunas = ['valpo', 'vina', 'quilpue']
cilindro_5kg = 0
cilindro_15kg = 0
cilindro_45kg = 0

def registrar_Pedido(pedidos):
    global cilindro_5kg, cilindro_15kg, cilindro_45kg

    print("Complete los siguientes datos: ")
    nombre = input("Ingrese nombre y apellido del cliente: ")
    while True:
        comuna = input("Ingrese comuna del pedido (valpo, vina, quilpue): ").lower()
        if comuna in comunas:
            break
        else:
            print("Esta comuna no se encuentra en el radio de entrega, ingrese nuevamente su comuna")
    direccion = input("Ingrese direccion del cliente: ")

    while True:
        try:
            #sub menu para elegir cilindro 
            print("Cilindros Gaxplosive")
            print("--------------------")
            print("1. Cilindro 5kg")
            print("2. Cilindro 15kg")
            print("3. Cilindro 45kg")
            print("4. Salir")
            cilindros = int(input("Ingrese el tipo de cilindro que requiera: "))

            if cilindros == 1:
                try:
                    cantidad5 = int(input("Ingrese la cantidad solicitada: "))
                    cilindro_5kg += cantidad5
                except ValueError:
                    print("Error, ingrese cantidad nuevamente")
            elif cilindros == 2:
                try:
                    cantidad15 = int(input("Ingrese la cantidad solicitada: "))
                    cilindro_15kg += cantidad15
                except ValueError:
                    print("Error, ingrese cantidad nuevamente")
            elif cilindros == 3:
                try:
                    cantidad45 = int(input("Ingrese la cantidad solicitada: "))
                    cilindro_45kg += cantidad45
                except ValueError:
                    print("Error, ingrese cantidad nuevamente")
            elif cilindros == 4:
                break
            else:
                print("Opción no válida, seleccione nuevamente")
        except ValueError:
            print("Ingrese un dato válido")

    pedidos.append({
        'Cliente': nombre,
        'Direccion': direccion,
        'Comuna': comuna,
        'Cilindro_5kg': cilindro_5kg,
        'Cilindro_15kg': cilindro_15kg,
        'Cilindro_45kg': cilindro_45kg
    })

def listar_Pedidos(pedidos):
    print("Listado de pedidos")
    for pedido in pedidos:
        print(pedido)

def imprimir_Hoja_Ruta(pedidos):
    while True:
        elegirComuna = input("Ingrese la comuna deseada para imprimir la hoja de ruta (valpo, vina, quilpue), o ingrese '0' para imprimir todos los pedidos: ")

        if elegirComuna in comunas:
            imprimir = []
            for comuna in pedidos:
                if comuna['Comuna'] == elegirComuna:
                    imprimir.append(comuna)

            hojaDeRuta = f'HojaDeRuta-{elegirComuna}.txt'

            with open(hojaDeRuta, 'w') as archivo:
                archivo.write("Lista de pedidos\n")
                for pedido in imprimir:
                    archivo.write(f'{pedido}\n')
            break
        elif elegirComuna == '0':
            imprimir_Todos_Pedidos(pedidos)
            break
        else:
            print("Comuna fuera de rango, intente nuevamente o presione 0 para salir")

def imprimir_Todos_Pedidos(pedidos):
    hojaDeRuta = 'HojaDeRuta-Todos.txt'
    with open(hojaDeRuta, 'w') as archivo:
        archivo.write("Lista de todos los pedidos\n")
        for pedido in pedidos:
            archivo.write(f'{pedido}\n')