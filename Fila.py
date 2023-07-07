class Fila():
    def __init__(self, reloj=None, evento = None , est_ll = None,rnd_ll = None, t_ll = None,h_ll= None, rnd_tipo = None,
                 tipo = None, est_encuesta = None, rnd_t_antenc_encuesta  = None,
                 t_atenc_encuesta  = None, h_atenc_encuesta  = None,est_vent_inm_1 = None, est_vent_inm_2 = None,rnd_t_antenc_inm = None,
                 t_atenc_inm = None,h_atenc_inm_1 = None,h_atenc_inm_2 = None,est_maquina = None,rnd_t_antenc_maq = None,
                 t_atenc_maq = None,h_atenc_maq = None,est_vent_ant = None,rnd_t_antenc_ant = None,t_atenc_ant = None,
                 h_atenc_ant = None,cantidad_ant = None, cantidad_inm = None,cantidad_fin_paciencia = None, porcentaje_fin_paciencia = None,
                 cantidad_encuesta = None, porcentaje_encuesta = None, t_acum_sistema = 0, promedio_t_sistema = None, cantidad_salieron = None,
                 cant_entraron = None, h_prox_detencion = None , rnd_tipo_detencion = None, tipo_detencion = None,
                 h_fin_detencion_ll = None,h_fin_detencion_vent = None , cola_ll = [], cola_ant = [], cola_inm = []):
        self.reloj = reloj
        self.evento = evento
        self.rnd_ll = rnd_ll
        self.t_ll = t_ll
        self.h_ll = h_ll
        self.rnd_tipo = rnd_tipo
        self.tipo = tipo
        self.est_encuesta = est_encuesta
        self.rnd_t_antenc_encuesta = rnd_t_antenc_encuesta
        self.t_atenc_encuesta = t_atenc_encuesta
        self.h_atenc_encuesta = h_atenc_encuesta
        self.est_vent_inm_1 = est_vent_inm_1
        self.est_vent_inm_2 = est_vent_inm_2
        self.rnd_t_antenc_inm = rnd_t_antenc_inm
        self.t_atenc_inm = t_atenc_inm
        self.h_atenc_inm_1 = h_atenc_inm_1
        self.h_atenc_inm_2 = h_atenc_inm_2
        self.est_maquina = est_maquina
        self.rnd_t_antenc_maq = rnd_t_antenc_maq
        self.t_atenc_maq = t_atenc_maq
        self.h_atenc_maq = h_atenc_maq
        self.est_vent_ant = est_vent_ant
        self.rnd_t_antenc_ant = rnd_t_antenc_ant
        self.t_atenc_ant = t_atenc_ant
        self.h_atenc_ant = h_atenc_ant
        self.cantidad_ant = cantidad_ant
        self.cantidad_inm = cantidad_inm
        self.cantidad_fin_paciencia = cantidad_fin_paciencia
        self.porcentaje_fin_paciencia = porcentaje_fin_paciencia
        self.cantidad_encuesta = cantidad_encuesta
        self.porcentaje_encuesta = porcentaje_encuesta
        self.t_acum_sistema = t_acum_sistema
        self.promedio_t_sistema = promedio_t_sistema
        self.cant_entraron = cant_entraron
        self.cantidad_salieron = cantidad_salieron
        self.est_ll = est_ll
        self.h_prox_detencion = h_prox_detencion
        self.rnd_tipo_detencion = rnd_tipo_detencion
        self.tipo_detencion = tipo_detencion
        self.h_fin_detencion_ll = h_fin_detencion_ll
        self.h_fin_detencion_vent = h_fin_detencion_vent
        self.cola_ll = cola_ll # cola de llegadas detenidas
        self.cola_ant = cola_ant  # [[est,tipo, h_ll], [est,tipo, h_ll] ,[est,tipo, h_ll]]
        self.cola_inm = cola_inm  # [[est, tipo, donde_se_esta_atiendiendo,h_ll],[est, tipo,donde_se_esta_atiendiendo,h_ll],
        # [est, tipo,donde_se_esta_atiendiendo,h_ll]]

        # donde_se_esta_atiendiendo puede ser "M" (maquina), "V1"(ventanilla1), "V2" ventanilla2)
