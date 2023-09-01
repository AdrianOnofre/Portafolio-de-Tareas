def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def accion1():
    print('Has elegido la opción 1')
    decimal = int(input("Ingrese un número decimal: "))
    resultado = ""
    cociente = decimal
    while cociente != 1:
        residuo = cociente % 2
        cociente = cociente // 2
        resultado = resultado + str(residuo)
    resultado = resultado + str(cociente)
    resultado = resultado[::-1]
    print("El número en binario es:", resultado)


def accion2():
    print('Has elegido la opcion 2')
    binario = input("Ingresa un numero binario: ")
    def binario_a_decimal(binario):
        posicion = 0
        decimal = 0
        binario = binario[::-1]
        for digito in binario:
            multiplicador = 2**posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal
    decimal = binario_a_decimal(binario)
    print("El número en decimal es:", decimal)

def accion3():
    print('Has elegido la opcion 3')
    numero1_como_cadena = input("Escribe un número: ")
    numero2_como_cadena = input("Escribe el otro número: ")
    numero1 = float(numero1_como_cadena)
    numero2 = float(numero2_como_cadena)
    multiplicacion = numero1 * numero2
    print("La multiplicacion es:", multiplicacion)

def accion4():
    print('Has elegido la opcion 4')
    numero1_como_cadena = input("Escribe un número: ")
    numero2_como_cadena = input("Escribe el otro número: ")
    numero1 = float(numero1_como_cadena)
    numero2 = float(numero2_como_cadena)
    suma = numero1 + numero2
    print("La suma es:", suma)

def accion5():
    print('Has elegido la opcion 5')
    numero1_como_cadena = input("Escribe un número: ")
    numero2_como_cadena = input("Escribe el otro número: ")
    numero1 = float(numero1_como_cadena)
    numero2 = float(numero2_como_cadena)
    resta = numero1 - numero2
    print("La resta es:", resta)

def accion6():
    print('Has elegido la opcion 6')
    numero1_como_cadena = input("Escribe un número: ")
    numero2_como_cadena = input("Escribe el otro número: ")
    numero1 = float(numero1_como_cadena)
    numero2 = float(numero2_como_cadena)
    division = numero1 / numero2
    print("La division es:", division)

def salir():
    print('Saliendo')


def menu_principal():
    opciones = {
        '1': ('Convertir de decimal a binario', accion1),
        '2': ('Convertir de binario a decimal', accion2),
        '3': ('Multiplicar', accion3),
        '4': ('Suma', accion4),
        '5': ('Resta', accion5),
        '6': ('Division', accion6),
        '7': ('Salir', salir)
    }
    
    generar_menu(opciones, '7')


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


if __name__ == '__main__':
    menu_principal()
    
import sys
sys.exit()