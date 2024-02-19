from base64 import b64decode
from tkinter import messagebox
from PyQt6 import QtCore, QtGui, QtWidgets
from engine import Email
from accueil import Ui_windowAccueil
from toolBar import setup_menubar
from vinted_api import VintedAPI

class Ui_ConnectionVinted(object):
    
    def setupUi(self, primary):
        self.centralwidget = QtWidgets.QWidget(parent=primary.MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        spacerItem = QtWidgets.QSpacerItem(311, 153, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        self.labelVinted_3 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(20)
        self.labelVinted_3.setFont(font)
        self.labelVinted_3.setStyleSheet("alternate-background-color: rgb(135, 206, 235);")
        self.gridLayout_4.addWidget(self.labelVinted_3, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(311, 156, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(312, 156, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.vinted_token_text = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vinted_token_text.setFont(font)
        self.horizontalLayout.addWidget(self.vinted_token_text, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 1, 1, 1, 1)
        self.vinted_token = QtWidgets.QLineEdit(parent=self.frame)
        self.gridLayout_3.addWidget(self.vinted_token, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.submitConnect = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitConnect.setFont(font)
        self.horizontalLayout_4.addWidget(self.submitConnect)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(304, 156, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        primary.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=primary.MainWindow)
        primary.MainWindow.setStatusBar(self.statusbar)

        # Mechanisms
        setup_menubar(self, primary)
        self.submitConnect.clicked.connect(lambda:self.set_vinted_token(primary))        
        
        # set font and text of elements
        self.retranslateUi(primary)
        QtCore.QMetaObject.connectSlotsByName(primary.MainWindow)

    def retranslateUi(self, primary):
        self.labelVinted_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#77b5fe;\">VINTED</span></p></body></html>")
        self.vinted_token_text.setText("vinted_fr_session :")
        self.submitConnect.setText("  "+primary.lang_file.get_page_text("connections_page", "connection_btn")+"  ")

    def set_vinted_token(self, primary):
        """Set the vinted fr session token"""        
        if self.vinted_token.text() == "":
            return messagebox.showwarning(primary.lang_file.get_page_text("connections_page", "co_error_title"), primary.lang_file.get_page_text("connections_page", "co_error_msg1")+" vinted token"+primary.lang_file.get_page_text("connections_page", "co_error_msg2"))
        # vinted api access available
        primary.vinted_api = VintedAPI(self.vinted_token.text())
        # --- Auto Log in to the google account --- #
        if primary.param.get_dict()["auto-login"]:
            identifiers = primary.log_in.get_dict()["google"]
            email = b64decode(identifiers["username"]).decode("ascii")
            password = b64decode(identifiers["password"]).decode("ascii")
            google_account = Email(email, password, primary)
            primary.log_account(google_account)
        Ui_windowAccueil().setupUi(primary)