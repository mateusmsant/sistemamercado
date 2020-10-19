from PyQt5 import QtCore, QtGui, QtWidgets
from alt_fornecedor import Ui_AltFornecedor
from remover_fornecedor import Ui_removeFornecedor
from adicionar_fornecedor import Ui_addFornecedor
import imagens
import sqlite3


class Ui_FornecedorWindow(object):
    def openAltFornecedorWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AltFornecedor()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddFornecedor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addFornecedor()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRemoveFornecedor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_removeFornecedor()
        self.ui.setupUi(self.window)
        self.window.show()

    def reloadFornecedores(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        result = c.execute("SELECT * FROM fornecedores")
        self.tableproduto.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableproduto.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableproduto.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.commit()
        c.close()

    def setupUi(self, FornecedorWindow):
        FornecedorWindow.setObjectName("FornecedorWindow")
        FornecedorWindow.resize(737, 582)
        FornecedorWindow.setMinimumSize(QtCore.QSize(737, 582))
        FornecedorWindow.setMaximumSize(QtCore.QSize(737, 582))
        FornecedorWindow.setStyleSheet("background-color: rgb(107, 107, 107)")
        self.aaa = QtWidgets.QWidget(FornecedorWindow)
        self.aaa.setStyleSheet("QLineEdit {\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:rgb(170, 170, 255)\n"
"}\n"

"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(85, 170, 255)\n"
"}")
        self.aaa.setObjectName("aaa")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.aaa)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content2 = QtWidgets.QFrame(self.aaa)
        self.content2.setMinimumSize(QtCore.QSize(719, 516))
        self.content2.setMaximumSize(QtCore.QSize(213213, 5000))
        self.content2.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(107, 107, 107);\n"
"\n"
"}")
        self.content2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content2.setObjectName("content2")
        self.frame_5 = QtWidgets.QFrame(self.content2)
        self.frame_5.setGeometry(QtCore.QRect(20, 10, 691, 498))
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(56456, 54654))
        self.frame_5.setStyleSheet("QFrame {\n"
"background-color: rgb(138, 138, 138);\n"
"color:rgb(51, 102, 153);"
"border-radius:20px;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(20, -70, 651, 631))
        self.frame_7.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:rgb(170, 170, 255)\n"
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
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tableproduto = QtWidgets.QTableWidget(self.frame_7)
        self.tableproduto.setGeometry(QtCore.QRect(20, 80, 1081, 311))
        self.tableproduto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableproduto.setRowCount(9)
        self.tableproduto.setColumnCount(5)
        self.tableproduto.setObjectName("tableproduto")
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(4, item)
        self.adicionarfornecedor = QtWidgets.QPushButton(self.frame_7)
        self.adicionarfornecedor.setGeometry(QtCore.QRect(0, 410, 201, 51))
        self.adicionarfornecedor.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.adicionarfornecedor.setObjectName("adicionarfornecedor")
        self.adicionarfornecedor.clicked.connect(self.openAddFornecedor)
        self.carregarfornecedores = QtWidgets.QPushButton(self.frame_7)
        self.carregarfornecedores.setGeometry(QtCore.QRect(430, 440, 201, 61))
        self.carregarfornecedores.setAutoFillBackground(False)
        self.carregarfornecedores.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.carregarfornecedores.setObjectName("carregarfornecedores")
        self.carregarfornecedores.clicked.connect(self.reloadFornecedores)
        self.removerfornecedor = QtWidgets.QPushButton(self.frame_7)
        self.removerfornecedor.setGeometry(QtCore.QRect(0, 480, 201, 51))
        self.removerfornecedor.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.removerfornecedor.setObjectName("removerfornecedor")
        self.removerfornecedor.clicked.connect(self.openRemoveFornecedor)
        self.alterarfornecedor = QtWidgets.QPushButton(self.frame_7)
        self.alterarfornecedor.setGeometry(QtCore.QRect(210, 440, 201, 61))
        self.alterarfornecedor.setAutoFillBackground(False)
        self.alterarfornecedor.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.alterarfornecedor.setObjectName("alterarfornecedor")
        self.alterarfornecedor.clicked.connect(self.openAltFornecedorWindow)
        self.verticalLayout.addWidget(self.content2)
        self.botbarasalways = QtWidgets.QFrame(self.aaa)
        self.botbarasalways.setMaximumSize(QtCore.QSize(16777215, 35))
        self.botbarasalways.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:5px;")
        self.botbarasalways.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botbarasalways.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botbarasalways.setObjectName("botbarasalways")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.botbarasalways)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nihilism = QtWidgets.QFrame(self.botbarasalways)
        self.nihilism.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nihilism.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nihilism.setObjectName("nihilism")
        self.horizontalLayout.addWidget(self.nihilism)
        self.nadaimporta = QtWidgets.QFrame(self.botbarasalways)
        self.nadaimporta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nadaimporta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nadaimporta.setObjectName("nadaimporta")
        self.horizontalLayout.addWidget(self.nadaimporta)
        self.kant = QtWidgets.QLabel(self.botbarasalways)
        self.kant.setStyleSheet("color:rgb(255,255,255);")
        self.kant.setObjectName("kant")
        self.horizontalLayout.addWidget(self.kant)
        self.verticalLayout.addWidget(self.botbarasalways)
        FornecedorWindow.setCentralWidget(self.aaa)
        self.actionFuncion_rios = QtWidgets.QAction(FornecedorWindow)
        self.actionFuncion_rios.setObjectName("actionFuncion_rios")
        self.actionProdutos = QtWidgets.QAction(FornecedorWindow)
        self.actionProdutos.setObjectName("actionProdutos")

        self.retranslateUi(FornecedorWindow)
        QtCore.QMetaObject.connectSlotsByName(FornecedorWindow)
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        result = c.execute("SELECT * FROM fornecedores")
        self.tableproduto.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableproduto.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableproduto.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.commit()
        c.close()

    def retranslateUi(self, FornecedorWindow):
        _translate = QtCore.QCoreApplication.translate
        FornecedorWindow.setWindowTitle(_translate("FornecedorWindow", "Fornecedores"))
        FornecedorWindow.setWindowIcon(QtGui.QIcon('icone.png'))
        item = self.tableproduto.horizontalHeaderItem(0)
        item.setText(_translate("FornecedorWindow", "Código"))
        item = self.tableproduto.horizontalHeaderItem(1)
        item.setText(_translate("FornecedorWindow", "Nome"))
        item = self.tableproduto.horizontalHeaderItem(2)
        item.setText(_translate("FornecedorWindow", "Email"))
        item = self.tableproduto.horizontalHeaderItem(3)
        item.setText(_translate("FornecedorWindow", "Cidade"))
        item = self.tableproduto.horizontalHeaderItem(4)
        item.setText(_translate("FornecedorWindow", "Segmento"))
        self.adicionarfornecedor.setText(_translate("FornecedorWindow", "Adicionar um fornecedor"))
        self.carregarfornecedores.setText(_translate("FornecedorWindow", "Atualizar fornecedores"))
        self.removerfornecedor.setText(_translate("FornecedorWindow", "Remover um fornecedor"))
        self.alterarfornecedor.setText(_translate("FornecedorWindow", "Alterar fornecedor"))
        self.kant.setText(_translate("FornecedorWindow", "                                Projeto de Introdução à Programação"))
        self.actionFuncion_rios.setText(_translate("FornecedorWindow", "Funcionários"))
        self.actionProdutos.setText(_translate("FornecedorWindow", "Produtos"))
        self.tableproduto.setColumnWidth(2, 200)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FornecedorWindow = QtWidgets.QMainWindow()
    ui = Ui_FornecedorWindow()
    ui.setupUi(FornecedorWindow)
    FornecedorWindow.show()
    sys.exit(app.exec_())
