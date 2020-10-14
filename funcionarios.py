from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from alt_funcionario import Ui_AltFuncWindow
from add_funcionario import Ui_AddFuncWindow
from remover_funcionario import Ui_RemoveFuncWindow


class Ui_FuncWindow(object):
    def openWindowAltFuncionario(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AltFuncWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def reloadFuncionarios(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        result = c.execute("SELECT * FROM funcionarios")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.commit()
        connection.close()


    def openWindowAddFuncionario(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddFuncWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowRemoverFuncionario(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RemoveFuncWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 760)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 760))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 760))
        MainWindow.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"border-radius:60px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:rgb(190, 170, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"QPushButton:focus {\n"
"    border: 3px solid rgb(85, 170, 255)\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(85, 170, 255)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content2 = QtWidgets.QFrame(self.centralwidget)
        self.content2.setMinimumSize(QtCore.QSize(500, 500))
        self.content2.setMaximumSize(QtCore.QSize(5000, 5000))
        self.content2.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(107, 107, 107);\n"
"    border-radius:60px;\n"
"}")
        self.content2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content2.setObjectName("content2")
        self.frame_4 = QtWidgets.QFrame(self.content2)
        self.frame_4.setGeometry(QtCore.QRect(10, 20, 1081, 691))
        self.frame_4.setStyleSheet("QFrame {\n"
"background-color: rgb(138, 138, 138);\n"
"color: rgb(170, 170, 255);\n"
"border-radius:60px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(0, 10, 1061, 691))
        self.frame_6.setStyleSheet("color:rgb(170, 170, 255)")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 1041, 491))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.reload_info = QtWidgets.QPushButton(self.frame_6)
        self.reload_info.setGeometry(QtCore.QRect(750, 560, 201, 51))
        self.reload_info.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.reload_info.setObjectName("Recarregar dados")
        self.reload_info.clicked.connect(self.reloadFuncionarios)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(20, 530, 200, 50))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindowAddFuncionario)
        self.altfunc = QtWidgets.QPushButton(self.frame_6)
        self.altfunc.setGeometry(QtCore.QRect(300, 550, 200, 80))
        self.altfunc.setAutoFillBackground(False)
        self.altfunc.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.altfunc.setObjectName("altfunc")
        self.altfunc.clicked.connect(self.openWindowAltFuncionario)
        self.remove_func = QtWidgets.QPushButton(self.frame_6)
        self.remove_func.setGeometry(QtCore.QRect(20, 610, 201, 51))
        self.remove_func.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.remove_func.setObjectName("remove_func")
        self.remove_func.clicked.connect(self.openWindowRemoverFuncionario)
        self.verticalLayout.addWidget(self.content2)
        self.bot_bar121313 = QtWidgets.QFrame(self.centralwidget)
        self.bot_bar121313.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bot_bar121313.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:5px;")
        self.bot_bar121313.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bot_bar121313.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_bar121313.setObjectName("bot_bar121313")
        self.botladoesquerdo = QtWidgets.QFrame(self.bot_bar121313)
        self.botladoesquerdo.setGeometry(QtCore.QRect(10, 10, 120, 80))
        self.botladoesquerdo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botladoesquerdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botladoesquerdo.setObjectName("botladoesquerdo")
        self.botladodireito = QtWidgets.QFrame(self.bot_bar121313)
        self.botladodireito.setGeometry(QtCore.QRect(470, 0, 491, 31))
        self.botladodireito.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botladodireito.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botladodireito.setObjectName("botladodireito")
        self.label = QtWidgets.QLabel(self.bot_bar121313)
        self.label.setGeometry(QtCore.QRect(910, 0, 301, 31))
        self.label.setStyleSheet("color:rgb(255,255,255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.bot_bar121313)
        MainWindow.setCentralWidget(self.centralwidget)


        
        connection = sqlite3.connect('supermercado.db')
        query = "SELECT * FROM funcionarios"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Funcionários"))
        MainWindow.setWindowIcon(QtGui.QIcon('icone.png'))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data de Nascimento"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Celular"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Login"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Senha"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Rua"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Número"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Cidade"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Classe"))
        self.reload_info.setText(_translate("MainWindow", "Recarregar funcionários"))
        self.pushButton.setText(_translate("MainWindow", "Adicionar um funcionário"))
        self.altfunc.setText(_translate("MainWindow", "Alterar um funcionário"))

        self.remove_func.setText(_translate("MainWindow", "Remover um funcionário"))
        self.label.setText(_translate("MainWindow", "Projeto de Introdução à Programação"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FuncWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
