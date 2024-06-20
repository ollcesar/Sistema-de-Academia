# Form implementation generated from reading ui file 'telaDeLogin.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(691, 507)
        Login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        Login.setStyleSheet("background: rgb(103, 103, 214)\n"
"")
        self.frame = QtWidgets.QFrame(parent=Login)
        self.frame.setGeometry(QtCore.QRect(140, 120, 421, 281))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.frame.setAcceptDrops(True)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background: rgba(0, 0, 0, 0.2)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.txt_user = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_user.setGeometry(QtCore.QRect(120, 120, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setMouseTracking(True)
        self.txt_user.setAutoFillBackground(False)
        self.txt_user.setStyleSheet("color: rgb(255, 255, 255)")
        self.txt_user.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_password.setGeometry(QtCore.QRect(120, 170, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("color: rgb(255,255,255)")
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_password.setObjectName("txt_password")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: rgba(0,0,0, 0.5);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(255,255,255);\n"
"    color: rgba(0,0,0, 0.5);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(180, 30, 71, 71))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/imgs/aplicativo-web.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.txt_user.raise_()
        self.txt_password.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.txt_user, self.txt_password)
        Login.setTabOrder(self.txt_password, self.pushButton)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.txt_user.setPlaceholderText(_translate("Login", "Usuário"))
        self.txt_password.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
