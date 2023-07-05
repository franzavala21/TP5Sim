import random
from Fila import *
from Eventos import *

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
        mostrar_acumulado = False
        if self.checkBox.checkState():
            mostrar_acumulado = True
        vector, estadisticas, largo_maximo_ant, largo_maximo_inm = principal(cant_dias,mostrar_desde, lambda_cercania, lambda_interp, lambda_ant, lambda_maq, lambda_critica, uniforme_min, uniforme_max, uniforme_min_enc, uniforme_max_enc, mostrar_acumulado)
        self.tabla.setColumnCount(38 + largo_maximo_ant + largo_maximo_inm)
        self.tabla.setRowCount(len(vector))

        self.cargarTabla(vector, largo_maximo_ant)
        self.cargarEstadisticas(estadisticas)
    def cargarTabla(self, vec_sim, largo_maximo):
        largo_linea = 37
        i = 0
        for linea in vec_sim:
            for j in range(largo_linea-2):
                linea_como_lista = [linea.reloj, linea.evento, linea.rnd_ll, linea.t_ll,linea.h_ll, linea.rnd_tipo,
                linea.tipo, linea.est_encuesta, linea.rnd_t_antenc_encuesta,
                linea.t_atenc_encuesta, linea.h_atenc_encuesta,linea.est_vent_inm_1, linea.est_vent_inm_2,linea.rnd_t_antenc_inm,
                linea.t_atenc_inm,linea.h_atenc_inm_1,linea.h_atenc_inm_2,linea.est_maquina,linea.rnd_t_antenc_maq,
                linea.t_atenc_maq,linea.h_atenc_maq,linea.est_vent_ant,linea.rnd_t_antenc_ant,linea.t_atenc_ant,
                linea.h_atenc_ant,linea.cantidad_ant, linea.cantidad_inm, linea.cantidad_fin_paciencia, linea.porcentaje_fin_paciencia,
                                    linea.cantidad_encuesta, linea.porcentaje_encuesta, linea.t_acum_sistema, linea.promedio_t_sistema,
                                    linea.cant_entraron, linea.cantidad_salieron]

                if type(linea_como_lista[j]) == float:
                    celda = str(round(linea_como_lista[j],2))

                elif linea_como_lista[j] == None:
                    celda = " "
                else:
                    celda = str(linea_como_lista[j])
                self.tabla.setItem(i, j, QtWidgets.QTableWidgetItem(celda))


            # Mostrar cola
            columna = 35
            for k in range(len(linea.cola_ant)):
                texto = f"{linea.cola_ant[k][0]} | {linea.cola_ant[k][1]} | {round(linea.cola_ant[k][2],2)}"
                self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
                columna += 1

            columna = 35 + largo_maximo
            texto = "XXXXXXXX"
            self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
            columna += 1

            for k in range(len(linea.cola_inm)):
                texto = f"{linea.cola_inm[k][0]} | {linea.cola_inm[k][1]} | {linea.cola_inm[k][2]} | {round(linea.cola_inm[k][3],2)}"
                self.tabla.setItem(i, columna, QtWidgets.QTableWidgetItem(texto))
                columna += 1

            i += 1

    def cargarEstadisticas(self, estadisticas):
        self.cant_no_atend.setText(str(round(estadisticas[0],2)))
        self.porc_no_atend.setText(str(round(estadisticas[1],2)))
        self.porc_encuesta.setText(str(round(estadisticas[2], 2)))
        self.prom_t_cola.setText(str(round(estadisticas[3], 2)))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())