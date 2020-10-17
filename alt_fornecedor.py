from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_AltFornecedor(object):
    def saveChangesToForn(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        codigo = self.codigo.text()

        if self.nome.text():
            nome = self.nome.text()
            query = f"UPDATE fornecedores SET nome = '{nome}' WHERE codigo = '{codigo}'"
            c.execute(query)

        if self.email.text():
            email = self.email.text()
            query = f"UPDATE fornecedores SET email = '{email}' WHERE codigo = '{codigo}'"
            c.execute(query)

        if self.cidade.text():
            cidade = self.cidade.text()
            query = f"UPDATE fornecedores SET cidade = '{cidade}' WHERE codigo = '{codigo}'"
            c.execute(query)

        if self.segmento.text():
            segmento = self.segmento.text()
            query = f"UPDATE fornecedores SET segmento = '{segmento}' WHERE codigo = '{codigo}'"
            c.execute(query)

        connection.commit()
        connection.close()
    
    def setupUi(self, AltFornecedor):
        AltFornecedor.setObjectName("AltFornecedor")
        AltFornecedor.resize(525, 549)
        AltFornecedor.setMinimumSize(QtCore.QSize(0, 0))
        AltFornecedor.setMaximumSize(QtCore.QSize(525, 549))
        AltFornecedor.setStyleSheet("background-color: rgb(115, 115, 115);\n"
"border:50px")
        self.centralwidget = QtWidgets.QWidget(AltFornecedor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("QLineEdit {\n"
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
        self.email = QtWidgets.QLineEdit(self.frame_4)
        self.email.setGeometry(QtCore.QRect(30, 160, 201, 31))
        self.email.setObjectName("email")
        self.cidade = QtWidgets.QLineEdit(self.frame_4)
        self.cidade.setGeometry(QtCore.QRect(260, 160, 201, 31))
        self.cidade.setObjectName("cidade")
        self.segmento = QtWidgets.QLineEdit(self.frame_4)
        self.segmento.setGeometry(QtCore.QRect(140, 220, 201, 31))
        self.segmento.setObjectName("segmento")
        self.nome = QtWidgets.QLineEdit(self.frame_4)
        self.nome.setGeometry(QtCore.QRect(260, 100, 201, 31))
        self.nome.setObjectName("nome")
        self.codigo = QtWidgets.QLineEdit(self.frame_4)
        self.codigo.setGeometry(QtCore.QRect(30, 100, 201, 31))
        self.codigo.setReadOnly(False)
        self.codigo.setObjectName("codigo")
        self.saveChanges = QtWidgets.QPushButton(self.frame_4)
        self.saveChanges.setGeometry(QtCore.QRect(170, 360, 151, 31))
        self.saveChanges.setStyleSheet("QPushButton {\n"
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
        self.saveChanges.setObjectName("saveChanges")
        self.saveChanges.clicked.connect(self.saveChangesToForn)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(10, 270, 471, 51))
        self.label.setObjectName("label")
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
        self.label_7.setGeometry(QtCore.QRect(280, 0, 211, 25))
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
        AltFornecedor.setCentralWidget(self.centralwidget)

        self.retranslateUi(AltFornecedor)
        QtCore.QMetaObject.connectSlotsByName(AltFornecedor)

    def retranslateUi(self, AltFornecedor):
        _translate = QtCore.QCoreApplication.translate
        AltFornecedor.setWindowTitle(_translate("Alterar fornecedor", "Alterar fornecedor"))
        AltFornecedor.setWindowIcon(QtGui.QIcon('icone.png'))
        self.email.setPlaceholderText(_translate("AltFornecedor", "                           Email"))
        self.cidade.setPlaceholderText(_translate("AltFornecedor", "                          Cidade"))
        self.segmento.setPlaceholderText(_translate("AltFornecedor", "                      Segmento"))
        self.nome.setPlaceholderText(_translate("AltFornecedor", "                          Nome"))
        self.codigo.setPlaceholderText(_translate("AltFornecedor", "                          Código"))
        self.saveChanges.setText(_translate("AltFornecedor", "Salvar alterações"))
        self.label.setText(_translate("AltFornecedor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">O código é inalterável.</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Linhas em branco não serão alteradas.</span></p></body></html>"))
        self.label_7.setText(_translate("AltFornecedor", "Projeto de Introdução à Programação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AltFornecedor = QtWidgets.QMainWindow()
    ui = Ui_AltFornecedor()
    ui.setupUi(AltFornecedor)
    AltFornecedor.show()
    sys.exit(app.exec_())
