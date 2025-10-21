# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peV2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)
import images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1372, 746)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_21 = QGridLayout(self.centralwidget)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frTab = QFrame(self.centralwidget)
        self.frTab.setObjectName(u"frTab")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frTab.sizePolicy().hasHeightForWidth())
        self.frTab.setSizePolicy(sizePolicy)
        self.frTab.setStyleSheet(u"#frTab\n"
"{\n"
"	background-color: #26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 10px 20px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 16px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    qproperty-iconSize: 24px 24px;\n"
"    text-align: left;\n"
"   padding-left: 20px;\n"
"}\n"
"\n"
"#frTab QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#frTab QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4"
                        "ng h\u1ed7 tr\u1ee3 trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.frTab.setFrameShape(QFrame.StyledPanel)
        self.frTab.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(31, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_branch_icon = QLabel(self.frTab)
        self.lb_branch_icon.setObjectName(u"lb_branch_icon")
        self.lb_branch_icon.setPixmap(QPixmap(u":/img/logo.png"))
        self.lb_branch_icon.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.lb_branch_icon)

        self.lb_branch_text = QLabel(self.frTab)
        self.lb_branch_text.setObjectName(u"lb_branch_text")
        font = QFont()
        font.setFamilies([u"Stencil"])
        font.setPointSize(10)
        self.lb_branch_text.setFont(font)
        self.lb_branch_text.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")
        self.lb_branch_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_branch_text)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(22, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.bt_view_config = QPushButton(self.frTab)
        self.bt_view_config.setObjectName(u"bt_view_config")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_view_config.sizePolicy().hasHeightForWidth())
        self.bt_view_config.setSizePolicy(sizePolicy1)
        self.bt_view_config.setMinimumSize(QSize(131, 41))
        icon = QIcon()
        icon.addFile(u":/img/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_view_config.setIcon(icon)
        self.bt_view_config.setIconSize(QSize(24, 24))
        self.bt_view_config.setCheckable(True)
        self.bt_view_config.setFlat(False)

        self.verticalLayout_5.addWidget(self.bt_view_config)

        self.bt_bulk_import = QPushButton(self.frTab)
        self.bt_bulk_import.setObjectName(u"bt_bulk_import")
        sizePolicy1.setHeightForWidth(self.bt_bulk_import.sizePolicy().hasHeightForWidth())
        self.bt_bulk_import.setSizePolicy(sizePolicy1)
        self.bt_bulk_import.setMinimumSize(QSize(131, 41))
        icon1 = QIcon()
        icon1.addFile(u":/img/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_bulk_import.setIcon(icon1)
        self.bt_bulk_import.setIconSize(QSize(24, 24))
        self.bt_bulk_import.setCheckable(True)

        self.verticalLayout_5.addWidget(self.bt_bulk_import)

        self.bt_single_maintain = QPushButton(self.frTab)
        self.bt_single_maintain.setObjectName(u"bt_single_maintain")
        sizePolicy1.setHeightForWidth(self.bt_single_maintain.sizePolicy().hasHeightForWidth())
        self.bt_single_maintain.setSizePolicy(sizePolicy1)
        self.bt_single_maintain.setMinimumSize(QSize(131, 41))
        icon2 = QIcon()
        icon2.addFile(u":/img/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_single_maintain.setIcon(icon2)
        self.bt_single_maintain.setIconSize(QSize(24, 24))
        self.bt_single_maintain.setCheckable(True)

        self.verticalLayout_5.addWidget(self.bt_single_maintain)

        self.bt_realtime_check = QPushButton(self.frTab)
        self.bt_realtime_check.setObjectName(u"bt_realtime_check")
        sizePolicy1.setHeightForWidth(self.bt_realtime_check.sizePolicy().hasHeightForWidth())
        self.bt_realtime_check.setSizePolicy(sizePolicy1)
        self.bt_realtime_check.setMinimumSize(QSize(131, 41))
        icon3 = QIcon()
        icon3.addFile(u":/img/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_realtime_check.setIcon(icon3)
        self.bt_realtime_check.setIconSize(QSize(24, 24))
        self.bt_realtime_check.setCheckable(True)

        self.verticalLayout_5.addWidget(self.bt_realtime_check)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 295, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout_21.addWidget(self.frTab, 0, 0, 2, 1)

        self.frHeader = QFrame(self.centralwidget)
        self.frHeader.setObjectName(u"frHeader")
        self.frHeader.setStyleSheet(u"#frHeader\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frHeader.setFrameShape(QFrame.StyledPanel)
        self.frHeader.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbHeader = QLabel(self.frHeader)
        self.lbHeader.setObjectName(u"lbHeader")
        font1 = QFont()
        font1.setFamilies([u"Stencil"])
        font1.setPointSize(40)
        self.lbHeader.setFont(font1)
        self.lbHeader.setLayoutDirection(Qt.LeftToRight)
        self.lbHeader.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbHeader.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbHeader, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frHeader, 0, 1, 1, 1)

        self.frMain = QFrame(self.centralwidget)
        self.frMain.setObjectName(u"frMain")
        self.frMain.setStyleSheet(u"#frMain\n"
"{\n"
"	background-color: #26364d;\n"
"}\n"
"")
        self.frMain.setFrameShape(QFrame.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frMain)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.mulPage = QStackedWidget(self.frMain)
        self.mulPage.setObjectName(u"mulPage")
        self.mulPage.setStyleSheet(u"#mulPage\n"
"{\n"
"	background-color:white;\n"
"}\n"
"")
        self.p_check_config = QWidget()
        self.p_check_config.setObjectName(u"p_check_config")
        self.gridLayout_20 = QGridLayout(self.p_check_config)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.lb_view_caption = QLabel(self.p_check_config)
        self.lb_view_caption.setObjectName(u"lb_view_caption")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(True)
        self.lb_view_caption.setFont(font2)
        self.lb_view_caption.setStyleSheet(u"color: #26364d;\n"
"font-weight:bold;")

        self.gridLayout_20.addWidget(self.lb_view_caption, 0, 0, 1, 3)

        self.f_view_find = QFrame(self.p_check_config)
        self.f_view_find.setObjectName(u"f_view_find")
        sizePolicy.setHeightForWidth(self.f_view_find.sizePolicy().hasHeightForWidth())
        self.f_view_find.setSizePolicy(sizePolicy)
        self.f_view_find.setStyleSheet(u"#f_view_find\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.f_view_find.setFrameShape(QFrame.StyledPanel)
        self.f_view_find.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.f_view_find)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_36 = QLabel(self.f_view_find)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setItalic(True)
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.cb_view_product = QComboBox(self.f_view_find)
        self.cb_view_product.setObjectName(u"cb_view_product")
        self.cb_view_product.setMinimumSize(QSize(107, 24))

        self.horizontalLayout_24.addWidget(self.cb_view_product)


        self.gridLayout_14.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.f_view_find)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.label_35)

        self.cb_view_project = QComboBox(self.f_view_find)
        self.cb_view_project.setObjectName(u"cb_view_project")
        self.cb_view_project.setMinimumSize(QSize(107, 24))

        self.horizontalLayout_23.addWidget(self.cb_view_project)


        self.gridLayout_14.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.f_view_find)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_8)

        self.cb_view_region = QComboBox(self.f_view_find)
        self.cb_view_region.setObjectName(u"cb_view_region")
        self.cb_view_region.setMinimumSize(QSize(107, 24))

        self.horizontalLayout.addWidget(self.cb_view_region)


        self.gridLayout_14.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_5 = QLabel(self.f_view_find)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_5, 3, 0, 1, 1)

        self.tx_view_skuSearch = QLineEdit(self.f_view_find)
        self.tx_view_skuSearch.setObjectName(u"tx_view_skuSearch")
        self.tx_view_skuSearch.setMinimumSize(QSize(161, 31))

        self.gridLayout_14.addWidget(self.tx_view_skuSearch, 4, 0, 1, 1)

        self.list_view_sku = QListView(self.f_view_find)
        self.list_view_sku.setObjectName(u"list_view_sku")

        self.gridLayout_14.addWidget(self.list_view_sku, 5, 0, 1, 1)


        self.gridLayout_20.addWidget(self.f_view_find, 1, 0, 1, 1)

        self.fKey = QFrame(self.p_check_config)
        self.fKey.setObjectName(u"fKey")
        sizePolicy.setHeightForWidth(self.fKey.sizePolicy().hasHeightForWidth())
        self.fKey.setSizePolicy(sizePolicy)
        self.fKey.setStyleSheet(u"#fKey\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.fKey.setFrameShape(QFrame.StyledPanel)
        self.fKey.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fKey)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.label_24 = QLabel(self.fKey)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_24)

        self.tx_view_mlabel = QLineEdit(self.fKey)
        self.tx_view_mlabel.setObjectName(u"tx_view_mlabel")
        sizePolicy1.setHeightForWidth(self.tx_view_mlabel.sizePolicy().hasHeightForWidth())
        self.tx_view_mlabel.setSizePolicy(sizePolicy1)
        self.tx_view_mlabel.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.tx_view_mlabel)


        self.gridLayout.addLayout(self.horizontalLayout_13, 7, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_20 = QLabel(self.fKey)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_20)

        self.tx_view_sap = QLineEdit(self.fKey)
        self.tx_view_sap.setObjectName(u"tx_view_sap")
        sizePolicy1.setHeightForWidth(self.tx_view_sap.sizePolicy().hasHeightForWidth())
        self.tx_view_sap.setSizePolicy(sizePolicy1)
        self.tx_view_sap.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.tx_view_sap)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_21 = QLabel(self.fKey)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_21)

        self.tx_view_color = QLineEdit(self.fKey)
        self.tx_view_color.setObjectName(u"tx_view_color")
        sizePolicy1.setHeightForWidth(self.tx_view_color.sizePolicy().hasHeightForWidth())
        self.tx_view_color.setSizePolicy(sizePolicy1)
        self.tx_view_color.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.tx_view_color)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)

        self.label_9 = QLabel(self.fKey)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_13 = QLabel(self.fKey)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_14 = QLabel(self.fKey)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.verticalLayout.addWidget(self.label_14)

        self.label_16 = QLabel(self.fKey)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.verticalLayout.addWidget(self.label_16)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tx_view_blabel = QLineEdit(self.fKey)
        self.tx_view_blabel.setObjectName(u"tx_view_blabel")
        sizePolicy1.setHeightForWidth(self.tx_view_blabel.sizePolicy().hasHeightForWidth())
        self.tx_view_blabel.setSizePolicy(sizePolicy1)
        self.tx_view_blabel.setMinimumSize(QSize(497, 0))
        self.tx_view_blabel.setMaximumSize(QSize(500, 16777215))
        self.tx_view_blabel.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.tx_view_blabel)

        self.tx_view_des = QLineEdit(self.fKey)
        self.tx_view_des.setObjectName(u"tx_view_des")
        self.tx_view_des.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.tx_view_des)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 6, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(28)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(self.fKey)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.tx_view_rlabel = QLineEdit(self.fKey)
        self.tx_view_rlabel.setObjectName(u"tx_view_rlabel")
        self.tx_view_rlabel.setMinimumSize(QSize(260, 0))
        self.tx_view_rlabel.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.tx_view_rlabel)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_18 = QLabel(self.fKey)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_18)

        self.tx_view_upc = QLineEdit(self.fKey)
        self.tx_view_upc.setObjectName(u"tx_view_upc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(115)
        sizePolicy3.setVerticalStretch(32)
        sizePolicy3.setHeightForWidth(self.tx_view_upc.sizePolicy().hasHeightForWidth())
        self.tx_view_upc.setSizePolicy(sizePolicy3)
        self.tx_view_upc.setMinimumSize(QSize(100, 32))
        self.tx_view_upc.setMaximumSize(QSize(100, 32))
        self.tx_view_upc.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.tx_view_upc)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_19 = QLabel(self.fKey)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_19)

        self.tx_view_brand = QLineEdit(self.fKey)
        self.tx_view_brand.setObjectName(u"tx_view_brand")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tx_view_brand.sizePolicy().hasHeightForWidth())
        self.tx_view_brand.setSizePolicy(sizePolicy4)
        self.tx_view_brand.setMinimumSize(QSize(65, 0))
        self.tx_view_brand.setMaximumSize(QSize(65, 32))
        self.tx_view_brand.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.tx_view_brand)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.label_15 = QLabel(self.fKey)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_22 = QLabel(self.fKey)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_11.addWidget(self.label_22)

        self.tx_view_qr = QLineEdit(self.fKey)
        self.tx_view_qr.setObjectName(u"tx_view_qr")
        sizePolicy1.setHeightForWidth(self.tx_view_qr.sizePolicy().hasHeightForWidth())
        self.tx_view_qr.setSizePolicy(sizePolicy1)
        self.tx_view_qr.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.tx_view_qr)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_23 = QLabel(self.fKey)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.tx_view_price = QLineEdit(self.fKey)
        self.tx_view_price.setObjectName(u"tx_view_price")
        sizePolicy1.setHeightForWidth(self.tx_view_price.sizePolicy().hasHeightForWidth())
        self.tx_view_price.setSizePolicy(sizePolicy1)
        self.tx_view_price.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.tx_view_price)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)


        self.gridLayout.addLayout(self.horizontalLayout_10, 6, 0, 1, 1)


        self.gridLayout_20.addWidget(self.fKey, 1, 1, 1, 1)

        self.fPrint = QFrame(self.p_check_config)
        self.fPrint.setObjectName(u"fPrint")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fPrint.sizePolicy().hasHeightForWidth())
        self.fPrint.setSizePolicy(sizePolicy5)
        self.fPrint.setStyleSheet(u"#fPrint\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.fPrint.setFrameShape(QFrame.StyledPanel)
        self.fPrint.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.fPrint)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.fPrint)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_26 = QLabel(self.fPrint)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_26)

        self.tx_view_carton = QLineEdit(self.fPrint)
        self.tx_view_carton.setObjectName(u"tx_view_carton")
        sizePolicy1.setHeightForWidth(self.tx_view_carton.sizePolicy().hasHeightForWidth())
        self.tx_view_carton.setSizePolicy(sizePolicy1)
        self.tx_view_carton.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.tx_view_carton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.fPrint)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_15.addWidget(self.label_27)

        self.tx_view_pallet1 = QLineEdit(self.fPrint)
        self.tx_view_pallet1.setObjectName(u"tx_view_pallet1")
        sizePolicy1.setHeightForWidth(self.tx_view_pallet1.sizePolicy().hasHeightForWidth())
        self.tx_view_pallet1.setSizePolicy(sizePolicy1)
        self.tx_view_pallet1.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_15.addWidget(self.tx_view_pallet1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_28 = QLabel(self.fPrint)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_16.addWidget(self.label_28)

        self.tx_view_pallet2 = QLineEdit(self.fPrint)
        self.tx_view_pallet2.setObjectName(u"tx_view_pallet2")
        sizePolicy1.setHeightForWidth(self.tx_view_pallet2.sizePolicy().hasHeightForWidth())
        self.tx_view_pallet2.setSizePolicy(sizePolicy1)
        self.tx_view_pallet2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.tx_view_pallet2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_29 = QLabel(self.fPrint)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_29)

        self.tx_view_pallet3 = QLineEdit(self.fPrint)
        self.tx_view_pallet3.setObjectName(u"tx_view_pallet3")
        sizePolicy1.setHeightForWidth(self.tx_view_pallet3.sizePolicy().hasHeightForWidth())
        self.tx_view_pallet3.setSizePolicy(sizePolicy1)
        self.tx_view_pallet3.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.tx_view_pallet3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(8)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_30 = QLabel(self.fPrint)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_18.addWidget(self.label_30)

        self.tx_view_repair = QLineEdit(self.fPrint)
        self.tx_view_repair.setObjectName(u"tx_view_repair")
        sizePolicy1.setHeightForWidth(self.tx_view_repair.sizePolicy().hasHeightForWidth())
        self.tx_view_repair.setSizePolicy(sizePolicy1)
        self.tx_view_repair.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.tx_view_repair)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_31 = QLabel(self.fPrint)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_19.addWidget(self.label_31)

        self.tx_view_ship = QLineEdit(self.fPrint)
        self.tx_view_ship.setObjectName(u"tx_view_ship")
        sizePolicy1.setHeightForWidth(self.tx_view_ship.sizePolicy().hasHeightForWidth())
        self.tx_view_ship.setSizePolicy(sizePolicy1)
        self.tx_view_ship.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_19.addWidget(self.tx_view_ship)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(17)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_32 = QLabel(self.fPrint)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_32)

        self.tx_view_overlay = QLineEdit(self.fPrint)
        self.tx_view_overlay.setObjectName(u"tx_view_overlay")
        sizePolicy1.setHeightForWidth(self.tx_view_overlay.sizePolicy().hasHeightForWidth())
        self.tx_view_overlay.setSizePolicy(sizePolicy1)
        self.tx_view_overlay.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.tx_view_overlay)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.label_25 = QLabel(self.fPrint)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")

        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(self.fPrint)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_33)

        self.tx_view_carton2 = QLineEdit(self.fPrint)
        self.tx_view_carton2.setObjectName(u"tx_view_carton2")
        sizePolicy1.setHeightForWidth(self.tx_view_carton2.sizePolicy().hasHeightForWidth())
        self.tx_view_carton2.setSizePolicy(sizePolicy1)
        self.tx_view_carton2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_21.addWidget(self.tx_view_carton2)


        self.gridLayout_3.addLayout(self.horizontalLayout_21, 3, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(11)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_34 = QLabel(self.fPrint)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_22.addWidget(self.label_34)

        self.tx_view_wic = QLineEdit(self.fPrint)
        self.tx_view_wic.setObjectName(u"tx_view_wic")
        sizePolicy1.setHeightForWidth(self.tx_view_wic.sizePolicy().hasHeightForWidth())
        self.tx_view_wic.setSizePolicy(sizePolicy1)
        self.tx_view_wic.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.tx_view_wic)


        self.gridLayout_3.addLayout(self.horizontalLayout_22, 4, 0, 1, 1)


        self.gridLayout_20.addWidget(self.fPrint, 1, 2, 1, 1)

        self.mulPage.addWidget(self.p_check_config)
        self.p_bulk = QWidget()
        self.p_bulk.setObjectName(u"p_bulk")
        self.gridLayout_17 = QGridLayout(self.p_bulk)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.f_bulk_find = QFrame(self.p_bulk)
        self.f_bulk_find.setObjectName(u"f_bulk_find")
        sizePolicy.setHeightForWidth(self.f_bulk_find.sizePolicy().hasHeightForWidth())
        self.f_bulk_find.setSizePolicy(sizePolicy)
        self.f_bulk_find.setStyleSheet(u"#f_bulk_find\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px 6px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 15px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 3px;\n"
"}\n"
"\n"
"#f_bulk_find QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_bulk_find QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 tro"
                        "ng Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_bulk_find.setFrameShape(QFrame.StyledPanel)
        self.f_bulk_find.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.f_bulk_find)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.bt_bulk_load_sku = QPushButton(self.f_bulk_find)
        self.bt_bulk_load_sku.setObjectName(u"bt_bulk_load_sku")
        self.bt_bulk_load_sku.setMinimumSize(QSize(141, 51))

        self.gridLayout_13.addWidget(self.bt_bulk_load_sku, 0, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_37 = QLabel(self.f_bulk_find)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_37)

        self.cb_bulk_product = QComboBox(self.f_bulk_find)
        self.cb_bulk_product.setObjectName(u"cb_bulk_product")
        self.cb_bulk_product.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_25.addWidget(self.cb_bulk_product)


        self.gridLayout_13.addLayout(self.horizontalLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(17)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_66 = QLabel(self.f_bulk_find)
        self.label_66.setObjectName(u"label_66")
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_51.addWidget(self.label_66)

        self.cb_bulk_project = QComboBox(self.f_bulk_find)
        self.cb_bulk_project.setObjectName(u"cb_bulk_project")
        self.cb_bulk_project.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_51.addWidget(self.cb_bulk_project)


        self.gridLayout_13.addLayout(self.horizontalLayout_51, 2, 0, 1, 1)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(21)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_67 = QLabel(self.f_bulk_find)
        self.label_67.setObjectName(u"label_67")
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setFont(font3)
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_52.addWidget(self.label_67)

        self.tx_bulk_surfix = QLineEdit(self.f_bulk_find)
        self.tx_bulk_surfix.setObjectName(u"tx_bulk_surfix")
        self.tx_bulk_surfix.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_52.addWidget(self.tx_bulk_surfix)


        self.gridLayout_13.addLayout(self.horizontalLayout_52, 3, 0, 1, 1)

        self.label_6 = QLabel(self.f_bulk_find)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.label_6, 4, 0, 1, 1)

        self.list_bulk_sku = QListView(self.f_bulk_find)
        self.list_bulk_sku.setObjectName(u"list_bulk_sku")

        self.gridLayout_13.addWidget(self.list_bulk_sku, 5, 0, 1, 1)


        self.gridLayout_17.addWidget(self.f_bulk_find, 2, 0, 2, 1)

        self.lb_bulk_caption = QLabel(self.p_bulk)
        self.lb_bulk_caption.setObjectName(u"lb_bulk_caption")
        self.lb_bulk_caption.setFont(font2)
        self.lb_bulk_caption.setStyleSheet(u"color: #26364d;\n"
"font-weight:bold;")

        self.gridLayout_17.addWidget(self.lb_bulk_caption, 0, 0, 1, 4)

        self.label_68 = QLabel(self.p_bulk)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)
        self.label_68.setStyleSheet(u"color: #26364d;")

        self.gridLayout_17.addWidget(self.label_68, 1, 0, 1, 1)

        self.f_button = QFrame(self.p_bulk)
        self.f_button.setObjectName(u"f_button")
        self.f_button.setStyleSheet(u"#f_button\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px 6px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 11px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 3px;\n"
"}\n"
"\n"
"#f_button QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_button QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 trong Qt CSS"
                        ", ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_button.setFrameShape(QFrame.StyledPanel)
        self.f_button.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.f_button)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(4)
        self.bt_bulk_keyConfig = QPushButton(self.f_button)
        self.bt_bulk_keyConfig.setObjectName(u"bt_bulk_keyConfig")
        sizePolicy2.setHeightForWidth(self.bt_bulk_keyConfig.sizePolicy().hasHeightForWidth())
        self.bt_bulk_keyConfig.setSizePolicy(sizePolicy2)
        self.bt_bulk_keyConfig.setMinimumSize(QSize(0, 0))
        self.bt_bulk_keyConfig.setMaximumSize(QSize(101, 41))

        self.gridLayout_8.addWidget(self.bt_bulk_keyConfig, 0, 0, 1, 1)

        self.bt_bulk_single_inspect = QPushButton(self.f_button)
        self.bt_bulk_single_inspect.setObjectName(u"bt_bulk_single_inspect")
        sizePolicy2.setHeightForWidth(self.bt_bulk_single_inspect.sizePolicy().hasHeightForWidth())
        self.bt_bulk_single_inspect.setSizePolicy(sizePolicy2)
        self.bt_bulk_single_inspect.setMinimumSize(QSize(0, 0))
        self.bt_bulk_single_inspect.setMaximumSize(QSize(111, 41))

        self.gridLayout_8.addWidget(self.bt_bulk_single_inspect, 0, 1, 1, 1)

        self.bt_bulk_autoLoad_key = QPushButton(self.f_button)
        self.bt_bulk_autoLoad_key.setObjectName(u"bt_bulk_autoLoad_key")
        sizePolicy2.setHeightForWidth(self.bt_bulk_autoLoad_key.sizePolicy().hasHeightForWidth())
        self.bt_bulk_autoLoad_key.setSizePolicy(sizePolicy2)
        self.bt_bulk_autoLoad_key.setMinimumSize(QSize(0, 0))
        self.bt_bulk_autoLoad_key.setMaximumSize(QSize(111, 41))

        self.gridLayout_8.addWidget(self.bt_bulk_autoLoad_key, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.f_button, 2, 1, 1, 1)

        self.f_bulk_content = QFrame(self.p_bulk)
        self.f_bulk_content.setObjectName(u"f_bulk_content")
        self.f_bulk_content.setStyleSheet(u"#f_bulk_content\n"
"{\n"
"	background-color:#26364d;\n"
"}")
        self.f_bulk_content.setFrameShape(QFrame.StyledPanel)
        self.f_bulk_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.f_bulk_content)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_70 = QLabel(self.f_bulk_content)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font3)
        self.label_70.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_70)

        self.list_bulk_keyConfig = QTableView(self.f_bulk_content)
        self.list_bulk_keyConfig.setObjectName(u"list_bulk_keyConfig")

        self.verticalLayout_8.addWidget(self.list_bulk_keyConfig)


        self.gridLayout_12.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_71 = QLabel(self.f_bulk_content)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font3)
        self.label_71.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_71)

        self.list_bulk_labelPrint = QTableView(self.f_bulk_content)
        self.list_bulk_labelPrint.setObjectName(u"list_bulk_labelPrint")

        self.verticalLayout_9.addWidget(self.list_bulk_labelPrint)


        self.gridLayout_12.addLayout(self.verticalLayout_9, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_72 = QLabel(self.f_bulk_content)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font3)
        self.label_72.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_72)

        self.tableView_3 = QTableView(self.f_bulk_content)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_10.addWidget(self.tableView_3)


        self.gridLayout_12.addLayout(self.verticalLayout_10, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.f_bulk_content, 3, 1, 1, 3)

        self.f_button_print = QFrame(self.p_bulk)
        self.f_button_print.setObjectName(u"f_button_print")
        self.f_button_print.setStyleSheet(u"#f_button_print\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 12px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 5px;\n"
"}\n"
"\n"
"#f_button_print QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_button_print QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3"
                        " trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_button_print.setFrameShape(QFrame.StyledPanel)
        self.f_button_print.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.f_button_print)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(4)
        self.bt_labelPrint_packing = QPushButton(self.f_button_print)
        self.bt_labelPrint_packing.setObjectName(u"bt_labelPrint_packing")
        self.bt_labelPrint_packing.setMinimumSize(QSize(91, 41))

        self.gridLayout_9.addWidget(self.bt_labelPrint_packing, 0, 0, 1, 1)

        self.bt_labelPrint_FATP = QPushButton(self.f_button_print)
        self.bt_labelPrint_FATP.setObjectName(u"bt_labelPrint_FATP")
        self.bt_labelPrint_FATP.setMinimumSize(QSize(91, 41))

        self.gridLayout_9.addWidget(self.bt_labelPrint_FATP, 0, 1, 1, 1)

        self.bt_labelPrint_CG = QPushButton(self.f_button_print)
        self.bt_labelPrint_CG.setObjectName(u"bt_labelPrint_CG")
        self.bt_labelPrint_CG.setMinimumSize(QSize(91, 41))

        self.gridLayout_9.addWidget(self.bt_labelPrint_CG, 0, 2, 1, 1)

        self.bt_labelPrint_BG = QPushButton(self.f_button_print)
        self.bt_labelPrint_BG.setObjectName(u"bt_labelPrint_BG")
        self.bt_labelPrint_BG.setMinimumSize(QSize(91, 41))

        self.gridLayout_9.addWidget(self.bt_labelPrint_BG, 0, 3, 1, 1)

        self.bt_labelPrint_autoLoad = QPushButton(self.f_button_print)
        self.bt_labelPrint_autoLoad.setObjectName(u"bt_labelPrint_autoLoad")
        self.bt_labelPrint_autoLoad.setMinimumSize(QSize(91, 41))

        self.gridLayout_9.addWidget(self.bt_labelPrint_autoLoad, 0, 4, 1, 1)


        self.gridLayout_17.addWidget(self.f_button_print, 2, 2, 1, 2)

        self.label_69 = QLabel(self.p_bulk)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font3)
        self.label_69.setStyleSheet(u"color: #26364d;")

        self.gridLayout_17.addWidget(self.label_69, 1, 2, 1, 2)

        self.label = QLabel(self.p_bulk)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #26364d;")

        self.gridLayout_17.addWidget(self.label, 1, 1, 1, 1)

        self.mulPage.addWidget(self.p_bulk)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_22 = QGridLayout(self.page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.lb_avartar = QLabel(self.page)
        self.lb_avartar.setObjectName(u"lb_avartar")
        self.lb_avartar.setScaledContents(True)

        self.gridLayout_22.addWidget(self.lb_avartar, 0, 0, 1, 1)

        self.mulPage.addWidget(self.page)
        self.p_main_single = QWidget()
        self.p_main_single.setObjectName(u"p_main_single")
        self.gridLayout_18 = QGridLayout(self.p_main_single)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.lb_maintain_caption = QLabel(self.p_main_single)
        self.lb_maintain_caption.setObjectName(u"lb_maintain_caption")
        self.lb_maintain_caption.setFont(font2)
        self.lb_maintain_caption.setStyleSheet(u"color: #26364d;\n"
"font-weight:bold;")

        self.gridLayout_18.addWidget(self.lb_maintain_caption, 0, 0, 1, 3)

        self.f_single_find = QFrame(self.p_main_single)
        self.f_single_find.setObjectName(u"f_single_find")
        sizePolicy.setHeightForWidth(self.f_single_find.sizePolicy().hasHeightForWidth())
        self.f_single_find.setSizePolicy(sizePolicy)
        self.f_single_find.setMinimumSize(QSize(171, 521))
        self.f_single_find.setStyleSheet(u"#f_single_find\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px 6px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 15px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 3px;\n"
"}\n"
"\n"
"#f_single_find QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_single_find QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3"
                        " trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_single_find.setFrameShape(QFrame.StyledPanel)
        self.f_single_find.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.f_single_find)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.bt_maintain_load_sku_2 = QPushButton(self.f_single_find)
        self.bt_maintain_load_sku_2.setObjectName(u"bt_maintain_load_sku_2")
        self.bt_maintain_load_sku_2.setMinimumSize(QSize(151, 41))

        self.gridLayout_5.addWidget(self.bt_maintain_load_sku_2, 0, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_40 = QLabel(self.f_single_find)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.label_40)

        self.cb_maintain_product_2 = QComboBox(self.f_single_find)
        self.cb_maintain_product_2.setObjectName(u"cb_maintain_product_2")

        self.horizontalLayout_32.addWidget(self.cb_maintain_product_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_32, 1, 0, 1, 1)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setSpacing(17)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_80 = QLabel(self.f_single_find)
        self.label_80.setObjectName(u"label_80")
        sizePolicy.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy)
        self.label_80.setFont(font3)
        self.label_80.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_58.addWidget(self.label_80)

        self.cb_maintain_project_2 = QComboBox(self.f_single_find)
        self.cb_maintain_project_2.setObjectName(u"cb_maintain_project_2")

        self.horizontalLayout_58.addWidget(self.cb_maintain_project_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_58, 2, 0, 1, 1)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(21)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_79 = QLabel(self.f_single_find)
        self.label_79.setObjectName(u"label_79")
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setFont(font3)
        self.label_79.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_57.addWidget(self.label_79)

        self.tx_maintain_surfix_2 = QLineEdit(self.f_single_find)
        self.tx_maintain_surfix_2.setObjectName(u"tx_maintain_surfix_2")

        self.horizontalLayout_57.addWidget(self.tx_maintain_surfix_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_57, 3, 0, 1, 1)

        self.label_11 = QLabel(self.f_single_find)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_11, 4, 0, 1, 1)

        self.tx_maintain_sku_2 = QLineEdit(self.f_single_find)
        self.tx_maintain_sku_2.setObjectName(u"tx_maintain_sku_2")
        self.tx_maintain_sku_2.setMinimumSize(QSize(151, 31))

        self.gridLayout_5.addWidget(self.tx_maintain_sku_2, 5, 0, 1, 1)

        self.list_maintain_sku_2 = QListView(self.f_single_find)
        self.list_maintain_sku_2.setObjectName(u"list_maintain_sku_2")

        self.gridLayout_5.addWidget(self.list_maintain_sku_2, 6, 0, 1, 1)


        self.gridLayout_18.addWidget(self.f_single_find, 1, 0, 1, 1)

        self.f_single_key = QFrame(self.p_main_single)
        self.f_single_key.setObjectName(u"f_single_key")
        self.f_single_key.setStyleSheet(u"#f_single_key\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px 6px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 15px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 3px;\n"
"}\n"
"\n"
"#f_single_key QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_single_key QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 "
                        "trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_single_key.setFrameShape(QFrame.StyledPanel)
        self.f_single_key.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.f_single_key)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lb_branch_text_2 = QLabel(self.f_single_key)
        self.lb_branch_text_2.setObjectName(u"lb_branch_text_2")
        self.lb_branch_text_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"	text-align: left;\n"
"}")
        self.lb_branch_text_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lb_branch_text_2, 0, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.chk_maintain_all = QCheckBox(self.f_single_key)
        self.chk_maintain_all.setObjectName(u"chk_maintain_all")

        self.horizontalLayout_29.addWidget(self.chk_maintain_all)

        self.chk_maintain_des = QCheckBox(self.f_single_key)
        self.chk_maintain_des.setObjectName(u"chk_maintain_des")

        self.horizontalLayout_29.addWidget(self.chk_maintain_des)

        self.chk_maintain_upc = QCheckBox(self.f_single_key)
        self.chk_maintain_upc.setObjectName(u"chk_maintain_upc")

        self.horizontalLayout_29.addWidget(self.chk_maintain_upc)

        self.chk_maintain_brand = QCheckBox(self.f_single_key)
        self.chk_maintain_brand.setObjectName(u"chk_maintain_brand")

        self.horizontalLayout_29.addWidget(self.chk_maintain_brand)

        self.chk_maintain_blabel = QCheckBox(self.f_single_key)
        self.chk_maintain_blabel.setObjectName(u"chk_maintain_blabel")

        self.horizontalLayout_29.addWidget(self.chk_maintain_blabel)

        self.chk_maintain_rlabel = QCheckBox(self.f_single_key)
        self.chk_maintain_rlabel.setObjectName(u"chk_maintain_rlabel")

        self.horizontalLayout_29.addWidget(self.chk_maintain_rlabel)


        self.gridLayout_10.addLayout(self.horizontalLayout_29, 1, 0, 1, 3)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.chk_maintain_sap = QCheckBox(self.f_single_key)
        self.chk_maintain_sap.setObjectName(u"chk_maintain_sap")

        self.horizontalLayout_28.addWidget(self.chk_maintain_sap)

        self.chk_maintain_color = QCheckBox(self.f_single_key)
        self.chk_maintain_color.setObjectName(u"chk_maintain_color")

        self.horizontalLayout_28.addWidget(self.chk_maintain_color)

        self.chk_maintain_mlabel = QCheckBox(self.f_single_key)
        self.chk_maintain_mlabel.setObjectName(u"chk_maintain_mlabel")

        self.horizontalLayout_28.addWidget(self.chk_maintain_mlabel)

        self.chk_maintain_price = QCheckBox(self.f_single_key)
        self.chk_maintain_price.setObjectName(u"chk_maintain_price")

        self.horizontalLayout_28.addWidget(self.chk_maintain_price)

        self.chk_maintain_qr = QCheckBox(self.f_single_key)
        self.chk_maintain_qr.setObjectName(u"chk_maintain_qr")

        self.horizontalLayout_28.addWidget(self.chk_maintain_qr)


        self.gridLayout_10.addLayout(self.horizontalLayout_28, 2, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(124, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.bt_maintain_load_key = QPushButton(self.f_single_key)
        self.bt_maintain_load_key.setObjectName(u"bt_maintain_load_key")
        self.bt_maintain_load_key.setMinimumSize(QSize(131, 41))

        self.gridLayout_10.addWidget(self.bt_maintain_load_key, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(124, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.lb_branch_text_4 = QLabel(self.f_single_key)
        self.lb_branch_text_4.setObjectName(u"lb_branch_text_4")
        self.lb_branch_text_4.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")
        self.lb_branch_text_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lb_branch_text_4, 4, 0, 1, 1)

        self.table_maintain_key = QTableView(self.f_single_key)
        self.table_maintain_key.setObjectName(u"table_maintain_key")

        self.gridLayout_10.addWidget(self.table_maintain_key, 5, 0, 1, 3)


        self.gridLayout_18.addWidget(self.f_single_key, 1, 1, 1, 1)

        self.f_single_Print = QFrame(self.p_main_single)
        self.f_single_Print.setObjectName(u"f_single_Print")
        self.f_single_Print.setStyleSheet(u"#f_single_Print\n"
"{\n"
"	background-color:#26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 3px 6px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 15px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    text-align: center;\n"
"   padding-left: 3px;\n"
"}\n"
"\n"
"#f_single_Print QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_single_Print QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3"
                        " trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_single_Print.setFrameShape(QFrame.StyledPanel)
        self.f_single_Print.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.f_single_Print)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lb_branch_text_3 = QLabel(self.f_single_Print)
        self.lb_branch_text_3.setObjectName(u"lb_branch_text_3")
        self.lb_branch_text_3.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")
        self.lb_branch_text_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lb_branch_text_3, 0, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.chk_maintain_print_all = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_all.setObjectName(u"chk_maintain_print_all")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_all)

        self.chk_maintain_print_carton = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_carton.setObjectName(u"chk_maintain_print_carton")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_carton)

        self.chk_maintain_print_pallet1 = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_pallet1.setObjectName(u"chk_maintain_print_pallet1")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_pallet1)

        self.chk_maintain_print_pallet2 = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_pallet2.setObjectName(u"chk_maintain_print_pallet2")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_pallet2)

        self.chk_maintain_print_pallet3 = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_pallet3.setObjectName(u"chk_maintain_print_pallet3")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_pallet3)

        self.chk_maintain_print_ship = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_ship.setObjectName(u"chk_maintain_print_ship")

        self.horizontalLayout_30.addWidget(self.chk_maintain_print_ship)


        self.gridLayout_11.addLayout(self.horizontalLayout_30, 1, 0, 1, 2)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.chk_maintain_print_carton2 = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_carton2.setObjectName(u"chk_maintain_print_carton2")

        self.horizontalLayout_31.addWidget(self.chk_maintain_print_carton2)

        self.chk_maintain_print_overlay = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_overlay.setObjectName(u"chk_maintain_print_overlay")

        self.horizontalLayout_31.addWidget(self.chk_maintain_print_overlay)

        self.chk_maintain_print_wic = QCheckBox(self.f_single_Print)
        self.chk_maintain_print_wic.setObjectName(u"chk_maintain_print_wic")

        self.horizontalLayout_31.addWidget(self.chk_maintain_print_wic)


        self.gridLayout_11.addLayout(self.horizontalLayout_31, 2, 1, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_5 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)

        self.bt_maintain_print_load = QPushButton(self.f_single_Print)
        self.bt_maintain_print_load.setObjectName(u"bt_maintain_print_load")
        self.bt_maintain_print_load.setMinimumSize(QSize(131, 41))

        self.horizontalLayout_27.addWidget(self.bt_maintain_print_load)

        self.horizontalSpacer_6 = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_6)


        self.gridLayout_11.addLayout(self.horizontalLayout_27, 3, 0, 1, 2)

        self.lb_branch_text_5 = QLabel(self.f_single_Print)
        self.lb_branch_text_5.setObjectName(u"lb_branch_text_5")
        self.lb_branch_text_5.setStyleSheet(u"QLabel\n"
"{\n"
"	color:white;\n"
"}")
        self.lb_branch_text_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lb_branch_text_5, 4, 0, 1, 1)

        self.table_maintain_print_upload = QTableView(self.f_single_Print)
        self.table_maintain_print_upload.setObjectName(u"table_maintain_print_upload")

        self.gridLayout_11.addWidget(self.table_maintain_print_upload, 5, 0, 1, 2)


        self.gridLayout_18.addWidget(self.f_single_Print, 1, 2, 1, 1)

        self.mulPage.addWidget(self.p_main_single)
        self.p_realtime_chk = QWidget()
        self.p_realtime_chk.setObjectName(u"p_realtime_chk")
        self.gridLayout_19 = QGridLayout(self.p_realtime_chk)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.lb_tieuDe_5 = QLabel(self.p_realtime_chk)
        self.lb_tieuDe_5.setObjectName(u"lb_tieuDe_5")
        self.lb_tieuDe_5.setFont(font2)
        self.lb_tieuDe_5.setStyleSheet(u"color: #26364d;\n"
"font-weight:bold;\n"
"")

        self.gridLayout_19.addWidget(self.lb_tieuDe_5, 0, 0, 1, 2)

        self.f_real_find = QFrame(self.p_realtime_chk)
        self.f_real_find.setObjectName(u"f_real_find")
        sizePolicy.setHeightForWidth(self.f_real_find.sizePolicy().hasHeightForWidth())
        self.f_real_find.setSizePolicy(sizePolicy)
        self.f_real_find.setMinimumSize(QSize(191, 521))
        self.f_real_find.setStyleSheet(u"#f_real_find\n"
"{\n"
" background-color: #26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 10px 20px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 16px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    qproperty-iconSize: 24px 24px;\n"
"    text-align: center;\n"
"   padding-left: 20px;\n"
"}\n"
"\n"
"#f_real_find QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}\n"
"#f_real_find QPushButton:pressed {\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95)"
                        ";       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}")
        self.f_real_find.setFrameShape(QFrame.StyledPanel)
        self.f_real_find.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.f_real_find)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.bt_realtime_load_sku = QPushButton(self.f_real_find)
        self.bt_realtime_load_sku.setObjectName(u"bt_realtime_load_sku")
        self.bt_realtime_load_sku.setMinimumSize(QSize(151, 41))

        self.gridLayout_16.addWidget(self.bt_realtime_load_sku, 0, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_38 = QLabel(self.f_real_find)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_38)

        self.cb_realtime_product = QComboBox(self.f_real_find)
        self.cb_realtime_product.setObjectName(u"cb_realtime_product")
        self.cb_realtime_product.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_26.addWidget(self.cb_realtime_product)


        self.gridLayout_16.addLayout(self.horizontalLayout_26, 1, 0, 1, 1)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(17)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_74 = QLabel(self.f_real_find)
        self.label_74.setObjectName(u"label_74")
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setFont(font3)
        self.label_74.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_54.addWidget(self.label_74)

        self.cb_realtime_project = QComboBox(self.f_real_find)
        self.cb_realtime_project.setObjectName(u"cb_realtime_project")
        self.cb_realtime_project.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_54.addWidget(self.cb_realtime_project)


        self.gridLayout_16.addLayout(self.horizontalLayout_54, 2, 0, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(21)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_73 = QLabel(self.f_real_find)
        self.label_73.setObjectName(u"label_73")
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setFont(font3)
        self.label_73.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_53.addWidget(self.label_73)

        self.cb_realtime_surfix = QLineEdit(self.f_real_find)
        self.cb_realtime_surfix.setObjectName(u"cb_realtime_surfix")
        self.cb_realtime_surfix.setMinimumSize(QSize(97, 24))

        self.horizontalLayout_53.addWidget(self.cb_realtime_surfix)


        self.gridLayout_16.addLayout(self.horizontalLayout_53, 3, 0, 1, 1)

        self.bt_realtime_inspect = QPushButton(self.f_real_find)
        self.bt_realtime_inspect.setObjectName(u"bt_realtime_inspect")
        self.bt_realtime_inspect.setMinimumSize(QSize(151, 41))

        self.gridLayout_16.addWidget(self.bt_realtime_inspect, 4, 0, 1, 1)

        self.label_7 = QLabel(self.f_real_find)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.label_7, 5, 0, 1, 1)

        self.tx_realtime_single_sku = QLineEdit(self.f_real_find)
        self.tx_realtime_single_sku.setObjectName(u"tx_realtime_single_sku")
        self.tx_realtime_single_sku.setMinimumSize(QSize(151, 31))

        self.gridLayout_16.addWidget(self.tx_realtime_single_sku, 6, 0, 1, 1)

        self.list_realtime_sku = QListView(self.f_real_find)
        self.list_realtime_sku.setObjectName(u"list_realtime_sku")

        self.gridLayout_16.addWidget(self.list_realtime_sku, 7, 0, 1, 1)


        self.gridLayout_19.addWidget(self.f_real_find, 1, 0, 1, 1)

        self.f_real_content = QFrame(self.p_realtime_chk)
        self.f_real_content.setObjectName(u"f_real_content")
        self.f_real_content.setStyleSheet(u"#f_real_content\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.f_real_content.setFrameShape(QFrame.StyledPanel)
        self.f_real_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.f_real_content)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_75 = QLabel(self.f_real_content)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font3)
        self.label_75.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_75)

        self.table_realtime_keyconfig = QTableView(self.f_real_content)
        self.table_realtime_keyconfig.setObjectName(u"table_realtime_keyconfig")

        self.verticalLayout_11.addWidget(self.table_realtime_keyconfig)


        self.gridLayout_15.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_76 = QLabel(self.f_real_content)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font3)
        self.label_76.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_76)

        self.table_realtime_result = QTableView(self.f_real_content)
        self.table_realtime_result.setObjectName(u"table_realtime_result")

        self.verticalLayout_12.addWidget(self.table_realtime_result)


        self.gridLayout_15.addLayout(self.verticalLayout_12, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.f_real_content, 1, 1, 1, 1)

        self.mulPage.addWidget(self.p_realtime_chk)

        self.gridLayout_7.addWidget(self.mulPage, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frMain, 1, 1, 1, 1)

        self.frfooter = QFrame(self.centralwidget)
        self.frfooter.setObjectName(u"frfooter")
        self.frfooter.setStyleSheet(u"#frfooter\n"
"{\n"
"	background-color: #26364d;\n"
"}\n"
"")
        self.frfooter.setFrameShape(QFrame.StyledPanel)
        self.frfooter.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frfooter)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lb_notice = QLabel(self.frfooter)
        self.lb_notice.setObjectName(u"lb_notice")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.lb_notice.setFont(font4)
        self.lb_notice.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_notice.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lb_notice, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frfooter, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mulPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_branch_icon.setText("")
        self.lb_branch_text.setText(QCoreApplication.translate("MainWindow", u"PE Label", None))
        self.bt_view_config.setText(QCoreApplication.translate("MainWindow", u"View Label Config", None))
        self.bt_bulk_import.setText(QCoreApplication.translate("MainWindow", u"Bulk Import File", None))
        self.bt_single_maintain.setText(QCoreApplication.translate("MainWindow", u"Maintain Single Item", None))
        self.bt_realtime_check.setText(QCoreApplication.translate("MainWindow", u"Realtime Ifuse Check", None))
        self.lbHeader.setText(QCoreApplication.translate("MainWindow", u"PE Control Label Configuration", None))
        self.lb_view_caption.setText(QCoreApplication.translate("MainWindow", u"Check Label Configuration By SKU", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Product :", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Project :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Region :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Search SKU :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"M-Label", None))
        self.tx_view_mlabel.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Normal Sku :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ATT & TMO Only :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"B-Label", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"R-Label", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"UPC", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IN Only :", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"QR-Code", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Normal Sku :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Carton", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Pallet1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Pallet2", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pallet3", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Repair", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Ship", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Over", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"IN Only :", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Carton2", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"GBP-W", None))
        self.bt_bulk_load_sku.setText(QCoreApplication.translate("MainWindow", u"Load SKU List", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Product :", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Surfix", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"List SKU :", None))
        self.lb_bulk_caption.setText(QCoreApplication.translate("MainWindow", u"Export Bulk Label Configuration Excel File & Auto Load Bulk File", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"SKU Load Area :", None))
        self.bt_bulk_keyConfig.setText(QCoreApplication.translate("MainWindow", u"Create KeyConfig", None))
        self.bt_bulk_single_inspect.setText(QCoreApplication.translate("MainWindow", u"Inspect Single", None))
        self.bt_bulk_autoLoad_key.setText(QCoreApplication.translate("MainWindow", u"Auto Upload", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Bulk Keyconfig File", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Bulk Keyconfig Inspection", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"LabelPrint Bulk File", None))
        self.bt_labelPrint_packing.setText(QCoreApplication.translate("MainWindow", u"Create Packing", None))
        self.bt_labelPrint_FATP.setText(QCoreApplication.translate("MainWindow", u"Create FATP", None))
        self.bt_labelPrint_CG.setText(QCoreApplication.translate("MainWindow", u"Create CG", None))
        self.bt_labelPrint_BG.setText(QCoreApplication.translate("MainWindow", u"Create BG", None))
        self.bt_labelPrint_autoLoad.setText(QCoreApplication.translate("MainWindow", u"Auto Upload", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"LabelPrint Function :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KeyConfig Function :", None))
        self.lb_avartar.setText("")
        self.lb_maintain_caption.setText(QCoreApplication.translate("MainWindow", u"Maintain Label By Single Step", None))
        self.bt_maintain_load_sku_2.setText(QCoreApplication.translate("MainWindow", u"Load SKU List", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Product :", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Surfix", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Single SKU :", None))
        self.lb_branch_text_2.setText(QCoreApplication.translate("MainWindow", u"KeyConfig :", None))
        self.chk_maintain_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.chk_maintain_des.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.chk_maintain_upc.setText(QCoreApplication.translate("MainWindow", u"UPC", None))
        self.chk_maintain_brand.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.chk_maintain_blabel.setText(QCoreApplication.translate("MainWindow", u"B-Label", None))
        self.chk_maintain_rlabel.setText(QCoreApplication.translate("MainWindow", u"R-Label", None))
        self.chk_maintain_sap.setText(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.chk_maintain_color.setText(QCoreApplication.translate("MainWindow", u"Carton-Color", None))
        self.chk_maintain_mlabel.setText(QCoreApplication.translate("MainWindow", u"M-Label", None))
        self.chk_maintain_price.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.chk_maintain_qr.setText(QCoreApplication.translate("MainWindow", u"QR-CODE", None))
        self.bt_maintain_load_key.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.lb_branch_text_4.setText(QCoreApplication.translate("MainWindow", u"Uploaded List :", None))
        self.lb_branch_text_3.setText(QCoreApplication.translate("MainWindow", u"LabelPrint :", None))
        self.chk_maintain_print_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.chk_maintain_print_carton.setText(QCoreApplication.translate("MainWindow", u"Carton", None))
        self.chk_maintain_print_pallet1.setText(QCoreApplication.translate("MainWindow", u"Pallet 1", None))
        self.chk_maintain_print_pallet2.setText(QCoreApplication.translate("MainWindow", u"Pallet 2", None))
        self.chk_maintain_print_pallet3.setText(QCoreApplication.translate("MainWindow", u"Pallet 3", None))
        self.chk_maintain_print_ship.setText(QCoreApplication.translate("MainWindow", u"Ship", None))
        self.chk_maintain_print_carton2.setText(QCoreApplication.translate("MainWindow", u"Carton 2", None))
        self.chk_maintain_print_overlay.setText(QCoreApplication.translate("MainWindow", u"Overlay", None))
        self.chk_maintain_print_wic.setText(QCoreApplication.translate("MainWindow", u"WIC", None))
        self.bt_maintain_print_load.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.lb_branch_text_5.setText(QCoreApplication.translate("MainWindow", u"Uploaded List :", None))
        self.lb_tieuDe_5.setText(QCoreApplication.translate("MainWindow", u"Realtime Checking The Label Configuration In Ifuse", None))
        self.bt_realtime_load_sku.setText(QCoreApplication.translate("MainWindow", u"Load SKU List", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Product :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Surfix", None))
        self.bt_realtime_inspect.setText(QCoreApplication.translate("MainWindow", u"Inspect Label Config", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Single SKU :", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Data Extract From Ifuse :", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Inspection Result :", None))
        self.lb_notice.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
    # retranslateUi

