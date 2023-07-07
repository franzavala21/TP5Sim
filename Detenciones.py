import copy
import random
from Rugen_Kutta import *


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
    fila.h_prox_detencion = None

    return fila, vector_rk3


