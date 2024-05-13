def mostrar_estadisticas(vida,vida_maxima,ataque,defensa,inteligencia,arma,armadura,dinero):
    """Tras pasar las estadísticas del jugador como parámetros, las imprime en pantalla"""
    print("\nVida: ",vida,"/",vida_maxima,"\nAtaque: ",ataque,"            Defensa: ",defensa,"     Inteligencia: ",inteligencia,sep="")
    print("Daño de arma: ",arma[1],"-",arma[2],"    Armadura: ",armadura[1],"    Créditos: ",dinero,sep="")

def avisar_jefe(vida,enemigo,vida_enemigo):
    """Pasando como parámetro la vida, el enemigo y la vida_enemigo, imprime el aviso
    de que el jugador se encuentra en la sala del jefe, y si comienza el combate no podrá huir"""
    print("Has llegado a la sala de mandos, donde se encuentra el corruptor")
    print("Ahora mismo está aletargado así que puedes aprovechar para irte y equiparte mejor, pero si lo atacas se despertará y no podrás escapar")
    print("Tienes",vida,"puntos de vida")
    print("El", enemigo[0] ,"tiene",vida_enemigo,"puntos de vida")

def mostrar_vida(vida,enemigo,vida_enemigo):
    """Pasando como parámetro la vida, el enemigo y la vida_enemigo, imprime la vida del jugador
    y la vida del enemigo"""
    print("\nTienes",vida,"puntos de vida")
    print("El/la",enemigo[0],"tiene",vida_enemigo,"puntos de vida")

def posibles_movimientos(posicion,n):
    """Indica los posibles movimientos a partir de la posición pasada como parámetro, para no pasarse
    de los límites. También se pasa la dimnesión (n) como parámetro para hallar los límites"""
    if(posicion[0] != 0):
        print("Puedes moverte hacia el Norte (Pulsa N)")
    if(posicion[0] != n-1):
        print("Puedes moverte hacia el Sur (Pulsa S)")
    if(posicion[1] != 0):
        print("Puedes moverte hacia el Oeste (Pulsa O)")
    if(posicion[1] != n-1):
        print("Puedes moverte hacia el Este (Pulsa E)")

def cambiar_sala(posicion,n):
    """Cambia la posición pasada como parámetro y la devuelve actualizada,
    según la dirección que se reciba por teclado(N/S/E/O)"""
    movimiento_correcto = False
    while(movimiento_correcto == False):
        movimiento = input ("Escribe la dirección en la que quieres moverte: ")
        if((movimiento == "N" and posicion[0] != 0)or(movimiento == "n" and posicion[0] != 0)):
            posicion[0] -= 1
            movimiento_correcto = True
        elif((movimiento == "N" and posicion[0] == 0)or(movimiento == "n" and posicion[0] != 0)):
            print("No puedes ir hacia el Norte")
        elif((movimiento == "S" and posicion[0] != n-1)or(movimiento == "s" and posicion[0] != n-1)):
            posicion[0] += 1
            movimiento_correcto = True
        elif((movimiento == "S" and posicion[0] == n-1)or(movimiento == "s" and posicion[0] == n-1)):
            print("No puedes ir hacia el Sur")
        elif((movimiento == "E" and posicion[1] != n-1)or(movimiento == "e" and posicion[1] != n-1)):
            posicion[1] += 1
            movimiento_correcto = True
        elif((movimiento == "E" and posicion[1] == n-1)or(movimiento == "e" and posicion[1] == n-1)):
            print("No puedes ir hacia el Este")
        elif((movimiento == "O" and posicion[1] != 0)or(movimiento == "o" and posicion[1] != 0)):
            posicion[1] -= 1
            movimiento_correcto = True
        elif((movimiento == "O" and posicion[1] == 0)or(movimiento == "o" and posicion[1] == 0)):
            print("No puedes ir hacia el Oeste")
    print("\nEstás en la sala",str(posicion[0]+1)+", "+str(posicion[1]+1))
    return posicion


def escoger_clase():
    """Muestra las clases disponibles y recibe por teclado la que el jugador escoja,
    retornando las nuevas estadísticas según la clase escogida"""
    clase = input ("Escoge tu clase:        Soldado(S)     Acorazado(A)        Científico(C) ")
    while(clase != "S" and clase != "s" and clase != "A" and clase != "a" and clase != "C" and clase != "c"):
        clase = input ("Escoge tu clase:        Soldado(S)     Acorazado(A)        Científico(C) ")
    if(clase == "S" or clase == "s"):
        vida_maxima = 100
        vida = 100
        ataque = 3
        defensa = 1
        inteligencia = 10
        clase = "Soldado"
        print("Has escogido al soldado")
    if(clase == "A" or clase == "a"):
        vida_maxima = 120
        vida = 120
        ataque = 1
        defensa = 3
        inteligencia = 10
        clase = "Acorazado"
        print("Has escogido al acorazado")
    if(clase == "C" or clase == "c"):
        vida_maxima = 100
        vida = 100
        ataque = 1
        defensa = 1
        inteligencia = 15
        clase = "Científico"
        print("Has escogido al científico")
    return vida_maxima,vida,ataque,defensa,inteligencia,clase