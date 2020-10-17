from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
textos = ''
soma_produtos = 0


class Ui_CaixaWindow(object):
    def emailParaFornecedor(self):
        import email
        import smtplib
        import sqlite3

        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        c.execute(f'SELECT fornecedor FROM produtos WHERE estoque > 5')
        nomeFornecedor = c.fetchone()

        for nomeReal in nomeFornecedor:
            c.execute(f"SELECT email FROM fornecedores WHERE nome = '{nomeReal}'")
            emailFornecedor = c.fetchone()

        for emailReal in emailFornecedor:
            c.execute(f'SELECT nome FROM produtos WHERE estoque > 5')
            nomeProduto = c.fetchone()

        for produtoReal in nomeProduto:
            nomeDoProdutoDesejado = produtoReal

        msg = email.message_from_string(
            f"Oi {nomeReal}. O Supermercado Try precisa de 50 unidades de {nomeDoProdutoDesejado}.")
        msg2 = email.message_from_string(f"Aguardo seu retorno sobre a disponibilidade. Grato!")
        msg['From'] = "trysupermercado@hotmail.com"
        msg['To'] = str(emailReal)
        msg['Subject'] = "Pedido de compra - Supermercado Try"

        s = smtplib.SMTP("smtp.live.com", 587)
        s.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        s.starttls()  # Puts connection to SMTP server in TLS mode
        s.ehlo()
        s.login('trysupermercado@hotmail.com', '9piu4exx')
        s.sendmail("trysupermercado@hotmail.com", str(emailReal), msg.as_string() + msg2.as_string())

        s.quit()

    def addItem(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()
      
        codigo1 = self.lineEdit.text()
        quantidade1 = self.lineEdit_2.text()
        global textos
        global soma_produtos
        if codigo1.isnumeric() and quantidade1.isnumeric():
            codigo = int(codigo1)
            quantidade = int(quantidade1)

            c.execute(f"SELECT estoque FROM produtos WHERE codigo = '{codigo}'")
            estoquefetch = c.fetchone()
            if estoquefetch:
                for estoqueatual in estoquefetch:
                    estoque = estoqueatual - quantidade
                    if estoque < 0:
                        self.oper.setText('Não há mais esse produto no estoque.')
                        break

                    c.execute(f"UPDATE produtos SET estoque = '{estoqueatual - quantidade}' WHERE codigo = '{codigo}'")
                    connection.commit()
                    c.execute(f"SELECT preço FROM produtos WHERE codigo = '{codigo}'")
                    get = c.fetchone()




                    if get and quantidade > 0:
                        for item in get:
                            resultado = item * quantidade
                            soma_produtos += resultado
                            c.execute(f"SELECT nome FROM produtos WHERE codigo = '{codigo}'")
                            nome = c.fetchone()
                            for name in nome:
                                tobeshow = f'Você adicionou {quantidade} do item {name}. Valor a ser pago: {resultado}. \n Estoque: {estoque}. \n'
                                textos += tobeshow
                            
                        self.oper.setText(textos)
                        connection.commit()
                        c.close()

            else:
                if quantidade > 0:
                    self.oper.setText('Você não digitou um código existente. ')

                else:
                    self.oper.setText('Você não digitou um código existente, nem uma quantidade válida. ')


        elif codigo1 == '' or quantidade1 == '':
            self.oper.setText('Há espaços vazios. ')
 
        else:
            for num in codigo1:
                if num == '-':
                    self.oper.setText('Você não pode digitar um código ou uma quantidade negativa. ')

            for num1 in quantidade1:
                if num1 == '-':
                    self.oper.setText('Você não pode digitar um código ou uma quantidade negativa. ')

        if estoque < 10:
            self.emailParaFornecedor()


    def reset(self):
        self.oper.setText(' ')
        self.total.setText('')
        global textos
        textos = ' '
        global soma_produtos
        soma_produtos = 0

        

    def showTotal(self):
        if not self.trocodef.text():
            text = f'    Total da compra: R$ {soma_produtos}.'
            self.total.setText(text)
        else:
            diferenca = float(self.trocodef.text()) - soma_produtos
            if diferenca > 0:
                text = f'    O cliente receberá R$ {round(diferenca, 2)} de troco. Total da compra: R$ {soma_produtos}.'
                self.total.setText(text)
            elif diferenca < 0:
                text = f'    O cliente não pode comprar mais do que pode pagar.'
                self.total.setText(text)
            elif diferenca == 0:
                text = f'    Não há troco. Total da compra: R$ {soma_produtos}'
                self.total.setText(text)


    def setupUi(self, CaixaWindow):
        CaixaWindow.setObjectName("CaixaWindow")
        CaixaWindow.resize(923, 644)
        CaixaWindow.setMaximumSize(QtCore.QSize(923, 644))
        CaixaWindow.setStyleSheet("color:rgb(170, 170, 255);\n"
"background-color: rgb(115, 115, 115);\n"
"")
        self.centralwidget = QtWidgets.QWidget(CaixaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(107, 107, 107);\n"
"    border-radius:30px;\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(255,255,255);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:10px;\n"
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
"}\n"
"QLineEdit {\n"
"    border:2px solid rgb(255, 255, 255);\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(620, 230, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addItem)
        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(620, 470, 171, 51))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.showTotal)
        self.pushButton3 = QtWidgets.QPushButton(self.frame)
        self.pushButton3.setGeometry(QtCore.QRect(620, 520, 171, 51))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.reset)
        self.trocodef = QtWidgets.QLineEdit(self.frame)
        self.trocodef.setGeometry(QtCore.QRect(540, 420, 330, 41))
        self.trocodef.setObjectName("trocodef")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(540, 100, 321, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 160, 321, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 10, 471, 541))
        self.frame_2.setStyleSheet("background-color:rgb(179, 179, 179);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.oper = QtWidgets.QLabel(self.frame_2)
        self.oper.setGeometry(QtCore.QRect(10, 10, 451, 441))
        self.oper.setStyleSheet("background-color: rgb(156, 156, 156); color:rgb(30, 0, 0); font-weight: bold")
        self.oper.setObjectName("oper")
        self.total = QtWidgets.QLabel(self.frame_2)
        self.total.setGeometry(QtCore.QRect(10, 460, 451, 61))
        self.total.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:20px;"
"font-weight:bold;"
"text-size:30px;")
        self.total.setObjectName("total")
        self.verticalLayout.addWidget(self.frame)
        self.bottom_bar = QtWidgets.QFrame(self.centralwidget)
        self.bottom_bar.setMinimumSize(QtCore.QSize(50, 2))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom_bar.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.bottom_bar)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.bottom_bar)
        self.label.setEnabled(False)
        self.label.setMaximumSize(QtCore.QSize(211, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color:rgb(240, 240, 240);\n"
"text-align:right;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.bottom_bar)
        CaixaWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(CaixaWindow)
        QtCore.QMetaObject.connectSlotsByName(CaixaWindow)

    def retranslateUi(self, CaixaWindow):
        _translate = QtCore.QCoreApplication.translate
        CaixaWindow.setWindowTitle(_translate("CaixaWindow", "Operações de caixa"))
        CaixaWindow.setWindowIcon(QtGui.QIcon('icone.png'))
        self.pushButton.setText(_translate("CaixaWindow", "Adicionar"))
        self.pushButton2.setText(_translate("CaixaWindow", "Calcular"))
        self.pushButton3.setText(_translate("CaixaWindow", "Resetar"))

        self.trocodef.setPlaceholderText(_translate("CaixaWindow", "Se o pagamento for em espécie, digite quanto o cliente irá dar."))
        self.lineEdit.setPlaceholderText(_translate("CaixaWindow", "                                    Código do produto"))
        self.lineEdit_2.setPlaceholderText(_translate("CaixaWindow", "                                 Quantidade do produto"))
        self.label.setText(_translate("CaixaWindow", "Projeto de Introdução à Programação"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CaixaWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    