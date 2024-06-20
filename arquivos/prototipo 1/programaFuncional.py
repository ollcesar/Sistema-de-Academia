from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.setupLeftContainer()
        self.setupRightContainer()

        self.horizontalLayout.addWidget(self.containerEsquerdo)
        self.horizontalLayout.addWidget(self.containerDireito)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.Paginas.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupLeftContainer(self):
        self.containerEsquerdo = QtWidgets.QFrame(parent=self.centralwidget)
        self.containerEsquerdo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.containerEsquerdo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.containerEsquerdo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.containerEsquerdo.setObjectName("containerEsquerdo")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.containerEsquerdo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.setupLogoFrame()
        self.setupMenuFrame()

        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.frame)

    def setupLogoFrame(self):
        self.frame_2 = QtWidgets.QFrame(parent=self.containerEsquerdo)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

    def setupMenuFrame(self):
        self.frame = QtWidgets.QFrame(parent=self.containerEsquerdo)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.toolBox = QtWidgets.QToolBox(parent=self.frame)
        self.toolBox.setObjectName("toolBox")

        self.setupToolboxPages()

        self.verticalLayout_5.addWidget(self.toolBox)

    def setupToolboxPages(self):
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 152, 293))
        self.page.setObjectName("page")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.Paginas.setCurrentIndex(0))  # Navegar para Home
        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.Paginas.setCurrentIndex(1))  # Navegar para Cadastro
        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.Paginas.setCurrentIndex(2))  # Navegar para Contatos
        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.Paginas.setCurrentIndex(3))  # Navegar para Sobre
        self.verticalLayout_6.addWidget(self.pushButton_5)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)

        self.toolBox.addItem(self.page, "")

        self.setupToolboxPage2()

    def setupToolboxPage2(self):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 147, 106))
        self.page_2.setObjectName("page_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, "")

    def setupRightContainer(self):
        self.containerDireito = QtWidgets.QFrame(parent=self.centralwidget)
        self.containerDireito.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.containerDireito.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.containerDireito.setObjectName("containerDireito")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.containerDireito)
        self.verticalLayout.setObjectName("verticalLayout")

        self.setupTopFrame()
        self.setupMainFrame()
        self.setupBottomFrame()

    def setupTopFrame(self):
        self.frameCima = QtWidgets.QFrame(parent=self.containerDireito)
        self.frameCima.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCima.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCima.setObjectName("frameCima")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameCima)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(parent=self.frameCima)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.frameCima)

    def setupMainFrame(self):
        self.mainFrame = QtWidgets.QFrame(parent=self.containerDireito)
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

        self.Paginas = QtWidgets.QStackedWidget(parent=self.mainFrame)
        self.Paginas.setObjectName("Paginas")

        self.setupPages()

        self.verticalLayout_7.addWidget(self.Paginas)
        self.verticalLayout.addWidget(self.mainFrame)

    def setupPages(self):
        # Página Home
        self.HomePg = QtWidgets.QWidget()
        self.HomePg.setObjectName("HomePg")
        self.labelHome = QtWidgets.QLabel("Bem-vindo à Academia VivaMais!", self.HomePg)
        self.labelHome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Paginas.addWidget(self.HomePg)

        # Página de Cadastro
        self.CadastroPg = QtWidgets.QWidget()
        self.CadastroPg.setObjectName("CadastroPg")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.CadastroPg)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.tabWidget = QtWidgets.QTabWidget(parent=self.CadastroPg)
        self.tabWidget.setObjectName("tabWidget")

        self.setupCadastroTab()
        self.setupAlunosTab()

        self.verticalLayout_8.addWidget(self.tabWidget)
        self.Paginas.addWidget(self.CadastroPg)

        # Página de Contatos
        self.ContatosPg = QtWidgets.QWidget()
        self.ContatosPg.setObjectName("ContatosPg")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ContatosPg)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.label_7 = QtWidgets.QLabel(parent=self.ContatosPg)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)

        self.Paginas.addWidget(self.ContatosPg)

        # Página Sobre
        self.SobrePg = QtWidgets.QWidget()
        self.SobrePg.setObjectName("SobrePg")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.SobrePg)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.label_8 = QtWidgets.QLabel(parent=self.SobrePg)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)

        self.Paginas.addWidget(self.SobrePg)

    def setupCadastroTab(self):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")

        self.labelID = QtWidgets.QLabel("ID:", self.tab)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelID)
        self.lineEditID = QtWidgets.QLineEdit(self.tab)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditID)

        self.labelNome = QtWidgets.QLabel("Nome:", self.tab)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelNome)
        self.lineEditNome = QtWidgets.QLineEdit(self.tab)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditNome)

        self.labelCPF = QtWidgets.QLabel("CPF:", self.tab)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelCPF)
        self.lineEditCPF = QtWidgets.QLineEdit(self.tab)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditCPF)

        self.labelTelefone = QtWidgets.QLabel("Telefone:", self.tab)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTelefone)
        self.lineEditTelefone = QtWidgets.QLineEdit(self.tab)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditTelefone)

        self.labelPlano = QtWidgets.QLabel("Plano:", self.tab)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPlano)
        self.lineEditPlano = QtWidgets.QLineEdit(self.tab)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditPlano)

        self.pushButton = QtWidgets.QPushButton("Adicionar Aluno", self.tab)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addAluno)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)

        self.tabWidget.addTab(self.tab, "Cadastro de Aluno")

    def setupAlunosTab(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nome", "CPF", "Telefone", "Plano"])
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "Lista de Alunos")

    def setupBottomFrame(self):
        self.frameBaixo = QtWidgets.QFrame(parent=self.containerDireito)
        self.frameBaixo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameBaixo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameBaixo.setObjectName("frameBaixo")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameBaixo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_2 = QtWidgets.QLabel(parent=self.frameBaixo)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.frameBaixo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Academia VivaMais"))
        self.label_3.setText(_translate("MainWindow", "Academia VivaMais"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Cadastro"))
        self.pushButton_4.setText(_translate("MainWindow", "Contatos"))
        self.pushButton_5.setText(_translate("MainWindow", "Sobre"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Menu"))
        self.label_4.setText(_translate("MainWindow", "Ajuda"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Ajuda"))
        self.label.setText(_translate("MainWindow", "Academia VivaMais"))
        self.label_7.setText(_translate("MainWindow", "Informações de Contato"))
        self.label_8.setText(_translate("MainWindow", "Sobre a Academia"))
        self.label_2.setText(_translate("MainWindow", "Todos os direitos reservados"))

    def addAluno(self):
        id = self.lineEditID.text()
        nome = self.lineEditNome.text()
        cpf = self.lineEditCPF.text()
        telefone = self.lineEditTelefone.text()
        plano = self.lineEditPlano.text()

        if not all([id, nome, cpf, telefone, plano]):
            QtWidgets.QMessageBox.warning(None, "Erro", "Todos os campos devem ser preenchidos.")
            return

        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(id))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(nome))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(cpf))
        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(telefone))
        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(plano))

        self.lineEditID.clear()
        self.lineEditNome.clear()
        self.lineEditCPF.clear()
        self.lineEditTelefone.clear()
        self.lineEditPlano.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
