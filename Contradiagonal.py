matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 10, 11, 12], [13, 14, 15, 16]]

def DiagonalPrincipal(matriz):
    resultado = 0
    for i in range(4):
        resultado += matriz[i][i]
    return resultado

def DiagonalPrincipalMult(matriz):
    resultado = 1
    for i in range(4):
        resultado *= matriz[i][i]
    return resultado

def Contradiagonal(matriz):
    resultado = 0
    for i in range(4):
        resultado += matriz[i][3 - i]
    return resultado

def ContradiagonalMult(matriz):
    resultado = 1
    for i in range(4):
        resultado *= matriz[i][3 - i]
    return resultado

print("Suma De La Diagonal Principal:", DiagonalPrincipal(matriz))
print("Multiplicación De La Diagonal Principal:", DiagonalPrincipalMult(matriz))
print("Suma De La Contradiagonal:", Contradiagonal(matriz))
print("Multiplicación De La Contradiagonal:", ContradiagonalMult(matriz))