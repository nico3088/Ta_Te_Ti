tablero = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "]
]

def imprimir_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) -1:
                print(fila[i], end="\n")
            else:
                print(fila[i], end="  ")

imprimir_tablero(ta)