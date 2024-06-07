tablero = ["   " for i in range(9)]
def suerte():
    for i in range(3):
        fila = f"|  {tablero[i*3]} |  {tablero[i*3+1]} |  {tablero[i*3+2]}  |"
        print(fila)
def jugadores(turno):
    if turno == "x":
        number = 1
    else:
        number = 2
    print(f"\n Turno del jugador # {number}")
    while True:
        try:
            posicion = int(input(f"Ingrese la posicion(1-9)\n ").strip())
            if posicion >= 1 and posicion <= 9:
                if tablero[posicion - 1] == "   ":
                    tablero[posicion - 1] =turno + "  "
                    break
                else:
                    print("Posicion ocupada, intentalo otra vez \n")
            else:
                print("movimiento invalido, Ingrese un numero entre 1 y 9\n")
        except ValueError:
            print("movimiento invalido\n")
def campeon(icono):
    icono=icono+"  "
    if (
        (tablero[0] == icono and tablero[1] == icono and tablero[2] == icono)
        or (tablero[3] == icono and tablero[4] == icono and tablero[5] == icono)
        or (tablero[6] == icono and tablero[7] == icono and tablero[8] == icono)
        or (tablero[0] == icono and tablero[3] == icono and tablero[6] == icono)
        or (tablero[1] == icono and tablero[4] == icono and tablero[7] == icono)
        or (tablero[2] == icono and tablero[5] == icono and tablero[8] == icono)
        or (tablero[0] == icono and tablero[4] == icono and tablero[8] == icono)
        or (tablero[2] == icono and tablero[4] == icono and tablero[6] == icono)
    ):
        suerte()
        return True
    else:
        return False
def empate():
        if "   " not in tablero:
            suerte()
            return True
        else:
            return False
        
while True:
    suerte()
    jugadores("x")
    if campeon("x"):
        print("Gano el jugador 1")
        break
    elif empate():
        print("Estamos Empate")
        break
    suerte()
    jugadores("o")
    if campeon("o"):
        print("Gano el jugador 2")
        break
    elif empate():
        print("Estamos Empate")
        break
