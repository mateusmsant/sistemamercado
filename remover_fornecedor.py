from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import imagens

class Ui_removeFornecedor(object):
    def removeFornecedorByCodigo(self):
        connection = sqlite3.connect('supermercado.db')
        c = connection.cursor()

        codigo = self.codigoFornRemove.text()
        c.execute(f"DELETE FROM fornecedores WHERE codigo = '{codigo}'")
        
        connection.commit()
        c.close()

    def setupUi(self, removeFornecedor):
        removeFornecedor.setObjectName("removeFornecedor")
        removeFornecedor.resize(594, 593)
        removeFornecedor.setMinimumSize(QtCore.QSize(594, 593))
        removeFornecedor.setMaximumSize(QtCore.QSize(594, 593))
        removeFornecedor.setStyleSheet("color:rgb(170, 170, 255);\n"
"background-color: rgb(115, 115, 115);\n"
"")
        self.centralwidget = QtWidgets.QWidget(removeFornecedor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setGeometry(QtCore.QRect(90, 50, 381, 331))
        self.frame.setStyleSheet("QFrame {\n"
"    \n"
"    image: url(:/Images/Images/pngwing.com.png);\n"
"    background-color: rgb(107, 107, 107);\n"
"    border-radius:60px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.codigoFornRemove = QtWidgets.QLineEdit(self.frame)
        self.codigoFornRemove.setGeometry(QtCore.QRect(40, 150, 291, 41))
        self.codigoFornRemove.setStyleSheet("QLineEdit {\n"
"    border:2px solid rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:rgb(170, 170, 255);\n"
"    padding:5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(85, 170, 255)\n"
"}")
        self.codigoFornRemove.setText("")
        self.codigoFornRemove.setObjectName("codigoFornRemove")
        self.removeForn = QtWidgets.QPushButton(self.frame)
        self.removeForn.setGeometry(QtCore.QRect(100, 220, 181, 31))
        self.removeForn.setStyleSheet("QPushButton {\n"
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
        self.removeForn.setObjectName("removeForn")
        self.removeForn.clicked.connect(self.removeFornecedorByCodigo)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
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
        removeFornecedor.setCentralWidget(self.centralwidget)

        self.retranslateUi(removeFornecedor)
        QtCore.QMetaObject.connectSlotsByName(removeFornecedor)

    def retranslateUi(self, removeFornecedor):
        _translate = QtCore.QCoreApplication.translate
        removeFornecedor.setWindowTitle(_translate("removeFornecedor", "Remover fornecedor"))
        removeFornecedor.setWindowIcon(QtGui.QIcon('icone.png'))
        self.codigoFornRemove.setPlaceholderText(_translate("removeFornecedor", "                              Código do fornecedor"))
        self.removeForn.setText(_translate("removeFornecedor", "Remover fornecedor"))
        self.label.setText(_translate("removeFornecedor", "Projeto de Introdução à Programação"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    removeFornecedor = QtWidgets.QMainWindow()
    ui = Ui_removeFornecedor()
    ui.setupUi(removeFornecedor)
    removeFornecedor.show()
    sys.exit(app.exec_())
