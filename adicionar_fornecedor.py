from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_addFornecedor(object):
    def adicionarFornecedor(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        codigo = self.codigo.text()
        nome = self.nome.text()
        email = self.email.text()
        cidade = self.cidade.text()
        segmento = self.segmento.text()
    
        query = f"SELECT codigo FROM fornecedores WHERE codigo = '{codigo}'"
        c.execute(query)
        result = c.fetchall()
        
        if codigo != '':
            if not result:
                c.execute("""INSERT INTO fornecedores (codigo, nome, email, cidade, segmento) VALUES (?,?,?,?,?)""", (codigo, nome, email, cidade, segmento))

        connection.commit()
        c.close()

    def setupUi(self, addFornecedor):
        addFornecedor.setObjectName("addFornecedor")
        addFornecedor.resize(497, 447)
        addFornecedor.setMinimumSize(QtCore.QSize(497, 447))
        addFornecedor.setMaximumSize(QtCore.QSize(497, 447))
        addFornecedor.setStyleSheet("background-color: rgb(60,58,58);\n"
"border:50px")
        self.centralwidget = QtWidgets.QWidget(addFornecedor)
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
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, 10, 531, 421))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.codigo = QtWidgets.QLineEdit(self.frame_2)
        self.codigo.setGeometry(QtCore.QRect(30, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.codigo.setFont(font)
        self.codigo.setText("")
        self.codigo.setObjectName("codigo")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.cidade = QtWidgets.QLineEdit(self.frame_2)
        self.cidade.setGeometry(QtCore.QRect(270, 130, 201, 31))
        self.cidade.setText("")
        self.cidade.setObjectName("cidade")
        self.addFornecedor = QtWidgets.QPushButton(self.frame_2)
        self.addFornecedor.setGeometry(QtCore.QRect(150, 260, 200, 40))
        self.addFornecedor.setStyleSheet("QPushButton {\n"
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
        self.addFornecedor.setObjectName("addFornecedor")
        self.addFornecedor.clicked.connect(self.adicionarFornecedor)
        self.nome = QtWidgets.QLineEdit(self.frame_2)
        self.nome.setGeometry(QtCore.QRect(270, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nome.setFont(font)
        self.nome.setText("")
        self.nome.setObjectName("nome")
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setGeometry(QtCore.QRect(30, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.email.setFont(font)
        self.email.setText("")
        self.email.setObjectName("email")
        self.segmento = QtWidgets.QLineEdit(self.frame_2)
        self.segmento.setGeometry(QtCore.QRect(150, 190, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.segmento.setFont(font)
        self.segmento.setText("")
        self.segmento.setObjectName("segmento")
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
        self.label_7.setGeometry(QtCore.QRect(250, 0, 211, 25))
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
        addFornecedor.setCentralWidget(self.centralwidget)

        self.retranslateUi(addFornecedor)
        QtCore.QMetaObject.connectSlotsByName(addFornecedor)

    def retranslateUi(self, addFornecedor):
        _translate = QtCore.QCoreApplication.translate
        addFornecedor.setWindowTitle(_translate("A", "Adicionar fornecedor"))
        addFornecedor.setWindowIcon(QtGui.QIcon('icone.png'))
        self.codigo.setPlaceholderText(_translate("addFornecedor", "                        Código"))
        self.cidade.setPlaceholderText(_translate("addFornecedor", "                        Cidade"))
        self.addFornecedor.setText(_translate("addFornecedor", "Adicionar fornecedor"))
        self.nome.setPlaceholderText(_translate("addFornecedor", "                        Nome"))
        self.email.setPlaceholderText(_translate("addFornecedor", "                          Email"))
        self.segmento.setPlaceholderText(_translate("addFornecedor", "                        Segmento"))
        self.label_7.setText(_translate("addFornecedor", "Projeto de Introdução à Programação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addFornecedor = QtWidgets.QMainWindow()
    ui = Ui_addFornecedor()
    ui.setupUi(addFornecedor)
    addFornecedor.show()
    sys.exit(app.exec_())
