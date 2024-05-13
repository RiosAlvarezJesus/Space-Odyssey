import random

## armas [nombre,daño mínimo,daño máximo,inteligencia requerida,precio]

ARMA0 = ["puños",1,2,0,0]
ARMA1 = ["pistola",3,5,0,6]
ARMA2 = ["porra",2,3,0,3]
ARMA3 = ["escopeta",4,12,0,12]
ARMA4 = ["fusil de precisión",7,9,0,12]
ARMA5 = ["cuchillo",3,4,0,5]
ARMA6 = ["rifle laser",11,15,15,20]
ARMA7 = ["lanzagrandas",10,20,0,25]
ARMA8 = ["cañon Gauss",20,20,25,33]
ARMA9 = ["BFG",25,35,40,50]
ARMA10 = ["pistola",3,5,0,6]
ARMA11 = ["porra",2,3,0,3]
ARMA12= ["ametralladora pesada",15,18,0,27]

ARMAS = [ARMA0,ARMA1,ARMA2,ARMA3,ARMA4,ARMA5,ARMA6,ARMA7,ARMA8,ARMA9,ARMA10,ARMA11,ARMA12]

## armaduras [nombre,defensa,precio]

ARMADURA0 = ["chaqueta",0,0]
ARMADURA1 = ["chaleco ligero",1,5]
ARMADURA2 = ["chaleco pesado",2,10]
ARMADURA3 = ["armadura corporal ligera",3,15]
ARMADURA4 = ["armadura corporal pesada",5,20]
ARMADURA5 = ["exoarmadura",7,30]
ARMADURA6 = ["chaleco ligero",1,5]
ARMADURA7 = ["armadura corporal ligera",3,15]

ARMADURAS = [ARMADURA0,ARMADURA1,ARMADURA2,ARMADURA3,ARMADURA4,ARMADURA5,ARMADURA6,ARMADURA7]

## enemigos [nombre,daño mínimo,daño máximo,vida,recompensa mín,recompensa máx]

ENEMIGO0 = ["cucaracha gigante",6,7,8,2,3]
ENEMIGO1 = ["larva",6,8,12,4,5]
ENEMIGO2 = ["saqueador",9,13,20,7,9]
ENEMIGO3 = ["torreta de seguridad",14,15,27,8,10]
ENEMIGO4 = ["robot limpiador",7,9,22,5,7]
ENEMIGO5 = ["robot guardián",11,13,27,6,8]
ENEMIGO6 = ["necromorfos",10,15,32,9,12]
ENEMIGO7 = ["necrófago",12,13,29,9,12]
ENEMIGO8 = ["juggernaut",23,26,44,14,19]
ENEMIGO9 = ["madre de progenie",17,22,58,15,18]
ENEMIGO10 = ["cucaracha gigante",6,7,8,2,3]
ENEMIGO11 = ["larva",6,8,12,4,5]
ENEMIGO12 = ["saqueador",9,13,20,7,9]
ENEMIGO13 = ["corruptor",30,35,100,0,0]##jefe final

ENEMIGOS = [ENEMIGO0,ENEMIGO1,ENEMIGO2,ENEMIGO3,ENEMIGO4,ENEMIGO5,ENEMIGO6,ENEMIGO7,ENEMIGO8,ENEMIGO9,ENEMIGO10,ENEMIGO11,ENEMIGO12,ENEMIGO13]

def escoger_enemigo():
    """Escoge un enemigo al azar de la lista ENEMIGOS y lo devuelve"""
    enemigo = ENEMIGOS[random.randint(0,len(ENEMIGOS)-2)]
    return enemigo