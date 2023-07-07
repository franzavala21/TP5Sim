import copy
import random
from Rugen_Kutta import *
from Eventos import *

def detener_atencion(fila_anterior):
    fila = copy.deepcopy(fila_anterior)


    rk, vector_rk3 = runge_kutta_3(fila.reloj,0.1)
    fila.tipo_detencion = "Servidor"
    if fila.est_vent_ant == "Atendiendo":  # ejemplo de ventanilla
        fila.h_atenc_ant += rk
    else:
        fila.h_atenc_ant = None
    fila.est_vent_ant = "Detenido"
    fila.h_fin_detencion_vent = fila.reloj + rk
    fila.evento = "Detención en ventanilla"

    return fila, vector_rk3


def fin_detencion_llegada(fila_anterior):
    fila = copy.deepcopy(fila_anterior)
    fila.evento = "Fin de detencion de llegadas"
    fila.reloj = fila_anterior.h_fin_detencion_ll

    

    

    

def fin_detencion_atencion(fila_anterior):
    fila = copy.deepcopy(fila_anterior)
    fila.reloj = fila_anterior.h_fin_detencion_vent
    fila.evento = "Fin de detención de servidor"
    encontrado = False
    if fila.h_atenc_ant == None:

        if fila_anterior.cantidad_ant > 0:
            for i in range(len(fila.cola_ant)):
                if fila.cola_ant[i][0] == 'C':
                    fila.cantidad_ant -= 1
                    # tipo_atencion = fila.cola_ant[i][1]
                    pos = i
                    fila = inicio_atencion_ant(fila, pos)
                    fila.est_vent_ant = "Ocupado"
                    fila.cola_ant[pos][0] = 'SA'
                    break

        else:
            fila.est_vent_ant = "Libre"
    else:
        fila.est_vent_ant = "Ocupado"


    return fila


def llegada_detenida(fila_anterior):
    fila = copy.deepcopy(fila_anterior)



    fila.reloj = fila_anterior.h_ll
    fila.evento = "Llegada detenida" 
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
        fila.cola_ll.append([None, fila.tipo, None, fila.reloj])
    else:
        fila.tipo = "Ant lento"
        if fila.rnd_tipo < 0.95:
            fila.tipo = "Ant norm"
        fila.cola_ll.append([None, fila.tipo, fila.reloj])
    
    return fila