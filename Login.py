from PyQt5 import QtCore, QtGui, QtWidgets
from admin import Ui_telaAdmin
from caixa import Ui_CaixaWindow
from esqueceu_senha import Ui_EsqueceuSenhaWindow
import sqlite3
import imagens

tentativas = 0


class Ui_LoginWindow(object):
    def esqueceuSenha(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EsqueceuSenhaWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def authCheck(self):
        global tentativas

        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()
    
        loginusado = self.user.text()
        senhausada = self.password.text()          

        # Admin
        c.execute(f"""SELECT * FROM funcionarios WHERE userlogin = '{loginusado}' AND userpassword = '{senhausada}' AND classe = 'Administrador'""")
        testeforadmin = c.fetchone()
        if testeforadmin:
            self.frame_error.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_telaAdmin()
            self.ui.setupUi(self.window)
            self.window.show()
           
        
        # Operador
        c.execute(f"""SELECT * FROM funcionarios WHERE userlogin = '{loginusado}' AND userpassword = '{senhausada}' AND classe = 'Operador'""")
        testeforoperador = c.fetchall()
        if testeforoperador:
            self.frame_error.hide()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CaixaWindow()
            self.ui.setupUi(self.window)
            self.window.show()

  

        # Tentativas
        c.execute(f"""SELECT * FROM funcionarios WHERE userlogin = '{loginusado}' AND userpassword != '{senhausada}'""")
        senhaErrada = c.fetchone()

        if senhaErrada and senhausada != '':
            tentativas += 1
            if tentativas != 4:
                this = f'Você digitou uma senha inválida. Você tem {5 - tentativas} tentativas.'
                self.erro_popup.setText(this)
                self.frame_error.show()
            else:
                this = f'Você digitou uma senha inválida. Você tem 1 tentativa.'
                self.erro_popup.setText(this)
                self.frame_error.show()
            
            
        

        # Campos em branco
        if loginusado + senhausada == '':
            self.erro_popup.setText('O campo de usuário e o de senha estão em branco.')
            self.frame_error.show()
            
        
        elif loginusado == '':
            self.erro_popup.setText('O campo de usuário está em branco.')
            self.frame_error.show()
        elif senhausada == '':
            self.erro_popup.setText('O campo da senha está em branco.')
            self.frame_error.show()
        

        # Erro de senha 5 vezes
        if tentativas == 5:
            app.exit()
        
        connection.commit()
        c.close()


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 812)
        MainWindow.setMinimumSize(QtCore.QSize(923, 812))
        MainWindow.setMaximumSize(QtCore.QSize(923, 812))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("color:rgb(170, 170, 255);\n"
"background-color: rgb(115, 115, 115);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(599, 700))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.login_area.setFont(font)
        self.login_area.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(60,58,58);\n"
"    border-radius:60px;\n"
"}")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(220, 190, 161, 120))
        self.avatar.setMinimumSize(QtCore.QSize(1, 0))
        self.avatar.setStyleSheet("QFrame {\n"
"    \n"
"    image: url(:/Images/Images/pngguru.com (3).png);\n"
"    border-radius:0px;\n"
"    border:10px fluid;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.user = QtWidgets.QLineEdit(self.login_area)
        self.user.setGeometry(QtCore.QRect(160, 340, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.user.setFont(font)
        self.user.setStyleSheet("QLineEdit {\n"
"    border:2px solid rgb(255, 255, 255);\n"
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
"}")
        self.user.setMaxLength(32)
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.login_area)
        self.password.setGeometry(QtCore.QRect(160, 400, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit {\n"
"    border:2px solid rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:rgb(170, 170, 255)\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(85, 170, 255)\n"
"}")
        self.password.setMaxLength(16)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.login_area)
        self.login.setGeometry(QtCore.QRect(200, 465, 200, 50))
        self.login.clicked.connect(self.authCheck)
        self.forgotpassword = QtWidgets.QPushButton(self.login_area)
        self.forgotpassword.setGeometry(QtCore.QRect(217, 600, 170, 35))
        self.forgotpassword.setStyleSheet("QPushButton {\n"
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
"}")
        self.forgotpassword.clicked.connect(self.esqueceuSenha)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setAutoFillBackground(False)
        self.login.setStyleSheet("QPushButton {\n"
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
"}")
        self.login.setObjectName("login")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(False)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/PinClipart.com_facts-clipart_2033374.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.frame_error = QtWidgets.QFrame(self.login_area)
        self.frame_error.setGeometry(QtCore.QRect(40, 0, 511, 21))
        self.frame_error.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_error.setStyleSheet("QFrame {\n"
"    background-color: rgb(0, 170, 255);    \n"
"    border-radius:2px;\n"
"}\n"
"")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.frame_error.hide()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(30, 3, 30, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.erro_popup = QtWidgets.QLabel(self.frame_error)
        self.erro_popup.setStyleSheet("color: rgb(0, 0, 0);")
        self.erro_popup.setAlignment(QtCore.Qt.AlignCenter)
        self.erro_popup.setObjectName("erro_popup")
        self.horizontalLayout_3.addWidget(self.erro_popup)
        self.botao_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.botao_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.botao_close_popup.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    \n"
"    image: url(:/Images/Images/EXIT.png);\n"
"    background-position:center;\n"
"    background-color: rgb(176, 176, 176);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(195, 195, 195);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color:rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.botao_close_popup.setText("")
        self.botao_close_popup.setObjectName("botao_close_popup")
        self.botao_close_popup.clicked.connect(self.frame_error.hide)
        self.horizontalLayout_3.addWidget(self.botao_close_popup)
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 923, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        MainWindow.setWindowIcon(QtGui.QIcon('icone.png'))
        self.user.setPlaceholderText(_translate("MainWindow", "                         Usuário"))
        self.password.setPlaceholderText(_translate("MainWindow", "                          Senha"))
        self.login.setText(_translate("MainWindow", "Entrar"))
        self.forgotpassword.setText(_translate("MainWindow", "Esqueci a senha"))
        self.label.setText(_translate("MainWindow", "Projeto de Introdução à Programação"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
