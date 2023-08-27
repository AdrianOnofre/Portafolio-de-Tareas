def Bindec(n):
    S = 0
    i = 0
    print('El binario', n, end = ' ')
    while (n >= 1) :
        d = n % 10
        n = int(n / 10)
        S = S + d * pow(2, i)
        i = i + 1

    print('corresponde al numero', S)

def DecBin(n):
    d = []
    print('El numero', n, end=' ')
    while n >= 1:
        d.append(n % 2)
        n = int(n / 2)

    S = d[::-1]

    print('corresponde al binario ', end= '')
    [print(k,end='') for k in S]

valor = int(input("Ingrese un valor: "))
opcion = input("¿Desea convertir a binario (bi) o a decimal (de)? ")

if opcion == 'bi':
    resultado = DecBin(valor)
    tipo = 'binario'
elif opcion == 'de':
    resultado = Bindec(valor)
    tipo = 'decimal'
else:
    print("Opcion no válida")

    exit()
