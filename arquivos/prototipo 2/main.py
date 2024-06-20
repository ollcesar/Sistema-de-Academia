from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")

        # Container esquerdo
        self.containerEsquerdo = QtWidgets.QFrame(self.centralwidget)
        self.containerEsquerdo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.containerEsquerdo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.containerEsquerdo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.containerEsquerdo.setObjectName("containerEsquerdo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.containerEsquerdo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Frame 2
        self.frame_2 = QtWidgets.QFrame(self.containerEsquerdo)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.frame_2)

        # Frame
        self.frame = QtWidgets.QFrame(self.containerEsquerdo)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setObjectName("toolBox")

        # Page
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 115, 269))
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.toolBox.addItem(self.page, "")

        # Page 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 147, 269))
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_5.addWidget(self.toolBox)
        self.verticalLayout_4.addWidget(self.frame)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.containerEsquerdo)

        # Container direito
        self.containerDireito = QtWidgets.QFrame(self.centralwidget)
        self.containerDireito.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.containerDireito.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.containerDireito.setObjectName("containerDireito")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.containerDireito)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameCima = QtWidgets.QFrame(self.containerDireito)
        self.frameCima.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCima.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCima.setObjectName("frameCima")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameCima)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frameCima)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frameCima)
        self.mainFrame = QtWidgets.QFrame(self.containerDireito)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Paginas = QtWidgets.QStackedWidget(self.mainFrame)
        self.Paginas.setObjectName("Paginas")

        # Home Page
        self.HomePg = QtWidgets.QWidget()
        self.HomePg.setObjectName("HomePg")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.HomePg)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_8 = QtWidgets.QFrame(self.HomePg)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setGeometry(QtCore.QRect(180, -10, 171, 145))
        self.label_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("imgs/aplicativo-web.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_20.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.HomePg)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_19.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_8.setPlaceholderText("Senha")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_19.addWidget(self.lineEdit_8)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_19.addWidget(self.pushButton_17)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_19.addItem(spacerItem1)
        self.verticalLayout_20.addWidget(self.frame_7)
        self.Paginas.addWidget(self.HomePg)

        # Pagina 2
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Paginas.addWidget(self.page_3)
        self.verticalLayout_7.addWidget(self.Paginas)
        self.verticalLayout.addWidget(self.mainFrame)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.containerDireito)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.Paginas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Label Text 3"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton 2"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton 3"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton 4"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton 5"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Toolbox Page 1"))
        self.label_4.setText(_translate("MainWindow", "Label Text 4"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Toolbox Page 2"))
        self.label.setText(_translate("MainWindow", "Label Text"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton 17"))
        self.label_2.setText(_translate("MainWindow", "Label Text 2"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
