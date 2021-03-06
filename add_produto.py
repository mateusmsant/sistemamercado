from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_AddProduto(object):   
    def rlyAddProd(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        codigo = self.linecodigo.text()
        nome = self.linhanome.text()
        preco = self.linepreco.text()
        marca = self.linhamarca.text()
        fornecedor = self.linhafornecedor.text()
        estoque_inicial = self.linhaestoqueinicial.text()

        # Existência do código
        query = f"SELECT codigo FROM produtos WHERE codigo = '{codigo}'"
        c.execute(query)
        result = c.fetchall()
        
        if not result and codigo.isnumeric():
            c.execute("""INSERT INTO produtos (codigo, nome, preço, marca, fornecedor, estoque) 
            VALUES (?,?,?,?,?,?)""", (
                codigo, nome, preco, marca, fornecedor, estoque_inicial))
                
            connection.commit()
            c.close()
        else:
            connection.commit()
            c.close()

    def setupUi(self, AddProduto):
        AddProduto.setObjectName("AddProduto")
        AddProduto.resize(530, 559)
        AddProduto.setMinimumSize(QtCore.QSize(540, 550))
        AddProduto.setMaximumSize(QtCore.QSize(540, 550))
        AddProduto.setStyleSheet("background-color: rgb(60,58,58);\n"
"border:50px")
        self.centralwidget = QtWidgets.QWidget(AddProduto)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("QLineEdit {\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(157, 192, 225)\n"
"}\n"
"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(85, 170, 255)\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: rgb(170,170,255)}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(483, 462))
        self.frame_4.setMaximumSize(QtCore.QSize(483, 462))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.linhaestoqueinicial = QtWidgets.QLineEdit(self.frame_4)
        self.linhaestoqueinicial.setGeometry(QtCore.QRect(260, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.linhaestoqueinicial.setFont(font)
        self.linhaestoqueinicial.setObjectName("linhaestoqueinicial")
        self.linepreco = QtWidgets.QLineEdit(self.frame_4)
        self.linepreco.setGeometry(QtCore.QRect(30, 160, 201, 31))
        self.linepreco.setObjectName("linepreco")
        self.linhamarca = QtWidgets.QLineEdit(self.frame_4)
        self.linhamarca.setGeometry(QtCore.QRect(260, 160, 201, 31))
        self.linhamarca.setObjectName("linhamarca")
        self.linhafornecedor = QtWidgets.QLineEdit(self.frame_4)
        self.linhafornecedor.setGeometry(QtCore.QRect(30, 220, 201, 31))
        self.linhafornecedor.setObjectName("linhafornecedor")
        self.linhanome = QtWidgets.QLineEdit(self.frame_4)
        self.linhanome.setGeometry(QtCore.QRect(260, 100, 201, 31))
        self.linhanome.setObjectName("linhanome")
        self.linecodigo = QtWidgets.QLineEdit(self.frame_4)
        self.linecodigo.setGeometry(QtCore.QRect(30, 100, 201, 31))
        self.linecodigo.setReadOnly(False)
        self.linecodigo.setObjectName("linecodigo")
        self.botaoaddproduto = QtWidgets.QPushButton(self.frame_4)
        self.botaoaddproduto.setGeometry(QtCore.QRect(140, 300, 200, 40))
        self.botaoaddproduto.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255,255,255);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:10px;\n"
"    color:rgb(170, 170, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:10px;\n"
"}")
        self.botaoaddproduto.setObjectName("botaoaddproduto")
        self.botaoaddproduto.clicked.connect(self.rlyAddProd)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.bottom_bar = QtWidgets.QFrame(self.centralwidget)
        self.bottom_bar.setMinimumSize(QtCore.QSize(50, 45))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom_bar.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.bottom_bar)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(290, 0, 211, 25))
        self.label_7.setMaximumSize(QtCore.QSize(211, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setStyleSheet("color:rgb(240, 240, 240);\n"
"text-align:right;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.bottom_bar)
        AddProduto.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddProduto)
        QtCore.QMetaObject.connectSlotsByName(AddProduto)

    def retranslateUi(self, AddProduto):
        _translate = QtCore.QCoreApplication.translate
        AddProduto.setWindowTitle(_translate("AddProduto", "Adicionar produto"))
        AddProduto.setWindowIcon(QtGui.QIcon('icone.png'))
        self.linhaestoqueinicial.setPlaceholderText(_translate("AddProduto", "                    Estoque inicial"))
        self.linepreco.setPlaceholderText(_translate("AddProduto", "                           Preço"))
        self.linhamarca.setPlaceholderText(_translate("AddProduto", "                          Marca"))
        self.linhafornecedor.setPlaceholderText(_translate("AddProduto", "                      Fornecedor"))
        self.linhanome.setPlaceholderText(_translate("AddProduto", "                          Nome"))
        self.linecodigo.setPlaceholderText(_translate("AddProduto", "                          Código"))
        self.botaoaddproduto.setText(_translate("AddProduto", "Adicionar produto"))
        self.label_7.setText(_translate("AddProduto", "Projeto de Introdução à Programação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AddProduto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
