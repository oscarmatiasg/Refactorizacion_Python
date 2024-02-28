def puntos_y_comentarios():
    while True:
        punto = input('Ingrese puntos de evaluación (1-5): ')
        if punto.isdecimal():
            punto = int(punto)
            if 1 <= punto <= 5:
                comentario = input('Ingrese un comentario: ')
                with open("data.txt", 'a') as archivo:
                    archivo.write(f'Puntos: {punto}, Comentario: {comentario}\n')
                break
            else:
                print('Por favor ingrese un valor entre 1 y 5.')
        else:
            print('Por favor ingrese un valor numérico para los puntos de evaluación.')

def mostrar_resultados():
    print('Resultados hasta ahora:')
    with open("data.txt", "r") as archivo:
        print(archivo.read())

def procesar_opcion(opcion):
    if opcion == 1:
        puntos_y_comentarios()
    elif opcion == 2:
        mostrar_resultados()
    elif opcion == 3:
        print('Saliendo...')
        exit()
    else:
        print('Por favor ingrese una opción del 1 al 3.')

while True:
    print('Seleccione una opción:')
    print('1: Ingresar puntos de evaluación y comentarios')
    print('2: Ver resultados hasta ahora')
    print('3: Salir')
    num = input()

    if num.isdecimal():
        num = int(num)
        procesar_opcion(num)
    else:
        print('Por favor ingrese una opción válida (1-3).')