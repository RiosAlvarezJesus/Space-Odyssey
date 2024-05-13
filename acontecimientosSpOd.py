import random

def sala_vacia():
    """Indica que la sala está vacía"""
    print("Estás en una sala vacía")

def obtener_arma(arma,inteligencia,ARMAS):
    """Pasando como parámetro el arma actual y la inteligencia, genera un arma al azar y,
    si la inteligencia del jugador es suficiente, permite decidir cogerla(retornándola) o
    mantener el arma acual(retornando esta), y si la inteligencia es insuficiente retorna el arma actual"""
    arma_nueva = ARMAS[random.randint(1,len(ARMAS)-1)]
    print("Encontraste un/una ",arma_nueva[0]," de daño ",arma_nueva[1],"-",arma_nueva[2],sep="")
    print("Tu arma actual es un/una ",arma[0], " de daño ",arma[1],"-",arma[2],sep="")
    if(inteligencia < arma_nueva[3]):
        print("No tienes inteligencia suficiente para usar este arma, requiere",arma_nueva[3],"de inteligencia")
        return arma
    else:
        eleccion = input ("¿Quieres cogerla(C) o mantener(M) tu arma actual? ")
        while(eleccion != "C" and eleccion != "c" and eleccion != "M" and eleccion != "m"):
            eleccion = input ("¿Quieres cogerla(C) o mantener(M) tu arma actual? ")
        if (eleccion == "C" or eleccion == "c"):
            print("Coges el/la",arma_nueva[0])
            return arma_nueva
        else:
            print("Te quedas con tu",arma[0])
            return arma


def obtener_armadura(armadura,ARMADURAS):
    """Pasando como parámetro la armadura actual, genera una armadura al azar y permite
    decidir cogerla(retornándola) o mantener la armadura acual(retornando esta)"""
    armadura_nueva = ARMADURAS[random.randint(1,len(ARMADURAS)-1)]
    print("Encontraste un/una",armadura_nueva[0],"de defensa",armadura_nueva[1])
    print("Tu armadura actual es un/una",armadura[0],"de defensa",armadura[1])
    eleccion = input ("¿Quieres cogerla(C) o mantener(M) tu armadura actual? ")
    while(eleccion != "C" and eleccion != "c" and eleccion != "M" and eleccion != "m"):
        eleccion = input ("¿Quieres cogerla(C) o mantener(M) tu arma actual? ")
    if (eleccion == "C" or eleccion == "c"):
        print("Coges el/la",armadura_nueva[0])
        return armadura_nueva
    else:
        print("Te quedas con tu",armadura[0])
        return armadura


def obtener_compañero(vida,vida_maxima,ataque,defensa,inteligencia,MAPA):##cambiar valores de compañeros
    """Pasando como parámetro la vida, el ataque, la defensa, la inteligencia y el mapa,
    permite escoger un compañero que modificará las estadísticas en función de la elección,
    y cambiará las salas del mapa que sean del mismo tipo a otras al azar,
    retornando todas las variables pasadas como parámetros junto con el compañero escogido"""
    print("Te encuentras con un grupo de personas que se ofrecen a ayudarte, pero solo puede acompañarte una, ya que un grupo demasiado grande atraería a los enemigos")
    eleccion = input ("Escoge a tu compañero:        Soldado(S)   Acorazado(A)        Científico(C) ")
    while (eleccion != "S" and eleccion != "s" and eleccion != "A" and eleccion != "a" and eleccion != "C" and eleccion != "c"):
        eleccion = input ("Escoge a tu compañero:        Soldado(S)   Acorazado(A)        Científico(C) ")
    if (eleccion == "S" or eleccion == "s"):
        ataque += 3
        print("Te acompañará un soldado")
    if (eleccion == "A" or eleccion == "a"):
        vida += 10
        vida_maxima += 10
        defensa += 2
        print("Te acompañará un acorazado")
    if (eleccion == "C" or eleccion == "c"):
        inteligencia += 8
        print("Te acompañará un científico")
    for i in range(len(MAPA)):
        for j in range(len(MAPA[i])):
            if (MAPA[i][j] == 1):
                MAPA[i][j] = random.randint(2,20)
    return vida,vida_maxima,ataque,defensa,inteligencia,MAPA


def comerciar(ARMAS,ARMADURAS,dinero,inteligencia):
    """Pasando como parámetro  las listas ARMAS y ARMADURAS, el dinero y la inteligendia,
    genera 3 productos que se pueden comprar mediante la función obtener_producto,
    y tras la elección del jugador recibida por teclado, devuelve el dinero y el objeto
    comprado, o bien el dinero y una lista con un 0 (para el condicional que recibe la función)
    si no se compra nada"""
    print("Te encuentras un armero que ofrece equipamiento a cambio de dinero")
    producto1,coste1 = obtener_producto(ARMAS,ARMADURAS,inteligencia)
    producto2,coste2 = obtener_producto(ARMAS,ARMADURAS,inteligencia)
    producto3,coste3 = obtener_producto(ARMAS,ARMADURAS,inteligencia)
    print("Tienes",dinero,"créditos")
    while (dinero > coste1 or dinero > coste2 or dinero > coste3):
        eleccion = input ("Escoge uno de los productos anteriores: el primero(1), el segundo(2), el tercero(3) o ninguno(0) ")
        while ( eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "0"):
            eleccion = input ("Escoge uno de los productos anteriores: el primero(1), el segundo(2), el tercero(3) o ninguno(0) ")
        if (eleccion == "1"):
            if(dinero >= coste1):
                dinero -= coste1
                print("Compras el/la",producto1[0],"y te quedas con",dinero,"créditos")
                return producto1,dinero
            else:
                print("No tienes créditos suficientes para comprar ese producto")
                continue
        if (eleccion == "2"):
            if(dinero >= coste2):
                dinero -= coste2
                print("Compras el/la",producto2[0],"y te quedas con",dinero,"créditos")
                return producto2,dinero
            else:
                print("No tienes créditos suficientes para comprar ese producto")
                continue
        if (eleccion == "3"):
            if(dinero >= coste3):
                dinero -= coste3
                print("Compras el/la",producto3[0],"y te quedas con",dinero,"créditos")
                return producto3,dinero
            else:
                print("No tienes créditos suficientes para comprar ese producto")
                continue
        if (eleccion == "0"):
            print("No compras nada")
            return [0],dinero
    print("No tienes créditos suficiente para comprar nada")
    return [0],dinero

def obtener_producto(ARMAS,ARMADURAS,inteligencia):
    """Usado en la función comerciar, pasando como parámetro la inteligencia
    y las listas ARMAS y AMRADURAS, genera o bien un arma (de inteligencia <= a la del jugador)
    o bien una armadura al azar de entre las de la lista correspondiente, y la devuelve"""
    producto = random.randint(0,1)
    if (producto == 0):
        producto = ARMAS[random.randint(1,len(ARMAS)-1)]
        coste = producto[4]
        while (producto[3] > inteligencia):
            producto = ARMAS[random.randint(1,len(ARMAS)-1)]
            coste = producto[4]
        print("Te vende un/una ", producto[0], " de daño ",producto[1],"-",producto[2]," a un precio de ",coste,sep="")
    else:
        producto = ARMADURAS[random.randint(1,len(ARMADURAS)-1)]
        coste = producto[2]
        print("Te vende un/una", producto[0], "de defensa",producto[1],"a un precio de",coste)
    return producto,coste


def comprar_implantes(dinero,ataque,defensa,inteligencia):
    """Pasando como parámetro el dinero, el ataque, la defensa y la inteligencia,
    pregunta al jugador si quiere mejorar alguna de las estadísticas a cambio de dinero,
    y en función de su elección mejora alguna o no,
    retornando las estadísticas (posiblemente cambiados) en función de la elección"""
    coste = 10
    print("Te encuentras un vendedor de implantes cibernéticos que mejoran tus estadísticas\nSolo puedes comprar uno ya que necesitas recuperarte tras la operación")
    print("Un implante cuesta",coste,"créditos y tienes",dinero)
    eleccion = input("Escoge tu implante:\nImplantes musculares(1): +1 de ataque\nBlindaje subdérmico(2): +1 de defensa\nCortéx cibernético(3): +2 de inteligencia\nNo comprar ninguno(0) ")
    while (eleccion != "0" and eleccion != "1" and eleccion != "2" and eleccion != "3"):
        eleccion = input("Escoge tu implante:\nImplantes musculares(1): +1 de ataque\nBlindaje subdérmico(2): +1 de defensa\nCortéx cibernético(3): +2 de inteligencia\nNo comprar ninguno(0) ")
    if (eleccion != "0" and dinero < coste):
        print("No tienes dinero suficiente para comprar ningún implante")
        return dinero,ataque,defensa,inteligencia
    if (eleccion == "1"):
        print("Te has instalado implantes musculares. Ahora eres más fuerte.")
        ataque += 1
        dinero -= coste
        return dinero,ataque,defensa,inteligencia
    if (eleccion == "2"):
        print("Te has instalado blindaje subdérmico. Ahora eres más resistente.")
        defensa += 1
        dinero -= coste
        return dinero,ataque,defensa,inteligencia
    if (eleccion == "3"):
        print("Te has instalado cortéx cibernético. Ahora eres más inteligente.")
        inteligencia += 2
        dinero -= coste
        return dinero,ataque,defensa,inteligencia
    if (eleccion == "0"):
        print("No te has instalado nada.")
        return dinero,ataque,defensa,inteligencia


def usar_medico(vida,vida_maxima,dinero):
    """Pasando como parámetro la vida, la vida máxima y el dinero,
    pregunta al jugador si quiere restaurar la vida a cambio de cierta cantidad de dinero,
    y en función de su elección le cura o no,
    y retorna la vida y el dinero (posiblemente cambiados) en función de la elección"""
    coste = 10
    print("Te encuentras con un médico que se ofrece a curar tus heridas a cambio de",coste,"créditos")
    print("Tienes",vida,"puntos de vida sobre un total de",vida_maxima,"puntos y dispones de",dinero,"créditos")
    if (vida == vida_maxima):
        print("No tienes heridas que curar")
        return vida,dinero
    eleccion = input ("¿Quieres pagar para curar tus heridas?: Sí(S) o No(N) ")
    while (eleccion != "S" and eleccion != "s" and eleccion != "si" and eleccion != "N" and eleccion != "n" and eleccion != "no"):
        eleccion = input ("¿Quieres pagar para curar tus heridas?: Sí(S) o No(N) ")
    if (eleccion == "S" or eleccion == "s" or eleccion == "si"):
        if(dinero >= coste):
            print("Has curado tus heridas")
            vida = vida_maxima
            dinero -= coste
            return vida,dinero
        else:
            print("No tienes dinero suficiente para curarte")
            return vida,dinero
    else:
        print("Decides no curarte")
        return vida,dinero