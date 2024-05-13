################################################################################
#
# Fundamentos de Informática
# Universidad de Oviedo
#
# Versión: 1.01 (18/01/2023)
#
# Autores: Jesús Ríos Álvarez, Marcos Regueiro Camblor, Sarah Colombo Rodríguez (Grupo 18 - T2)
#
###

import random
import exploracionSpOd
import datosSpOd
import combateSpOd
import acontecimientosSpOd
import entradaysalidaSpOd
from datosSpOd import ARMAS,ARMADURAS,ENEMIGOS

##estadísticas de personaje
vida_maxima = 0
vida = 0
ataque = 0
defensa = 0
inteligencia = 0

##inventario
arma = ARMAS[0]
armadura = ARMADURAS[0]
dinero = 10

##estadísticas de partida
salas_recorridas = 0
enemigos_derrotados = 0
resultado = ""
clase = ""

##comienzo del juego
print("""
  _________                           ________       .___
 /   _____/__________    ____  ____   \_____  \    __| _/__.__. ______ ______ ____ ___.__.
 \_____  \\____ \__  \ _/ ___\/ __ \   /   |   \  / __ <   |  |/  ___//  ___// __ <   |  |
 /        \  |_> > __ \\  \__\  ___/  /    |    \/ /_/ |\___  |\___ \ \___ \\  ___/\___  |
/_______  /   __(____  /\___  >___  > \_______  /\____ |/ ____/____  >____  >\___  > ____|
        \/|__|       \/     \/    \/          \/      \/\/         \/     \/     \/\/
""")
print("La Estación Espacial Arquímedes ha caído víctima de un terrible virus esparcido por un corruptor en la sala de mandos que está enloqueciendo a su tripulación y transformándolos en horribles monstruos.")
print("Tu eres un operativo de élite que ha sido envíado a acabar con el corruptor y poner fin a esta plaga")
print("Un aterrizaje de emergencia por un fallo en el módulo de navegación ha provocado que pierdas todo tu equipo, así que tendrás que equiparte con lo que encuentres en la estación para poder derrotar al corruptor")
print("Afortunadamente, conservas tus créditos al estar en tu cuenta de CajaEspacial así que podrás usarlos en la Estación")
print("Ten cuidado con los peligros de la Estación y buena suerte en tu misión\n")

vida_maxima,vida,ataque,defensa,inteligencia,clase = entradaysalidaSpOd.escoger_clase()
n = random.randint(8,9)
MAPA = exploracionSpOd.crear_mapa(n)
posicion = [3,4]
while(vida>0):
    entradaysalidaSpOd.mostrar_estadisticas(vida,vida_maxima,ataque,defensa,inteligencia,arma,armadura,dinero)
    posicion = exploracionSpOd.escoger_sala(posicion,MAPA,n)
    salas_recorridas += 1
    if (MAPA[posicion[0]][posicion[1]] in (14,15,16,17,18,19,20)):
        enemigo = datosSpOd.escoger_enemigo()
        vida_enemigo = enemigo[3]
        print("Te encuentras con un/una",enemigo[0],"al entrar en la sala")
        while(vida > 0 and vida_enemigo > 0):
            entradaysalidaSpOd.mostrar_vida(vida,enemigo,vida_enemigo)
            eleccion = combateSpOd.preguntar_eleccion(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia)
            if (eleccion == -1):
                break
            else:
                vida,vida_enemigo = eleccion
        if(vida_enemigo <= 0):
            dinero += combateSpOd.calcular_recompensa(enemigo)
            enemigos_derrotados += 1
    elif (MAPA[posicion[0]][posicion[1]] == 21):##jefe final
        enemigo = ENEMIGOS[len(ENEMIGOS)-1]
        vida_enemigo = enemigo[3]
        entradaysalidaSpOd.avisar_jefe(vida,enemigo,vida_enemigo)
        eleccion = combateSpOd.preguntar_eleccion(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia)
        if (eleccion == -1):
            continue
        else:
            vida,vida_enemigo = eleccion
        while(vida > 0 and vida_enemigo > 0):
            entradaysalidaSpOd.mostrar_vida(vida,enemigo,vida_enemigo)
            vida,vida_enemigo = combateSpOd.preguntar_eleccion_jefe(vida,ataque,defensa,arma,enemigo,vida_enemigo,armadura,inteligencia)
        if(vida_enemigo <= 0):## al ganar
            enemigos_derrotados += 1
            resultado = "Has derrotado al corruptor y salvado la estación"
            print("\n---------------------- Has logrado derrotar al corruptor ----------------------")
            print("Con la sala de mandos libre, consigues introducir el antivirus en los sistemas de filtrado de oxígeno, librando a la Estacion del virus y salvando a su tripulación")
            print("                                 MISION CUMPLIDA")
            break

    elif (MAPA[posicion[0]][posicion[1]] == 0):## 0 - sala vacia
        acontecimientosSpOd.sala_vacia()

    elif (MAPA[posicion[0]][posicion[1]] == 1):## 1 - sala de compañero
        vida,vida_maxima,ataque,defensa,inteligencia,MAPA = acontecimientosSpOd.obtener_compañero(vida,vida_maxima,ataque,defensa,inteligencia,MAPA)
        MAPA[posicion[0]][posicion[1]] = 0

    elif (MAPA[posicion[0]][posicion[1]] == 2):## 2 - sala de implantes
        dinero,ataque,defensa,inteligencia = acontecimientosSpOd.comprar_implantes(dinero,ataque,defensa,inteligencia)

    elif (MAPA[posicion[0]][posicion[1]] in (3,4,5)):## 3,4,5 - sala de arma
        arma = acontecimientosSpOd.obtener_arma(arma,inteligencia,ARMAS)
        MAPA[posicion[0]][posicion[1]] = 0

    elif (MAPA[posicion[0]][posicion[1]] in (6,7,8)):## 6,7,8 - sala de armadura
        armadura = acontecimientosSpOd.obtener_armadura(armadura,ARMADURAS)
        MAPA[posicion[0]][posicion[1]] = 0

    elif (MAPA[posicion[0]][posicion[1]] in (9,10)):## 9,10 - sala de comerciante
        compra,dinero = acontecimientosSpOd.comerciar(ARMAS,ARMADURAS,dinero,inteligencia)
        if (len(compra) == 5):
            arma = compra
        elif (len(compra) == 3):
            armadura = compra

    elif (MAPA[posicion[0]][posicion[1]] in (11,12,13)):## 11,12,13 - sala de médico
        vida,dinero = acontecimientosSpOd.usar_medico(vida,vida_maxima,dinero)

if (vida <= 0):## al morir
    print("\n------------------ Has muerto a manos de un/una",enemigo[0],"------------------")
    print("Con tu muerte la Estación Espacial Arquímedes está condenada a sucumbir al virus")
    print("                             MISION FALLIDA")
    resultado = "No has conseguido recuperar la estación"


## fichero (estadísticas de juego)
print("\nRevisa el fichero estadísticas_SpaceOddyssey para comprobar tus estadísticas")
f = open ('estadísticas_SpaceOddyssey', 'a')
f.write('Clase escogida: '+ clase + '\n')
f.write('Salas recorridas: ' + str(salas_recorridas) +'\n')
f.write('Enemigos derrotados: ' + str(enemigos_derrotados) + '\n')
f.write('Resultado: ' + resultado + '\n\n')
f.close()