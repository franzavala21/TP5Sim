import copy
import random
import math
from Rugen_Kutta import *
from Detenciones import *
# esto es un comentario
# Falta agregar el t acum de sistema al fin de maquina y paciencia

from Fila import *
def principal(cant_dias, mostrar_desde,lambda_cercania, lambda_interp, lambda_ant, lambda_maq, lambda_critica, uniforme_min, uniforme_max,uniforme_min_enc, uniforme_max_enc, mostrar_acmulado):
    global lambda_cercania1
    lambda_cercania1 = lambda_cercania
    global lambda_interp1
    lambda_interp1 = lambda_interp
    global lambda_ant1
    lambda_ant1 = lambda_ant
    global lambda_maq1
    lambda_maq1 = lambda_maq
    global lambda_critica1
    lambda_critica1 = lambda_critica
    global uniforme_min1
    uniforme_min1 = uniforme_min
    global uniforme_max1
    uniforme_max1 = uniforme_max
    global uniforme_min2
    uniforme_min2 = uniforme_min_enc
    global uniforme_max2
    uniforme_max2 = uniforme_max_enc
    global vector_rk1
    global vector_rk2
    global vector_rk3
    global t_rk1
    t_rk1 = 1

    tiempo_rk1, vector_rk1 = runge_kutta_1(0.2,50, 0.1)
    tiempo_rk2, vector_rk2 = runge_kutta_2(30, 0.1)
    tiempo_rk3, vector_rk3 = runge_kutta_3(50, 0.1)

    vec_filas = ()
    cant_fin_paciencia = 0
    porcentaje_fin_paciencia = 0
    porcentaje_encuesta = 0
    promedio_t_sistema = 0
    largo_maximo_ant = 0
    largo_maximo_inm = 0
    for dia in range(cant_dias):
        guardar = False
        if mostrar_desde <= dia <= mostrar_desde + 10:
            guardar = True


        fila_inicial = crear_fila_inicial()
        if dia > 0 and mostrar_acmulado:
            fila_inicial.cantidad_fin_paciencia = vec_filas[-1].cantidad_fin_paciencia
            fila_inicial.porcentaje_fin_paciencia = vec_filas[-1].porcentaje_fin_paciencia
            fila_inicial.cantidad_encuesta = vec_filas[-1].cantidad_encuesta
            fila_inicial.porcentaje_encuesta = vec_filas[-1].porcentaje_encuesta
            fila_inicial.t_acum_sistema = vec_filas[-1].t_acum_sistema
            fila_inicial.promedio_t_sistema = vec_filas[-1].promedio_t_sistema
            fila_inicial.cant_entraron = vec_filas[-1].cant_entraron
            fila_inicial.cantidad_salieron = vec_filas[-1].cantidad_salieron
        fila = copy.deepcopy(fila_inicial)
        fila_anterior = copy.deepcopy(fila)
        vec_filas += (fila_inicial,)

        while fila.reloj < 1440 or(len(fila.cola_ant) > 0 or len(fila.cola_inm) > 0):

            fila = copy.deepcopy(proxima_fila(fila_anterior))


            fila_anterior = copy.deepcopy(fila)

            fila_anterior = random_a_None(fila_anterior)

            if fila.cantidad_salieron == 0:
                fila.promedio_t_sistema = 0
            else:
                fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
            if guardar:

                fila_a_agregar = copy.deepcopy(fila)

                vec_filas += (fila_a_agregar,)
            if len(fila.cola_ant) > largo_maximo_ant:
                largo_maximo_ant = len(fila.cola_ant)

            if len(fila.cola_inm) > largo_maximo_inm:
                largo_maximo_inm = len(fila.cola_inm)
                """linea = vec_filas[1]
                print(linea.reloj, linea.evento, linea.rnd_ll, linea.t_ll, linea.h_ll, linea.rnd_tipo,
                      linea.tipo, linea.est_encuesta, linea.rnd_t_antenc_encuesta,
                      linea.t_atenc_encuesta, linea.h_atenc_encuesta, linea.est_vent_inm_1, linea.est_vent_inm_2,
                      linea.rnd_t_antenc_inm,
                      linea.t_atenc_inm, linea.h_atenc_inm_1, linea.h_atenc_inm_2, linea.est_maquina,
                      linea.rnd_t_antenc_maq,
                      linea.t_atenc_maq, linea.h_atenc_maq, linea.est_vent_ant, linea.rnd_t_antenc_ant,
                      linea.t_atenc_ant,
                      linea.h_atenc_ant, linea.cantidad_ant, linea.cantidad_inm, linea.cola_ant, linea.cola_inm)"""



        cant_fin_paciencia += fila.cantidad_fin_paciencia
        porcentaje_fin_paciencia += fila.porcentaje_fin_paciencia
        porcentaje_encuesta += fila.porcentaje_encuesta
        promedio_t_sistema += fila.promedio_t_sistema




    vec_estadisticas = [cant_fin_paciencia / cant_dias, porcentaje_fin_paciencia / cant_dias,
                        porcentaje_encuesta / cant_dias, promedio_t_sistema / cant_dias ]
    if mostrar_acmulado:
        vec_estadisticas = [fila.cantidad_fin_paciencia, fila.porcentaje_fin_paciencia, fila.porcentaje_encuesta, fila.promedio_t_sistema]

    if mostrar_desde + 10 < cant_dias and cant_dias > 0:
        fila_a_agregar = copy.deepcopy(fila)

        vec_filas += (fila_a_agregar,)


    return vec_filas, vec_estadisticas, largo_maximo_ant, largo_maximo_inm , vector_rk1, vector_rk2, vector_rk3




def proxima_fila(fila_anterior):
    fa = fila_anterior
    cantidad_llegadas = 0

    # Cargo los tiempos dellegada a la fila de
    primero_cola_inm = 499999999
    segundo_cola_inm = 500000000
    pos_cola_1 = None
    pos_cola_2 = None

    for i in range(len(fa.cola_ant)):

        if fa.cola_ant[i][0] == "C" and primero_cola_inm != 499999999:
            segundo_cola_inm = fa.cola_ant[i][2]
            pos_cola_2 = i
            break
        if fa.cola_ant[i][0] == "C" and primero_cola_inm == 499999999:
            primero_cola_inm = fa.cola_ant[i][2]
            pos_cola_1 = i
            break

    primero_cola_inm += 20
    segundo_cola_inm += 20




    hora_minima = 500000000
    i = 0
    siguiente_evento = 11
    for hora in (fa.h_ll, fa.h_atenc_encuesta, fa.h_atenc_ant, fa.h_atenc_inm_1, fa.h_atenc_inm_2, fa.h_atenc_maq,
                 primero_cola_inm, segundo_cola_inm, fa.h_prox_detencion, fa.h_fin_detencion_ll,fa.h_fin_detencion_vent):
        if hora != None:
            if hora < hora_minima:
                hora_minima = hora
                siguiente_evento = i
        i += 1



    if siguiente_evento == 11:
        print("Fin")


    if siguiente_evento == 0:

        fila = llegada(fila_anterior)
        fila.cant_entraron += 1
        cantidad_llegadas += 1
        if cantidad_llegadas == 150:
            beta = random.random()
            global t_rk1
            t_rk1, vector_rk1 = runge_kutta_1(beta,fila.reloj,0.1)
            fila.h_prox_detencion = copy.copy(fila.reloj + t_rk1)


    elif siguiente_evento == 1:

        fila = fin_atencion_encuesta(fila_anterior)
        fila.cantidad_encuesta += 1
        fila.evento = "fin encuesta"

    elif siguiente_evento == 2:

        fila = fin_atencion_anticipada(fila_anterior)
        fila.cantidad_salieron += 1
        fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
        fila.evento = "fin atencion ant"


    elif siguiente_evento == 3:

        fila = fin_atencion_inmediata_1(fila_anterior)
        fila.cantidad_salieron += 1
        fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
        fila.evento = "fin atencion inm 1"


    elif siguiente_evento == 4:

        fila = fin_atencion_inmediata_2(fila_anterior)
        fila.cantidad_salieron += 1
        fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
        fila.evento = "fin atencion inm 2"

    elif siguiente_evento == 5:

        fila = copy.deepcopy(fin_atencion_maquina(fila_anterior))
        fila.cantidad_salieron += 1
        fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
        fila.evento = "fin atencion maq"
        print(fila_anterior.cola_inm)


    elif siguiente_evento == 6 or siguiente_evento == 7:

        if siguiente_evento == 6:
            fila = fin_paciencia(fila_anterior,1)
        else:
            fila = fin_paciencia(fila_anterior, 2)

        fila.cantidad_salieron += 1
        fila.cantidad_fin_paciencia += 1

        fila.promedio_t_sistema = fila.t_acum_sistema / fila.cantidad_salieron
        fila.evento = "fin paciencia"

    elif siguiente_evento == 8:
        fila = copy.deepcopy(fila_anterior)
        fila.reloj = fila_anterior.h_prox_detencion
        fila.rnd_tipo_detencion = random.random()

        if fila.rnd_tipo_detencion < 35:
            # DETENCION LLEGADA
            pass

        else:

            fila, vector_rk3 = detener_atencion(fila_anterior)
            print("Detencion")



    elif siguiente_evento == 9:
        fila = fin_detencion_atencion(fila_anterior)
        fila.h_prox_detencion = copy.copy(fila.reloj + t_rk1)
        print("Fin Detencion Llegada")

    elif siguiente_evento == 10:
        print("Fin Detencion Vantanilla")
        # Cambiar estado de ventanilla a Libre o Ocupado



    fila.porcentaje_encuesta = fila.cantidad_encuesta * 100 / fila.cant_entraron
    if fila.cantidad_salieron == 0:
        fila.porcentaje_fin_paciencia = 0
    else:
        fila.porcentaje_fin_paciencia = fila.cantidad_fin_paciencia * 100 / fila.cantidad_salieron
    linea = fila
    return fila
"""print(linea.reloj, linea.evento, linea.rnd_ll, linea.t_ll, linea.h_ll, linea.rnd_tipo,
  linea.tipo, linea.est_encuesta, linea.rnd_t_antenc_encuesta,
  linea.t_atenc_encuesta, linea.h_atenc_encuesta, linea.est_vent_inm_1, linea.est_vent_inm_2,
  linea.rnd_t_antenc_inm,
  linea.t_atenc_inm, linea.h_atenc_inm_1, linea.h_atenc_inm_2, linea.est_maquina, linea.rnd_t_antenc_maq,
  linea.t_atenc_maq, linea.h_atenc_maq, linea.est_vent_ant, linea.rnd_t_antenc_ant, linea.t_atenc_ant,
  linea.h_atenc_ant, linea.cantidad_ant, linea.cantidad_inm, linea.cola_ant, linea.cola_inm)"""



# HAY QUE GUARDAR EN ALGUN LUGAR LA LONGITUD MAXIMA QUE HAYA TENIDO CADA COLA (LO PODEMOS CONVERTIR EN UNA ESTADISTICA)


def crear_fila_inicial():
    lambda_ll = lambda_critica1 # Cambiar lamda
    fila_inicial = Fila()
    fila_inicial.reloj = 360
    fila_inicial.evento = "Inicio"
    fila_inicial.rnd_ll, fila_inicial.t_ll = gen_exponencial(lambda_ll)
    fila_inicial.h_ll = fila_inicial.t_ll + fila_inicial.reloj
    fila_inicial.est_maquina = "Libre"
    fila_inicial.est_encuesta = "Libre"
    fila_inicial.est_vent_ant = "Libre"
    fila_inicial.est_vent_inm_1 = "Libre"
    fila_inicial.est_vent_inm_2 = "Libre"
    fila_inicial.cantidad_ant = 0
    fila_inicial.cantidad_inm = 0
    fila_inicial.cantidad_fin_paciencia = 0
    fila_inicial.porcentaje_fin_paciencia = 0
    fila_inicial.cantidad_encuesta = 0
    fila_inicial.porcentaje_encuesta = 0
    fila_inicial.t_acum_sistema = 0
    fila_inicial.promedio_t_sistema = 0
    fila_inicial.cant_entraron = 0
    fila_inicial.cantidad_salieron = 0


    return fila_inicial


# ESTO LO HACE JERE
def llegada(fila_anterior):
    fila = copy.deepcopy(fila_anterior)



    fila.reloj = fila_anterior.h_ll
    fila.evento = "Llegada"



    if fila.reloj < 1440:
        if fila.reloj < 900: # Critico
            fila.rnd_ll, fila.t_ll = gen_exponencial(lambda_critica1)

        else: # Normal

            fila.rnd_ll, fila.t_ll = gen_uniforme(uniforme_min1, uniforme_max1)
        fila.h_ll = fila.reloj + fila.t_ll
    else:
        fila.h_ll = None

    # Cargo el tipo de llegada y lo agrego a la cola que corresponda
    fila.rnd_tipo = random.random()
    # Llegada inmediata
    if fila.rnd_tipo < 0.75:

        fila.tipo = "Interp"
        if fila.rnd_tipo < 0.5:
            fila.tipo = "Cerc"
        fila.cola_inm.append([None, fila.tipo, None, fila.reloj])


        if fila.est_encuesta == "Libre":
            fila.est_encuesta = "Atendiendo"
            fila.cola_inm[-1][0] = "E"
            fila.rnd_t_antenc_encuesta , fila.t_atenc_encuesta = gen_uniforme(uniforme_min2,uniforme_max2)
            fila.h_atenc_encuesta = fila.reloj + fila.t_atenc_encuesta

        else:
            fila = atender_inm_o_cola(fila,-1)



    # Llegada anticipada
    else:
        fila.tipo = "Ant lento"
        if fila.rnd_tipo < 0.95:
            fila.tipo = "Ant norm"
        fila.cola_ant.append([None, fila.tipo, fila.reloj])

        if fila.est_ll == "Detenido":
            pass
            # Van a una cola

        elif fila.est_encuesta == "Libre":

            fila.est_encuesta = "Atendiendo"
            fila.cola_ant[-1][0] = "E"
            fila.rnd_t_antenc_encuesta, fila.t_atenc_encuesta = gen_uniforme(uniforme_min2,uniforme_max2)
            fila.h_atenc_encuesta = fila.reloj + fila.t_atenc_encuesta

        else:
            fila = atender_ant_o_cola(fila, -1)

    return fila




def fin_atencion_encuesta(fila_anterior):
    fila = copy.deepcopy(fila_anterior)

    fila.evento = "Fin encuesta"
    fila.reloj = fila_anterior.h_atenc_encuesta
    fila.est_encuesta = "Libre"
    fila.h_atenc_encuesta = None
    encontrado = False
    for i in range(len(fila.cola_ant)):
        if fila.cola_ant[i][0] == "E":
            encontrado = True
            fila = copy.deepcopy(atender_ant_o_cola(fila, i))
            break
    if not encontrado:
        for i in range(len(fila.cola_inm)):
            if fila.cola_inm[i][0] == "E":
                fila = copy.deepcopy(atender_inm_o_cola(fila, i))

                break
    return fila


# ESTO LO HACE FRAN
def fin_atencion_anticipada(fila_anterior):
    fila = copy.deepcopy(fila_anterior)
    fila.reloj = fila_anterior.h_atenc_ant
    fila.h_atenc_ant = None
    for i in range(len(fila.cola_ant)):
        if fila.cola_ant[i][0] == "SA":
            #Elimino el cliente
            fila.t_acum_sistema += fila.reloj - fila.cola_ant[i][2]
            fila.cola_ant.pop(i)
            break
    if fila_anterior.cantidad_ant > 0:
        
        #tipo_atencion = None

        for i in range(len(fila.cola_ant)):
            if fila.cola_ant[i][0] == 'C':
                fila.cantidad_ant -= 1
                #tipo_atencion = fila.cola_ant[i][1]
                pos = i
                fila = inicio_atencion_ant(fila, pos)
                fila.cola_ant[pos][0] = 'SA'
                break

    else:
        fila.est_vent_ant = 'Libre'

    return fila




def fin_atencion_inmediata_1(fila_anterior):
    fila = copy.deepcopy(fila_anterior)

    fila.reloj = fila_anterior.h_atenc_inm_1
    fila.evento = "Fin atencion"
    fila.h_atenc_inm_1 = None


    # Elimino al cliente
    for i in range(len(fila.cola_inm)):
        if fila.cola_inm[i][2] == 'V1':
            fila.t_acum_sistema += fila.reloj - fila.cola_inm[i][3]
            fila.cola_inm.pop(i)
            break

    if fila_anterior.cantidad_inm > 0:
        #Si no encontro a nadie
        tipo_atencion = None

        # Obtener el tipo de atención del siguiente cliente en la cola
        for i in range(len(fila.cola_inm)):
            if fila.cola_inm[i][0] == 'C':
                tipo_atencion = fila.cola_inm[i][1] 
                fila.cantidad_inm -= 1
                pos = i
                break

        if tipo_atencion == "Cerc": 

            fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_cercania1)
            fila.h_atenc_inm_1 = fila.reloj + fila.t_atenc_inm
            fila.cola_inm[pos][0] = "SA"
            fila.cola_inm[pos][2] = "V1"
            

        elif tipo_atencion == "Interp": 
            fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_interp1)
            fila.h_atenc_inm_1 = fila.reloj + fila.t_atenc_inm
            fila.cola_inm[pos][0] = "SA"
            fila.cola_inm[pos][2] = "V1"
        
   

    else:
        fila.est_vent_inm_1 = "Libre"
        fila.h_atenc_inm_1 = None
        #Fijarse que otra cosa puede pasar si no hay clientes en cola

    #Metricas


    return fila

def fin_atencion_inmediata_2(fila_anterior):
        fila = copy.copy(fila_anterior)
        fila.cola_ant = copy.copy(fila.cola_ant)
        fila.cola_inm = copy.copy(fila.cola_inm)
        fila.reloj = fila_anterior.h_atenc_inm_2
        fila.evento = "Fin atencion"
        fila.h_atenc_inm_2 = None
        # Elimino al cliente
        for i in range(len(fila.cola_inm)):
            if fila.cola_inm[i][2] == 'V2':
                fila.t_acum_sistema += fila.reloj - fila.cola_inm[i][3]
                fila.cola_inm.pop(i)
                break
        if fila.reloj > 900:
            fila.est_vent_inm_2 = "Cerrada"
        else:
            if fila_anterior.cantidad_inm > 0:
                #Si no encontro a nadie
                tipo_atencion = None

                # Obtener el tipo de atención del primer cliente en la cola
                for i in range(len(fila.cola_inm)):
                    if fila.cola_inm[i][0] == 'C':
                        tipo_atencion = fila.cola_inm[i][1]

                        fila.cantidad_inm -= 1
                        pos = i
                        break

                if tipo_atencion == "Cerc":

                    fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_cercania1)
                    fila.h_atenc_inm_2 = fila.reloj + fila.t_atenc_inm
                    fila.cola_inm[pos][0] = "SA"
                    fila.cola_inm[pos][2] = "V2"


                elif tipo_atencion == "Interp":
                    fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_interp1)
                    fila.h_atenc_inm_2 = fila.reloj + fila.t_atenc_inm
                    fila.cola_inm[pos][0] = "SA"
                    fila.cola_inm[pos][2] = "V2"



            else:
                fila.est_vent_inm_2 = "Libre"
                fila.h_atenc_inm_2 = None
            #Fijarse que otra cosa puede pasar si no hay clientes en cola
        return fila


# ESTO LO HACE VALE
def fin_atencion_maquina(fila_anterior):
    fila = copy.deepcopy(fila_anterior)

    fila.reloj = fila_anterior.h_atenc_maq
    fila.evento = "Fin atencion maquina"
    fila.h_atenc_maq = None
    x = len(fila.cola_inm)

    for i in range(x):

        if fila.cola_inm[i][0] == "SA" and fila.cola_inm[i][2] == "M":
            fila.t_acum_sistema += fila.reloj - fila.cola_inm[i][3]
            fila.cola_inm.pop(i)
            break

    fila.h_atenc_maq = None
    fila.est_maquina = "Libre"

    if fila.cantidad_inm > 0:
        for i in range(fila.cantidad_inm):
            if fila.cola_inm[i][1] == "Cerc" and fila.cola_inm[i][0] == "C":
                fila.cantidad_inm -= 1
                fila = inicio_atencion_maquina(i, fila)
            break

    return fila


"""def fin_atencion_maquina(fila_anterior):

    for i in range(len(fila_anterior.cola_inm)):
       if fila_anterior.cola_inm[i][0] == "M":
           pos_cola = i
           fila_anterior.cola_inm.pop(pos_cola)
           break

    encontrado = False
    if fila_anterior.cantidad_inm > 0:

        for i in range(len(fila_anterior.cola_inm)):
            tipo = fila_anterior.cola_inm[i][1]
            estado = fila_anterior.cola_inm[i][0]
            if tipo == "Cerc" and estado == "C":
                fila_anterior.cola_inm[i][0] = "SA"
                fila_anterior.est_maquina = "Ocupado"
                fila_anterior.rnd_t_antenc_maq, fila_anterior.t_fin_atencion = gen_exponencial(0.5)  # μ=30 (en nro clientes/hora)
                fila_anterior.h_atenc_maq = fila_anterior.reloj + fila_anterior.t_fin_atencion
                encontrado = True


    if not encontrado:
        fila_anterior.est_maquina = "Libre"
    return fila_anterior"""


def fin_paciencia(fila_anterior, pos_cola):
    fila = copy.deepcopy(fila_anterior)

    fila.reloj = fila_anterior.cola_ant[pos_cola][2] + 20

    fila.t_acum_sistema += fila.reloj - fila.cola_ant[pos_cola][2]
    fila.cola_ant.pop(pos_cola)
    fila.cantidad_ant -= 1
    return fila

def gen_exponencial(lamda):
    rnd = random.random()
    x = - (1 / lamda) * math.log(1 - rnd)
    return rnd, x

def gen_normal(media, desviacion):
    rnd1 = random.random()
    rnd2 = random.random()
    z = ((-2 * math.log(rnd1)) ** 0.5) * math.cos(2 * math.pi * rnd2)
    x = media + z * desviacion
    return rnd1, x

def gen_uniforme(min, max):
    rnd = random.random()
    x = min + (max - min) * rnd
    return rnd, x


#  *********************  INICIO ATENCION   *********************
def inicio_atencion_inm_1(fila, pos_cola):
    tipo_atencion = fila.cola_inm[pos_cola][1]
    if tipo_atencion == "Cerc":  # HAY QUE PONERSE DE ACUERDO EN EL NOMRBRE DE LOS TIPOS Y ESTADOS

        fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_cercania1)
        fila.h_atenc_inm_1 = fila.reloj + fila.t_atenc_inm
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V1"

    elif tipo_atencion == "Interp":  # HAY QUE PONERSE DE ACUERDO EN EL NOMRBRE DE LOS TIPOS Y ESTADOS

        fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_interp1)
        fila.h_atenc_inm_1 = fila.reloj + fila.t_atenc_inm
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V1"
    return fila

def inicio_atencion_inm_2(fila, pos_cola):

    tipo_atencion = fila.cola_inm[pos_cola][1]
    if tipo_atencion == "Cerc":  # HAY QUE PONERSE DE ACUERDO EN EL NOMRBRE DE LOS TIPOS Y ESTADOS

        fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_cercania1)
        fila.h_atenc_inm_2 = fila.reloj + fila.t_atenc_inm
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V2"

    elif tipo_atencion == "Interp":  # HAY QUE PONERSE DE ACUERDO EN EL NOMRBRE DE LOS TIPOS Y ESTADOS
        fila.rnd_t_antenc_inm, fila.t_atenc_inm = gen_exponencial(lambda_interp1)
        fila.h_atenc_inm_2 = fila.reloj + fila.t_atenc_inm
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V2"
    return fila


def random_a_None(fila):
    fila.rnd_ll = None
    fila.t_ll = None
    fila.rnd_tipo = None
    fila.tipo  = None
    fila.rnd_t_antenc_inm = None
    fila.rnd_t_antenc_ant = None
    fila.rnd_t_antenc_maq = None
    fila.rnd_t_antenc_encuesta = None
    fila.t_atenc_inm = None
    fila.t_atenc_encuesta = None
    fila.t_atenc_ant = None
    fila.t_atenc_maq = None
    return fila


def inicio_atencion_maquina(pos_cola, fila):
    fila.cola_inm = copy.copy(fila.cola_inm)
    fila.cola_ant = copy.copy(fila.cola_ant)
    fila.cola_inm[pos_cola][0] = "SA"
    fila.cola_inm[pos_cola][2] = "M"
    fila.est_maquina = "Ocupado"
    fila.rnd_t_antenc_maq, fila.t_atenc_maq = gen_exponencial(lambda_maq1)
    fila.h_atenc_maq = fila.reloj + fila.t_atenc_maq
    return fila

def inicio_atencion_ant(fila, pos_fila):
    fila.cola_inm = copy.copy(fila.cola_inm)
    fila.cola_ant = copy.copy(fila.cola_ant)
    fila.rnd_t_antenc_ant, fila.t_atenc_ant = gen_exponencial(lambda_ant1)
    if fila.tipo == "Ant lento":
        fila.t_atenc_ant += 2
    fila.h_atenc_ant = fila.reloj + fila.t_atenc_ant


    fila.cola_ant[pos_fila][0] = "SA"

    fila.est_vent_ant = "Ocupado"
    return fila


def atender_inm_o_cola(fila, pos_cola):
    fila.cola_inm = copy.deepcopy(fila.cola_inm)
    fila.cola_ant = copy.deepcopy(fila.cola_ant)
    if fila.est_maquina == "Libre" and fila.cola_inm[pos_cola][1] == "Cerc":
        fila.est_maquina = "Atendiendo"
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "M"
        fila = inicio_atencion_maquina(pos_cola, fila)

    elif fila.est_vent_inm_1 == "Libre":
        fila.est_vent_inm_1 = "Atendiendo"
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V1"
        fila = inicio_atencion_inm_1(fila, pos_cola)

    elif fila.est_vent_inm_2 == "Libre":
        fila.est_vent_inm_2 = "Atendiendo"
        fila.cola_inm[pos_cola][0] = "SA"
        fila.cola_inm[pos_cola][2] = "V2"
        fila = inicio_atencion_inm_2(fila, pos_cola)

    else:
        fila.cola_inm[pos_cola][0] = "C"
        fila.cantidad_inm += 1
    return fila

def atender_ant_o_cola(fila, pos_cola):
    fila.cola_inm = copy.copy(fila.cola_inm)
    fila.cola_ant = copy.copy(fila.cola_ant)
    if fila.est_vent_ant == "Libre":
        fila.est_vent_ant = "Atendiendo"
        fila.cola_ant[pos_cola][0] = "SA"
        fila = inicio_atencion_ant(fila, pos_cola)

    else:
        fila.cola_ant[pos_cola][0] = "C"
        fila.cantidad_ant += 1
    return fila