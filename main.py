import random
from Fila import *
from Eventos import *
from ventana_RK1 import *
from ventana_RK2 import *
from ventana_RK3 import *


from PyQt5 import uic, QtWidgets
import sys
def catch_exceptions(t, val, tb):
    old_hook(t, val, tb)
old_hook = sys.excepthook
sys.excepthook = catch_exceptions


qtCreatorFile = "Interfaz.ui"  # Nombre del archivo aquí.

Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)



        self.boton_simular.clicked.connect(self.simular)
        self.boton_RK1.clicked.connect(self.mostrar_RK1)
        self.boton_RK2.clicked.connect(self.mostrar_RK2)
        self.boton_RK3.clicked.connect(self.mostrar_RK3)





    def simular(self):
        self.tabla.clearContents()
        cant_dias = int(self.cant_dias.text())

        mostrar_desde = int(self.mostrar_desde.text())

        lambda_cercania =  float(self.lambda_cerc.text())
        lambda_interp = float(self.lambda_inter.text())
        lambda_ant = float(self.lambda_ant.text())
        lambda_maq = float(self.lambda_maq.text())
        lambda_critica = float(self.lambda_critica.text())
        uniforme_min = float(self.uniforme_min.text())
        uniforme_max = float(self.uniforme_max.text())
        uniforme_min_enc = float(self.uniforme_min_enc.text())
        uniforme_max_enc = float(self.uniforme_max_enc.text())
        multiplicador_rk1 = float(self.multiplicador_rk1.text())
        multiplicador_rk2 = float(self.multiplicador_rk2.text())
        multiplicador_rk3 = float(self.multiplicador_rk3.text())
        mostrar_acumulado = False
        if self.checkBox.checkState():
            mostrar_acumulado = True
        vector, estadisticas, largo_maximo_ant, largo_maximo_inm, largo_maximo_ll, vector_rk1, vector_rk2, vector_rk3 = principal(cant_dias,mostrar_desde, lambda_cercania, lambda_interp, lambda_ant, lambda_maq, lambda_critica, uniforme_min, uniforme_max, uniforme_min_enc, uniforme_max_enc, mostrar_acumulado, multiplicador_rk1, multiplicador_rk2, multiplicador_rk3)
        self.vector_rk1 = vector_rk1
        self.vector_rk2 = vector_rk2
        self.vector_rk3 = vector_rk3
        self.tabla.setColumnCount(43 + largo_maximo_ant + largo_maximo_inm + largo_maximo_ll)
        self.tabla.setRowCount(len(vector))

        self.cargarTabla(vector, largo_maximo_ant, largo_maximo_inm)
        self.cargarEstadisticas(estadisticas)
    def cargarTabla(self, vec_sim, largo_maximo, largo_maximo_inm):
        largo_linea = 44
        i = 0
        for linea in vec_sim:
            linea_como_lista = [linea.reloj, linea.evento,linea.est_ll, linea.rnd_ll, linea.t_ll, linea.h_ll, linea.rnd_tipo,
                                linea.tipo, linea.est_encuesta, linea.rnd_t_antenc_encuesta,
                                linea.t_atenc_encuesta, linea.h_atenc_encuesta, linea.est_vent_inm_1,
                                linea.est_vent_inm_2, linea.rnd_t_antenc_inm,
                                linea.t_atenc_inm, linea.h_atenc_inm_1, linea.h_atenc_inm_2, linea.est_maquina,
                                linea.rnd_t_antenc_maq,
                                linea.t_atenc_maq, linea.h_atenc_maq, linea.est_vent_ant, linea.rnd_t_antenc_ant,
                                linea.t_atenc_ant,
                                linea.h_atenc_ant, linea.cantidad_ant, linea.cantidad_inm, linea.cantidad_fin_paciencia,
                                linea.porcentaje_fin_paciencia,
                                linea.cantidad_encuesta, linea.porcentaje_encuesta, linea.t_acum_sistema,
                                linea.promedio_t_sistema,
                                linea.cant_entraron, linea.cantidad_salieron,linea.beta, linea.h_prox_detencion,
                                linea.rnd_tipo_detencion, linea.tipo_detencion, linea.h_fin_detencion_ll,
                                linea.h_fin_detencion_vent]
            for j in range(largo_linea-2):




                if type(linea_como_lista[j]) == float:
                    celda = str(round(linea_como_lista[j],2))

                elif linea_como_lista[j] == None:
                    celda = " "
                else:
                    celda = str(linea_como_lista[j])
                self.tabla.setItem(i, j, QtWidgets.QTableWidgetItem(celda))


            # Mostrar cola
            columna = 43
            for k in range(len(linea.cola_ant)):
                texto = f"{linea.cola_ant[k][0]} | {linea.cola_ant[k][1]} | {round(linea.cola_ant[k][2],2)}"
                self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
                columna += 1

            columna = 43 + largo_maximo
            texto = "XXXXXXXX"
            self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
            columna += 1

            for k in range(len(linea.cola_inm)):
                texto = f"{linea.cola_inm[k][0]} | {linea.cola_inm[k][1]} | {linea.cola_inm[k][2]} | {round(linea.cola_inm[k][3],2)}"
                self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
                columna += 1

            columna = 43 + largo_maximo + largo_maximo_inm
            texto = "XXXXXXXX"
            self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
            columna += 1

            for k in range(len(linea.cola_ll)):
                persona = linea.cola_ll[k]
                if persona[1] == "Cerc" or persona[1] == "Interp":
                    texto = f"{persona[0]} | {persona[1]} | {persona[2]} | {round(persona[3],2)}"
                else:
                    texto = f"{persona[0]} | {persona[1]} | {round(persona[2], 2)}"
                self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
                columna += 1



            i += 1

    def cargarEstadisticas(self, estadisticas):
        self.cant_no_atend.setText(str(round(estadisticas[0],2)))
        self.porc_no_atend.setText(str(round(estadisticas[1],2)))
        self.porc_encuesta.setText(str(round(estadisticas[2], 2)))
        self.prom_t_cola.setText(str(round(estadisticas[3], 2)))

    def mostrar_RK1(self):
        self.ventana1 = QtWidgets.QWidget()
        self.ui = Ui_ventana_RK1()
        self.ui.setupUi(self.ventana1, self.vector_rk1)






        self.ventana1.show()

    def mostrar_RK2(self):
        self.ventana2 = QtWidgets.QWidget()
        self.ui = Ui_ventana_RK2()
        self.ui.setupUi(self.ventana2, self.vector_rk2)



        self.ventana2.show()

    def mostrar_RK3(self):
        self.ventana3 = QtWidgets.QWidget()
        self.ui = Ui_ventana_RK3()
        self.ui.setupUi(self.ventana3,self.vector_rk3)



        self.ventana3.show()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())