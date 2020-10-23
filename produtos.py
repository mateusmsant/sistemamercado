from PyQt5 import QtCore, QtGui, QtWidgets
from alt_produto import Ui_AlterarProduto
from add_produto import Ui_AddProduto
from remover_produto import Ui_RemoveProdutoWindow
import sqlite3
import imagens

class Ui_ProdutosWindow(object):
    def openCodigoAltWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AlterarProduto()
        self.ui.setupUi(self.window)
        self.window.show()
       

    def openAddProdutoWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddProduto()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRemoveProdutoWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RemoveProdutoWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def reloadProd(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        result = c.execute("SELECT * FROM produtos")
        self.tableproduto.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableproduto.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableproduto.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.commit()
        c.close()


    def setupUi(self, ProdutosWindow):
        ProdutosWindow.setObjectName("ProdutosWindow")
        ProdutosWindow.resize(737, 582)
        ProdutosWindow.setMinimumSize(QtCore.QSize(737, 582))
        ProdutosWindow.setMaximumSize(QtCore.QSize(737, 582))
        ProdutosWindow.setStyleSheet("background-color: rgb(107, 107, 107)")
        self.filosofiakantiana = QtWidgets.QWidget(ProdutosWindow)
        self.filosofiakantiana.setStyleSheet("QLineEdit {\n"
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
        self.filosofiakantiana.setObjectName("filosofiakantiana")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.filosofiakantiana)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content2 = QtWidgets.QFrame(self.filosofiakantiana)
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
"color:rgb(51, 102, 153);\n"
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
        self.tableproduto.setGeometry(QtCore.QRect(0, 90, 1081, 311))
        self.tableproduto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableproduto.setRowCount(5)
        self.tableproduto.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableproduto.setHorizontalHeaderItem(5, item)
        self.tableproduto.setColumnWidth(0, 50)
        self.tableproduto.setColumnWidth(1, 180)



        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        result = c.execute("SELECT * FROM produtos")
        self.tableproduto.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableproduto.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableproduto.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.commit()
        c.close()

        self.addproduto = QtWidgets.QPushButton(self.frame_7)
        self.addproduto.setGeometry(QtCore.QRect(0, 410, 201, 51))
        self.addproduto.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.addproduto.setObjectName("addproduto")
        self.addproduto.clicked.connect(self.openAddProdutoWindow)
        self.loadproduto = QtWidgets.QPushButton(self.frame_7)
        self.loadproduto.setGeometry(QtCore.QRect(415, 430, 201, 81))
        self.loadproduto.setAutoFillBackground(False)
        self.loadproduto.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.loadproduto.setObjectName("loadproduto")
        self.loadproduto.clicked.connect(self.reloadProd)
        self.altproduto = QtWidgets.QPushButton(self.frame_7)
        self.altproduto.setGeometry(QtCore.QRect(210, 430, 200, 81))
        self.altproduto.setAutoFillBackground(False)
        self.altproduto.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.altproduto.setObjectName("altproduto")
        self.altproduto.clicked.connect(self.openCodigoAltWindow)
        self.removeproduto = QtWidgets.QPushButton(self.frame_7)
        self.removeproduto.setGeometry(QtCore.QRect(0, 480, 201, 51))
        self.removeproduto.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.removeproduto.setObjectName("removeproduto")
        self.removeproduto.clicked.connect(self.openRemoveProdutoWindow)
        self.verticalLayout.addWidget(self.content2)
        self.botbarasalways = QtWidgets.QFrame(self.filosofiakantiana)
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
        ProdutosWindow.setCentralWidget(self.filosofiakantiana)
        self.actionFuncion_rios = QtWidgets.QAction(ProdutosWindow)
        self.actionFuncion_rios.setObjectName("actionFuncion_rios")
        self.actionProdutos = QtWidgets.QAction(ProdutosWindow)
        self.actionProdutos.setObjectName("actionProdutos")

        self.retranslateUi(ProdutosWindow)
        QtCore.QMetaObject.connectSlotsByName(ProdutosWindow)

    def retranslateUi(self, ProdutosWindow):
        _translate = QtCore.QCoreApplication.translate
        ProdutosWindow.setWindowTitle(_translate("ProdutosWindow", "Produtos"))
        ProdutosWindow.setWindowIcon(QtGui.QIcon('icone.png'))
        item = self.tableproduto.horizontalHeaderItem(0)
        item.setText(_translate("ProdutosWindow", "Código"))
        item = self.tableproduto.horizontalHeaderItem(1)
        item.setText(_translate("ProdutosWindow", "Nome"))
        item = self.tableproduto.horizontalHeaderItem(2)
        item.setText(_translate("ProdutosWindow", "Preço"))
        item = self.tableproduto.horizontalHeaderItem(3)
        item.setText(_translate("ProdutosWindow", "Marca"))
        item = self.tableproduto.horizontalHeaderItem(4)
        item.setText(_translate("ProdutosWindow", "Fornecedor"))
        item = self.tableproduto.horizontalHeaderItem(5)
        item.setText(_translate("ProdutosWindow", "Estoque"))
        self.addproduto.setText(_translate("ProdutosWindow", "Adicionar um produtos"))
        self.loadproduto.setText(_translate("ProdutosWindow", "Recarregar produtos"))
        self.altproduto.setText(_translate("ProdutosWindow", "Alterar produtos"))
        self.removeproduto.setText(_translate("ProdutosWindow", "Remover um produto"))
        self.kant.setText(_translate("ProdutosWindow", "                                Projeto de Introdução à Programação"))
        self.actionFuncion_rios.setText(_translate("ProdutosWindow", "Funcionários"))
        self.actionProdutos.setText(_translate("ProdutosWindow", "Produtos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddFuncWindow = QtWidgets.QMainWindow()
    ui = Ui_ProdutosWindow()
    ui.setupUi(AddFuncWindow)
    AddFuncWindow.show()
    sys.exit(app.exec_())
