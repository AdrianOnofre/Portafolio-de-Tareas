decimal = int(input())
resultado = ""
cociente = decimal
while cociente != 1:
    residuo = cociente % 2
    cociente = cociente // 2
    resultado = resultado + str(residuo)
resultado = resultado + str(cociente)
resultado = resultado[::-1]
print(resultado)


