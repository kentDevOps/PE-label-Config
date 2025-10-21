# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadSku.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_skuForm(object):
    def setupUi(self, skuForm):
        if not skuForm.objectName():
            skuForm.setObjectName(u"skuForm")
        skuForm.resize(268, 600)
        icon = QIcon()
        icon.addFile(u"img/kca.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        skuForm.setWindowIcon(icon)
        self.centralwidget = QWidget(skuForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frsku = QFrame(self.centralwidget)
        self.frsku.setObjectName(u"frsku")
        self.frsku.setGeometry(QRect(10, 10, 251, 581))
        self.frsku.setStyleSheet(u"#frsku\n"
"{\n"
" background-color: #26364d;\n"
"}\n"
"QPushButton  {\n"
"    background-color: #26364d;   /* M\u00e0u n\u1ec1n xanh */\n"
"    color: white;             /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    border: 2px solid white;  /* Vi\u1ec1n tr\u1eafng */\n"
"    padding: 5px 8px;       /* Kho\u1ea3ng c\u00e1ch trong */\n"
"    border-radius: 5px;       /* Bo g\u00f3c */\n"
"    cursor: pointer;          /* Hi\u1ec7n tay khi hover */\n"
"    font-size: 11px;          /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    qproperty-iconSize: 24px 24px;\n"
"    text-align: center;\n"
"   padding-left: 5px;\n"
"}\n"
"\n"
"#frsku QPushButton:hover {\n"
"    background-color: #3a5a80; /* \u0110\u1ed5i m\u00e0u khi hover */\n"
"}")
        self.frsku.setFrameShape(QFrame.Shape.StyledPanel)
        self.frsku.setFrameShadow(QFrame.Shadow.Raised)
        self.lb_region_bob = QLabel(self.frsku)
        self.lb_region_bob.setObjectName(u"lb_region_bob")
        self.lb_region_bob.setGeometry(QRect(10, 10, 221, 20))
        font = QFont()
        font.setFamilies([u"Stencil"])
        font.setPointSize(9)
        self.lb_region_bob.setFont(font)
        self.lb_region_bob.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_region_bob.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_region_bob.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tx_sku = QTextEdit(self.frsku)
        self.tx_sku.setObjectName(u"tx_sku")
        self.tx_sku.setGeometry(QRect(20, 40, 211, 481))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.tx_sku.setFont(font1)
        self.tx_sku.setStyleSheet(u"#tx_sku\n"
"{\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"}")
        self.bt_save = QPushButton(self.frsku)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setGeometry(QRect(90, 530, 65, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_save.sizePolicy().hasHeightForWidth())
        self.bt_save.setSizePolicy(sizePolicy)
        self.bt_save.setMinimumSize(QSize(65, 41))
        self.bt_save.setMaximumSize(QSize(65, 41))
        self.bt_save.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.bt_save.setIconSize(QSize(24, 24))
        self.bt_save.setCheckable(True)
        self.bt_save.setFlat(False)
        skuForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(skuForm)

        QMetaObject.connectSlotsByName(skuForm)
    # setupUi

    def retranslateUi(self, skuForm):
        skuForm.setWindowTitle(QCoreApplication.translate("skuForm", u"Add SKU LIST", None))
        self.lb_region_bob.setText(QCoreApplication.translate("skuForm", u"SKU LIST", None))
        self.bt_save.setText(QCoreApplication.translate("skuForm", u"Save", None))
    # retranslateUi

