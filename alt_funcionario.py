from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_AltFuncWindow(object):
    def saveChangesToFunc(self):       
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        cpfpraseralterado = self.linha_cpf.text()

        if self.linha_nome.text():
            novo_nome = self.linha_nome.text()
            query = f"UPDATE funcionarios SET nome = '{novo_nome}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_sexo.text():
            novo_sexo = self.linha_sexo.text()
            query = f"UPDATE funcionarios SET sexo = '{novo_sexo}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_data.text():
            nova_data = self.linha_data.text()
            query = f"UPDATE funcionarios SET datanascimento = '{nova_data}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_telefone.text():
            novo_telefone = self.linha_telefone.text()
            query = f"UPDATE funcionarios SET telefone = '{novo_telefone}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_celular.text():
            novo_celular = self.linha_celular.text()
            query = f"UPDATE funcionarios SET celular = '{novo_celular}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_email.text():
            novo_email = self.linha_email.text()
            query = f"UPDATE funcionarios SET email = '{novo_email}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_usuario.text():
            novo_userlogin = self.linha_usuario.text()
            query = f"UPDATE funcionarios SET userlogin = '{novo_userlogin}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_senha.text():
            nova_senha = self.linha_senha.text()
            query = f"UPDATE funcionarios SET userpassword = '{nova_senha}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_rua.text():
            nova_rua = self.linha_rua.text()
            query = f"UPDATE funcionarios SET rua = '{nova_rua}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_rua_2.text():
            novo_numero = self.linha_rua_2.text()
            query = f"UPDATE funcionarios SET numero = '{novo_numero}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_bairro.text():
            novo_bairro = self.linha_bairro.text()
            query = f"UPDATE funcionarios SET bairro = '{novo_bairro}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_cidade.text():
            novo_cidade = self.linha_cidade.text()
            query = f"UPDATE funcionarios SET cidade = '{novo_cidade}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 
        if self.linha_classe.text():
            nova_classe = self.linha_classe.text()
            query = f"UPDATE funcionarios SET classe = '{nova_classe}' WHERE cpf = '{cpfpraseralterado}'"
            c.execute(query)
 

        connection.commit()
        c.close()

    def setupUi(self, AltFuncWindow):
        AltFuncWindow.setObjectName("AltFuncWindow")
        AltFuncWindow.resize(532, 547)
        AltFuncWindow.setMinimumSize(QtCore.QSize(532, 547))

        AltFuncWindow.setMaximumSize(QtCore.QSize(532, 547))
        AltFuncWindow.setStyleSheet("background-color: rgb(60,58,58);\n"
"border:50px")
        self.centralwidget = QtWidgets.QWidget(AltFuncWindow)
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
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(280, 0, 261, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.linha_rua = QtWidgets.QLineEdit(self.frame_3)
        self.linha_rua.setGeometry(QtCore.QRect(20, 50, 201, 31))
        self.linha_rua.setReadOnly(False)
        self.linha_rua.setObjectName("linha_rua")
        self.linha_bairro = QtWidgets.QLineEdit(self.frame_3)
        self.linha_bairro.setGeometry(QtCore.QRect(20, 130, 201, 31))
        self.linha_bairro.setObjectName("linha_bairro")
        self.linha_cidade = QtWidgets.QLineEdit(self.frame_3)
        self.linha_cidade.setGeometry(QtCore.QRect(20, 170, 201, 31))
        self.linha_cidade.setObjectName("linha_cidade")
        self.linha_rua_2 = QtWidgets.QLineEdit(self.frame_3)
        self.linha_rua_2.setGeometry(QtCore.QRect(20, 90, 201, 31))
        self.linha_rua_2.setObjectName("linha_rua_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(280, 230, 271, 191))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.linha_email = QtWidgets.QLineEdit(self.frame_4)
        self.linha_email.setGeometry(QtCore.QRect(20, 140, 191, 31))
        self.linha_email.setObjectName("linha_email")
        self.linha_telefone = QtWidgets.QLineEdit(self.frame_4)
        self.linha_telefone.setGeometry(QtCore.QRect(20, 40, 191, 31))
        self.linha_telefone.setObjectName("linha_telefone")
        self.linha_celular = QtWidgets.QLineEdit(self.frame_4)
        self.linha_celular.setGeometry(QtCore.QRect(20, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.linha_celular.setFont(font)
        self.linha_celular.setObjectName("linha_celular")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 230, 281, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.linha_usuario = QtWidgets.QLineEdit(self.frame_2)
        self.linha_usuario.setGeometry(QtCore.QRect(20, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.linha_usuario.setFont(font)
        self.linha_usuario.setObjectName("linha_usuario")
        self.linha_senha = QtWidgets.QLineEdit(self.frame_2)
        self.linha_senha.setGeometry(QtCore.QRect(20, 90, 201, 31))
        self.linha_senha.setObjectName("linha_senha")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.linha_classe = QtWidgets.QLineEdit(self.frame_2)
        self.linha_classe.setGeometry(QtCore.QRect(20, 140, 201, 31))
        self.linha_classe.setObjectName("linha_classe")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.botaoAltFunc = QtWidgets.QPushButton(self.frame)
        self.botaoAltFunc.setGeometry(QtCore.QRect(295, 430, 200, 40))
        self.botaoAltFunc.setStyleSheet("QPushButton {\n"
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
        self.botaoAltFunc.setObjectName("botaoAltFunc")
        self.botaoAltFunc.clicked.connect(self.saveChangesToFunc)

        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 281, 231))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.linha_sexo = QtWidgets.QLineEdit(self.frame_5)
        self.linha_sexo.setGeometry(QtCore.QRect(30, 160, 181, 31))
        self.linha_sexo.setObjectName("linha_sexo")
        self.linha_cpf = QtWidgets.QLineEdit(self.frame_5)
        self.linha_cpf.setGeometry(QtCore.QRect(30, 0, 181, 31))
        self.linha_cpf.setObjectName("linha_cpf")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.linha_nome = QtWidgets.QLineEdit(self.frame_5)
        self.linha_nome.setGeometry(QtCore.QRect(30, 75, 181, 31))
        self.linha_nome.setText("")
        self.linha_nome.setObjectName("linha_nome")
        self.linha_data = QtWidgets.QLineEdit(self.frame_5)
        self.linha_data.setGeometry(QtCore.QRect(30, 120, 181, 31))
        self.linha_data.setObjectName("linha_data")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 430, 200, 41))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color:rgb(255,255,255)")
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
        AltFuncWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AltFuncWindow)
        QtCore.QMetaObject.connectSlotsByName(AltFuncWindow)

    def retranslateUi(self, AltFuncWindow):
        _translate = QtCore.QCoreApplication.translate
        AltFuncWindow.setWindowTitle(_translate("AddFuncWindow", "Alterar funcionário"))
        AltFuncWindow.setWindowIcon(QtGui.QIcon('icone.png'))
        self.label_4.setText(_translate("AltFuncWindow", "Endereço"))
        self.linha_rua.setPlaceholderText(_translate("AltFuncWindow", "                            Rua"))
        self.linha_bairro.setPlaceholderText(_translate("AltFuncWindow", "                           Bairro"))
        self.linha_cidade.setPlaceholderText(_translate("AltFuncWindow", "                          Cidade"))
        self.linha_rua_2.setPlaceholderText(_translate("AltFuncWindow", "                         Número"))
        self.label_2.setText(_translate("AltFuncWindow", "Contato"))
        self.linha_email.setPlaceholderText(_translate("AltFuncWindow", "                         Email"))
        self.linha_telefone.setPlaceholderText(_translate("AltFuncWindow", "                      Telefone"))
        self.linha_celular.setPlaceholderText(_translate("AltFuncWindow", "                        Celular"))
        self.linha_usuario.setPlaceholderText(_translate("AltFuncWindow", "                        Usuário"))
        self.linha_senha.setPlaceholderText(_translate("AltFuncWindow", "                         Senha"))
        self.linha_classe.setPlaceholderText(_translate("AltFuncWindow", "           Administrador/Operador"))
        self.label_3.setText(_translate("AltFuncWindow", "Dados de login"))
        self.botaoAltFunc.setText(_translate("AltFuncWindow", "Alterar funcionário"))
        self.linha_sexo.setPlaceholderText(_translate("AltFuncWindow", "                        Sexo"))
        self.linha_cpf.setPlaceholderText(_translate("AltFuncWindow", "                       CPF"))
        self.label_5.setText(_translate("AltFuncWindow", "Dados pessoais"))
        self.linha_nome.setPlaceholderText(_translate("AltFuncWindow", "                      Nome"))
        self.linha_data.setPlaceholderText(_translate("AltFuncWindow", "           Data de nascimento"))
        self.label_6.setText(_translate("AltFuncWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Insira o CPF e altere o funcionário.</span></p></body></html>"))
        self.label_7.setText(_translate("AltFuncWindow", "Projeto de Introdução à Programação"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AltFuncWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())