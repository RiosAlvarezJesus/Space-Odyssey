import random

def preguntar_eleccion(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia):
    """Pasando como parámetro la vida, el ataque, la defensa, el arma, el enemigo, la vida_enemigo,
    la armadura y la inteligencia, pregunta si huir o luchar. Si el jugador escoge huir,
    duelve -1, para que se identidique la respuesta en el módulo principal. Si escoge luchar,
    llama a la función luchar(), que actualiza la vida y la vida_enemigo, y las devuelve"""
    eleccion = input ("Escoge tu próxima acción: huir(H) o luchar(L) ")
    while(eleccion != "H" and eleccion != "huir" and eleccion != "h" and eleccion != "L" and eleccion != "luchar" and eleccion != "l"):
        eleccion = input ("Escoge tu próxima acción: huir(H) o luchar(L) ")
    if (eleccion == "H" or eleccion == "huir" or eleccion == "h"):
        print("Decides huir")
        return -1
    else:
        vida,vida_enemigo = luchar(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia)
        return vida,vida_enemigo

def preguntar_eleccion_jefe(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia):
    """De forma similar a la función preguntar_eleccion(), pasando como parámetro la vida, el ataque,
    la defensa, el arma, el enemigo, la vida_enemigo, la armadura y la inteligencia, solo permite
    pulsar cualquier tecla para continuar (para así crear una pausa entre cada turno del combate),
    llamando a la función luchar(), que que actualiza la vida y la vida_enemigo, y las devuelve"""
    input ("Pulsa cualquier tecla para continuar el combate ")
    vida,vida_enemigo = luchar(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia)
    return vida,vida_enemigo

def luchar(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia):
    """Pasando como parámetro la vida, el ataque, la defensa, el arma, el enemigo, la vida_enemigo,
    la armadura y la inteligencia, llama a la función calcular_daño_causado y lo muestra. En caso de
    no haber matado al enemigo, llama a la función calcular_daño_recibido, mostrándolo también y
    devolviendo la vida y la vida_enemigo. En caso de haber matado al enemigo lo muestra y devuelve
    directamente la vida y la vida_enemigo sin calcular el daño recibido"""
    vida_enemigo,daño_causado = calcular_daño_causado(arma,vida_enemigo,ataque,inteligencia)
    print("Haces",daño_causado,"de daño al enemigo")

    if(vida_enemigo > 0):
        vida,daño_recibido = calcular_daño_recibido(enemigo,vida,defensa,armadura)
        print("El enemigo te hace",daño_recibido,"de daño")
    else:
        print("Has matado al/a la",enemigo[0])

    return vida,vida_enemigo

def calcular_daño_causado(daños,vida,ataque,inteligencia):
    """Calcula, mediante la vida, el ataque y una lista con daño mínimo y máximo pasadas
    como parámetros, los daños causados (al azar entre máximo y mínimo más el ataque) y
    la vida restante tras los daños, y los devuelve"""
    probabilidad_critico = random.randint(1,100)
    if (probabilidad_critico <= inteligencia):
        print("Impacto crítico")
        daño = (random.randint(daños[1],daños[2])+ataque)*2
        vida = vida - daño
    else:
        daño = random.randint(daños[1],daños[2])+ataque
        vida = vida - daño
    return vida,daño

def calcular_daño_recibido(daños,vida,defensa,armadura):
    """Calcula, mediante la vida, la defensa y una lista con daño mínimo y máximo pasadas
    como parámetros, los daños recibidos (al azar entre máximo y mínimo, menos la defensa y la armadura)
    y la vida restante tras los daños, y los devuelve"""
    daño = random.randint(daños[1],daños[2])-defensa-armadura[1]
    if (daño < 0):
        daño = 0
    vida -= daño
    return vida,daño

def calcular_recompensa(enemigo):
    """Calcula y devuelve una cantidad de dinero al azar entre el máximo y el
    mínimo del enemigo pasado como parámetro"""
    dinero = random.randint(enemigo[4],enemigo[5])
    print("Obtienes",dinero,"créditos")
    return dinero