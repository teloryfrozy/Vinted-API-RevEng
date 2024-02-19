# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from sys import path
path.append('program')
from PyQt6 import QtCore, QtGui, QtWidgets
from secreteriat import Ui_windowSecreteriat
from toolBar import setup_menubar
from adManagement import Ui_windowAdManagement
from followMass import Ui_FollowMass
from home_p2 import Ui_HomePage2


class Ui_windowAccueil(object):
    
    def setupUi(self, primary):
        self.centralwidget = QtWidgets.QWidget(parent=primary.MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.left_arrow_btn = QtWidgets.QPushButton(parent=self.frame)
        self.left_arrow_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.left_arrow_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.left_arrow_btn.setFont(font)
        self.left_arrow_btn.setMouseTracking(False)
        self.gridLayout_2.addWidget(self.left_arrow_btn, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(parent=self.frame)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setLineWidth(20)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.gridLayout_2.addWidget(self.line_4, 0, 8, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=self.frame)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(20)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.gridLayout_2.addWidget(self.line_3, 0, 6, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(20)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.gridLayout_2.addWidget(self.line, 0, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(20)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.follow_mass_title = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.follow_mass_title.setFont(font)
        self.follow_mass_title.setMouseTracking(False)
        self.follow_mass_title.setStyleSheet("color: rgb(98, 98, 98);")
        self.horizontalLayout_10.addWidget(self.follow_mass_title, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.follow_mass_button = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.follow_mass_button.setFont(font)
        self.follow_mass_button.setStyleSheet("background-color: rgb(22, 175, 12);")
        self.follow_mass_button.setAutoDefault(False)
        self.follow_mass_button.setDefault(True)
        self.follow_mass_button.setFlat(True)
        self.horizontalLayout_6.addWidget(self.follow_mass_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 6, 1, 1, 1)
        self.description_follow_mass = QtWidgets.QTextBrowser(parent=self.frame)
        self.description_follow_mass.setMinimumSize(QtCore.QSize(280, 250))
        self.description_follow_mass.setSizeIncrement(QtCore.QSize(300, 0))
        self.description_follow_mass.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"")
        self.description_follow_mass.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gridLayout_4.addWidget(self.description_follow_mass, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 4, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 6, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.goSecreteriat = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goSecreteriat.setFont(font)
        self.goSecreteriat.setStyleSheet("background-color: rgb(212, 175, 55);")
        self.goSecreteriat.setAutoDefault(False)
        self.goSecreteriat.setDefault(True)
        self.goSecreteriat.setFlat(True)
        self.horizontalLayout_8.addWidget(self.goSecreteriat)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.Secreteritat = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.Secreteritat.setFont(font)
        self.Secreteritat.setStyleSheet("color: rgb(179, 139, 109);")
        self.horizontalLayout_11.addWidget(self.Secreteritat, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 4, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem11, 2, 1, 1, 1)
        self.descriptionMailManagement = QtWidgets.QTextBrowser(parent=self.frame)
        self.descriptionMailManagement.setMinimumSize(QtCore.QSize(280, 250))
        self.descriptionMailManagement.setSizeIncrement(QtCore.QSize(300, 0))
        self.descriptionMailManagement.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.descriptionMailManagement.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gridLayout_6.addWidget(self.descriptionMailManagement, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 7, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.AdManagement = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.AdManagement.setFont(font)
        self.AdManagement.setStyleSheet("color: rgb(119, 181, 254);")
        self.horizontalLayout_9.addWidget(self.AdManagement, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem12, 6, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.goAdManagement = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.goAdManagement.setFont(font)
        self.goAdManagement.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.goAdManagement.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.goAdManagement.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.goAdManagement.setAcceptDrops(False)
        self.goAdManagement.setToolTipDuration(-1)
        self.goAdManagement.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.goAdManagement.setAutoFillBackground(False)
        self.goAdManagement.setStyleSheet("background-color: rgb(219, 74, 57);")
        self.goAdManagement.setAutoDefault(False)
        self.goAdManagement.setDefault(True)
        self.goAdManagement.setFlat(True)
        self.horizontalLayout_7.addWidget(self.goAdManagement)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem15, 0, 1, 1, 1)
        self.descriptionAdManagement = QtWidgets.QTextBrowser(parent=self.frame)
        self.descriptionAdManagement.setMinimumSize(QtCore.QSize(280, 250))
        self.descriptionAdManagement.setSizeIncrement(QtCore.QSize(300, 0))
        self.descriptionAdManagement.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.descriptionAdManagement.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gridLayout_5.addWidget(self.descriptionAdManagement, 3, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem16, 4, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem17, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 2, 1, 1)
        self.right_arrow_btn = QtWidgets.QPushButton(parent=self.frame)
        self.right_arrow_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.right_arrow_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.right_arrow_btn.setFont(font)
        self.right_arrow_btn.setAutoDefault(False)
        self.right_arrow_btn.setDefault(False)
        self.right_arrow_btn.setFlat(False)
        self.gridLayout_2.addWidget(self.right_arrow_btn, 0, 9, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        primary.MainWindow.setCentralWidget(self.centralwidget)
        
        # load the menubar and the toolbar
        setup_menubar(self, primary)
        # mechanisms
        self.follow_mass_button.clicked.connect(lambda:primary.set_page(Ui_FollowMass()))
        self.goSecreteriat.clicked.connect(lambda:primary.set_page(Ui_windowSecreteriat()))
        self.goAdManagement.clicked.connect(lambda:primary.set_page(Ui_windowAdManagement()))
        self.left_arrow_btn.clicked.connect(lambda:primary.set_page(Ui_HomePage2()))
        self.right_arrow_btn.clicked.connect(lambda:primary.set_page(Ui_HomePage2()))

        self.retranslateUi(primary)
        QtCore.QMetaObject.connectSlotsByName(primary.MainWindow)

    def retranslateUi(self, primary):
        self.left_arrow_btn.setText("<")
        self.follow_mass_title.setText("✈️ " + primary.lang_file.get_page_text("home_page", "follow_mass_title"))
        self.follow_mass_button.setText(primary.lang_file.get_page_text("home_page", "follow_mass_btn")+" 👊")
        follow_mass_desc1 = primary.lang_file.get_page_text("home_page", "follow_mass_desc1")
        follow_mass_desc2 = primary.lang_file.get_page_text("home_page", "follow_mass_desc2")
        follow_mass_desc3 = primary.lang_file.get_page_text("home_page", "follow_mass_desc3")
        self.description_follow_mass.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{follow_mass_desc1}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{follow_mass_desc2}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{follow_mass_desc3}</span></p></body></html>")
        self.goSecreteriat.setText(primary.lang_file.get_page_text("home_page", "secretariat_btn")+" 🚪")
        self.Secreteritat.setText("💻 "+primary.lang_file.get_page_text("home_page", "secretariat_title"))
        secretariat_desc1 = primary.lang_file.get_page_text("home_page", "secretariat_desc1")
        secretariat_desc2 = primary.lang_file.get_page_text("home_page", "secretariat_desc2")
        secretariat_desc3 = primary.lang_file.get_page_text("home_page", "secretariat_desc3")
        secretariat_desc4 = primary.lang_file.get_page_text("home_page", "secretariat_desc4")
        self.descriptionMailManagement.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{secretariat_desc1}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{secretariat_desc2}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{secretariat_desc3}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{secretariat_desc4}</span></p></body></html>")
        self.AdManagement.setText("📈 "+primary.lang_file.get_page_text("home_page", "ad_management_title"))
        self.goAdManagement.setText(primary.lang_file.get_page_text("home_page", "ad_management_btn")+" 👉")
        ad_management_desc1 = primary.lang_file.get_page_text("home_page", "ad_management_desc1")
        ad_management_desc2 = primary.lang_file.get_page_text("home_page", "ad_management_desc2")
        ad_management_desc3 = primary.lang_file.get_page_text("home_page", "ad_management_desc3")
        ad_management_desc4 = primary.lang_file.get_page_text("home_page", "ad_management_desc4")
        self.descriptionAdManagement.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{ad_management_desc1}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{ad_management_desc2}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{ad_management_desc3}</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:11pt;\"><br /></p>\n"
f"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt;\">{ad_management_desc4}</span></p></body></html>")
        self.right_arrow_btn.setText(">")