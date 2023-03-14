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

turno_1 = True
jugador_1 = " "
jugador_2 = " "
turno = 0

imprimir_tablero(tablero)
while turno < 9:
    if jugador_1 == " ":
        print("Nombre de jugador 1 (x)")
        jugador_1 = input()
        print("Nombre de jugador 2 (o)")
        jugador_2 = input()
    else:
        if turno_1:
            print(jugador_1 + ", elegí una posición")
        else:
            print(jugador_2 + ", elegí una posición")
        jugada = int(input())