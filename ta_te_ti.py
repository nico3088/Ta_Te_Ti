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

def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = "X"
    else:
        simbolo = "O"
    
    if posicion == 1:
        if tablero[4][0] == " ":
            tablero[4][0] == simbolo
            return 0
        else:
            return "Ese lugar está ocupado."
    elif posicion == 2:
        if tablero[4][2] == " ":
            tablero[4][2] == simbolo
            return 0
        else:
            return "Ese lugar está ocupado."
    elif posicion == 3:
        if tablero[4][4] == " ":
            tablero[4][4] == simbolo
            return 0
        else:
            return "Ese lugar está ocupado."
    elif posicion == 4:
        if tablero[2][0] == " ":
            tablero[2][0] == simbolo
            return 0
        else:
            return "Ese lugar está ocupado."
    elif posicion == 5:
        if tablero[2][2] == " ":
            tablero[2][2] == simbolo
            return 0
        else:
            return "Ese lugar está ocupado."    
    elif posicion == 6:
        if tablero[2][4] == " ":
         tablero[2][4] == simbolo
         return 0
        else:
            return "Ese lugar está ocupado."

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