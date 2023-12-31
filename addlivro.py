# Form implementation generated from reading ui file 'AddBook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class AddLivro_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_titulo = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_titulo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_titulo.setFont(font)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.verticalLayout.addWidget(self.lineEdit_titulo)
        self.lineEdit_autoria = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_autoria.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_autoria.setFont(font)
        self.lineEdit_autoria.setObjectName("lineEdit_autoria")
        self.verticalLayout.addWidget(self.lineEdit_autoria)
        self.lineEdit_editora = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_editora.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_editora.setFont(font)
        self.lineEdit_editora.setObjectName("lineEdit_editora")
        self.verticalLayout.addWidget(self.lineEdit_editora)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:gray;\n"
"color:white\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_result = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.insert_livro)

    def insert_livro(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            titulo = self.lineEdit_titulo.text()
            autoria = self.lineEdit_autoria.text()
            editora = self.lineEdit_editora.text()

            if titulo=="" or autoria=="" or editora=="":
                self.label_result.setText("Por favor preencha todos os campos")
                self.label_result.setStyleSheet('color:red')
                return
            
            mycursor = mydb.cursor()
            query = "INSERT INTO livros (titulo, autoria, editora) VALUES (%s,%s,%s)"
            values = (titulo, autoria, editora)
            mycursor.execute(query, values)
            mydb.commit()
            self.label_result.setText("Livro adicionado com sucesso!")
            self.label_result.setStyleSheet('color:green')

            self.lineEdit_titulo.setText("")
            self.lineEdit_editora.setText("")
            self.lineEdit_autoria.setText("")

        except mc.Error as e:
            print("Error", e)
            self.label_result.setText("erro")
            self.label_result.setStyleSheet('color: red')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_titulo.setPlaceholderText(_translate("Dialog", "Título do Livro"))
        self.lineEdit_autoria.setPlaceholderText(_translate("Dialog", "Autor(a) do Livro"))
        self.lineEdit_editora.setPlaceholderText(_translate("Dialog", "Editora"))
        self.pushButton.setText(_translate("Dialog", "Adicionar Livro"))



