# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_RK3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_RK3(object):
    def setupUi(self, ventana_RK3, vector_rk3):
        ventana_RK3.setObjectName("ventana_RK3")
        ventana_RK3.resize(1030, 641)
        self.tabla3 = QtWidgets.QTableWidget(ventana_RK3)
        self.tabla3.setGeometry(QtCore.QRect(5, 30, 1020, 611))
        self.tabla3.setObjectName("tabla3")
        self.tabla3.setColumnCount(7)
        self.tabla3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla3.setHorizontalHeaderItem(6, item)

        self.tabla3.setColumnWidth(0, 50)
        self.tabla3.setColumnWidth(1, 150)
        self.tabla3.setColumnWidth(2, 150)
        self.tabla3.setColumnWidth(3, 150)
        self.tabla3.setColumnWidth(4, 150)
        self.tabla3.setColumnWidth(5, 150)
        self.tabla3.setColumnWidth(6, 150)

        self.retranslateUi(ventana_RK3)
        QtCore.QMetaObject.connectSlotsByName(ventana_RK3)

        self.tabla3.setRowCount(len(vector_rk3))
        self.tabla3.setColumnCount(7)
        for i in range (len(vector_rk3)):
            for i in range(len(vector_rk3)):
                self.tabla3.setItem(i, 0, QtWidgets.QTableWidgetItem(str(vector_rk3[i][0])))
                self.tabla3.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vector_rk3[i][1])))
                self.tabla3.setItem(i, 2, QtWidgets.QTableWidgetItem(str(vector_rk3[i][2])))
                self.tabla3.setItem(i, 3, QtWidgets.QTableWidgetItem(str(vector_rk3[i][5])))
                self.tabla3.setItem(i, 4, QtWidgets.QTableWidgetItem(str(vector_rk3[i][8])))
                self.tabla3.setItem(i, 5, QtWidgets.QTableWidgetItem(str(vector_rk3[i][11])))
                self.tabla3.setItem(i, 6, QtWidgets.QTableWidgetItem(str(vector_rk3[i][12])))

    def retranslateUi(self, ventana_RK3):
        _translate = QtCore.QCoreApplication.translate
        ventana_RK3.setWindowTitle(_translate("ventana_RK3", "Tabla Runge Kutta 3"))
        item = self.tabla3.horizontalHeaderItem(0)
        item.setText(_translate("ventana_RK3", "t"))
        item = self.tabla3.horizontalHeaderItem(1)
        item.setText(_translate("ventana_RK3", "A"))
        item = self.tabla3.horizontalHeaderItem(2)
        item.setText(_translate("ventana_RK3", "k1"))
        item = self.tabla3.horizontalHeaderItem(3)
        item.setText(_translate("ventana_RK3", "k2"))
        item = self.tabla3.horizontalHeaderItem(4)
        item.setText(_translate("ventana_RK3", "k3"))
        item = self.tabla3.horizontalHeaderItem(5)
        item.setText(_translate("ventana_RK3", "k4"))
        item = self.tabla3.horizontalHeaderItem(6)
        item.setText(_translate("ventana_RK3", "An+1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_RK3 = QtWidgets.QWidget()
    ui = Ui_ventana_RK3()
    ui.setupUi(ventana_RK3)
    ventana_RK3.show()
    sys.exit(app.exec_())
