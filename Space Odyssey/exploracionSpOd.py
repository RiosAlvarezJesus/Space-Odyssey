import random
import entradaysalidaSpOd

def crear_mapa(n):
    """Crea la matriz cuadrada que será el mapa del juego con
    la dimensión n pasada como parámetro, y la devuelve"""
    MAPA = []
    for i in range (n):
        FILA = []
        for j in range(n):
            FILA.append(random.randint(1,20))
        MAPA.append(FILA)
    MAPA[3][4]=0 ##asignación de habitación inicial
    MAPA[7][5]=21 ##asignación de habitación de jefe
    return MAPA

def escoger_sala(posicion,MAPA,n):
    """Pasando como parámetro la matriz del mapa, la posición y la n, muestra los posibles
    movimientos y cambia la posición de acuerdo a la dirección introducida por teclado,
    devolviendo la nueva posición"""
    print("Estás en la sala",str(posicion[0]+1)+", "+str(posicion[1]+1))
    entradaysalidaSpOd.posibles_movimientos(posicion,n)
    posicion = entradaysalidaSpOd.cambiar_sala(posicion,n)
    return posicion