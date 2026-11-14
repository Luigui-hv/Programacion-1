import numpy as np
#Juego de 2 jugadores de "X" y "O" 
#---------------------------------------------
def mostrar_tablero(tablero):
    print("\n    1   2   3")

    for fila in range(3):
        print(f"{fila + 1}   " + " | ".join(tablero[fila]))

        if fila < 2:
            print("   ---+---+---")

    print()
#---------------------------------------------
def hay_ganador(tablero, jugador):
    # Revisar filas y columnas
    for i in range(3):
        if np.all(tablero[i, :] == jugador):
            return True

        if np.all(tablero[:, i] == jugador):
            return True

    # Diagonal principal
    if np.all(np.diag(tablero) == jugador):
        return True

    # Diagonal secundaria
    if np.all(np.diag(np.fliplr(tablero)) == jugador):
        return True

    return False
#---------------------------------------------
def pedir_jugada(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, fila [1-3]: "))
            columna = int(input("Columna [1-3]: "))

            if not (1 <= fila <= 3 and 1 <= columna <= 3):
                print("La fila y la columna deben estar entre 1 y 3.")
                continue

            fila -= 1
            columna -= 1

            if tablero[fila, columna] != " ":
                print("La casilla está ocupada. Elige otra.")
                continue

            return fila, columna

        except ValueError:
            print("Debes escribir números enteros.")
#----------------------------------------------------
# Proceso principal
#----------------------------------------------------
# Arreglo 2D: cada elemento guarda un carácter
tablero = np.full((3, 3), " ")
jugador = "X"
ganador = None

mostrar_tablero(tablero)

while True:
    fila, columna = pedir_jugada(tablero, jugador)
    tablero[fila, columna] = jugador

    mostrar_tablero(tablero)

    if hay_ganador(tablero, jugador):
        print(f"¡Ganó el jugador {jugador}!")
        ganador = jugador
        break

    if np.all(tablero != " "):
        print("¡Empate!")
        break

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

