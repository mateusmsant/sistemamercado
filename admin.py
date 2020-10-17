from PyQt5 import QtCore, QtGui, QtWidgets
from funcionarios import Ui_FuncWindow
from produtos import Ui_ProdutosWindow
from fornecedores import Ui_FornecedorWindow


class Ui_telaAdmin(object):
    def produtos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProdutosWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def fornecedores(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FornecedorWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def funcionarios(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FuncWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, telaAdmin):
        telaAdmin.setObjectName("telaAdmin")
        telaAdmin.resize(490, 334)
        telaAdmin.setMaximumSize(QtCore.QSize(490, 334))
        telaAdmin.setStyleSheet("color:rgb(170, 170, 255);\n"
"background-color: rgb(115, 115, 115);\n"
"")
        self.centralwidget = QtWidgets.QWidget(telaAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(107, 107, 107);\n"
"    border-radius:60px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.goToProd = QtWidgets.QPushButton(self.frame)
        self.goToProd.setGeometry(QtCore.QRect(25, 70, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.goToProd.setFont(font)
        self.goToProd.setStyleSheet("QPushButton {\n"
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
        self.goToProd.setObjectName("goToProd")
        self.goToProd.clicked.connect(self.produtos)

        self.gotoFunc = QtWidgets.QPushButton(self.frame)
        self.gotoFunc.setGeometry(QtCore.QRect(250, 70, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.gotoFunc.setFont(font)
        self.gotoFunc.setStyleSheet("QPushButton {\n"
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
        self.gotoFunc.setObjectName("gotoFunc")
        self.gotoFunc.clicked.connect(self.funcionarios)
        self.gotoForn = QtWidgets.QPushButton(self.frame)
        self.gotoForn.setGeometry(QtCore.QRect(110, 160, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.gotoForn.setFont(font)
        self.gotoForn.setStyleSheet("QPushButton {\n"
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
        self.gotoForn.setObjectName("gotoForn")
        self.gotoForn.clicked.connect(self.fornecedores)
        self.verticalLayout.addWidget(self.frame)
        self.bottom_bar = QtWidgets.QFrame(self.centralwidget)
        self.bottom_bar.setMinimumSize(QtCore.QSize(50, 2))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom_bar.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.bottom_bar)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.bottom_bar)
        self.label_5.setEnabled(False)
        self.label_5.setMaximumSize(QtCore.QSize(211, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setStyleSheet("color:rgb(240, 240, 240);\n"
"text-align:right;")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.bottom_bar)
        telaAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaAdmin)
        QtCore.QMetaObject.connectSlotsByName(telaAdmin)

    def retranslateUi(self, telaAdmin):
        _translate = QtCore.QCoreApplication.translate
        telaAdmin.setWindowTitle(_translate("telaAdmin", "Administrador"))
        telaAdmin.setWindowIcon(QtGui.QIcon('icone.png'))

        self.goToProd.setText(_translate("telaAdmin", "Produtos"))
        self.gotoFunc.setText(_translate("telaAdmin", "Funcionários"))
        self.gotoForn.setText(_translate("telaAdmin", "Fornecedores"))
        self.label_5.setText(_translate("telaAdmin", "Projeto de Introdução à Programação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaAdmin = QtWidgets.QMainWindow()
    ui = Ui_telaAdmin()
    ui.setupUi(telaAdmin)
    telaAdmin.show()
    sys.exit(app.exec_())
