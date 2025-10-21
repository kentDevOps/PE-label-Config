# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
    QWidget)
class Ui_retailForm(QMainWindow):
    def setupUi(self, retailForm):
        if not retailForm.objectName():
            retailForm.setObjectName(u"retailForm")
        retailForm.resize(587, 303)
        self.centralwidget = QWidget(retailForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frHeader = QFrame(self.centralwidget)
        self.frHeader.setObjectName(u"frHeader")
        font = QFont()
        font.setPointSize(7)
        self.frHeader.setFont(font)
        self.frHeader.setStyleSheet(u"#frHeader\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_r_sku = QLabel(self.frHeader)
        self.lb_r_sku.setObjectName(u"lb_r_sku")
        font1 = QFont()
        font1.setFamilies([u"Stencil"])
        font1.setPointSize(9)
        self.lb_r_sku.setFont(font1)
        self.lb_r_sku.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_r_sku.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_r_sku.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_r_sku, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frHeader)

        self.frRegion = QFrame(self.centralwidget)
        self.frRegion.setObjectName(u"frRegion")
        self.frRegion.setFont(font)
        self.frRegion.setStyleSheet(u"#frRegion\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frRegion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frRegion.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frRegion)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_r_region = QLabel(self.frRegion)
        self.lb_r_region.setObjectName(u"lb_r_region")
        self.lb_r_region.setFont(font1)
        self.lb_r_region.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_r_region.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_r_region.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_r_region, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frRegion)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.frRetail = QFrame(self.centralwidget)
        self.frRetail.setObjectName(u"frRetail")
        self.frRetail.setFont(font)
        self.frRetail.setStyleSheet(u"#frRetail\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frRetail.setFrameShape(QFrame.Shape.StyledPanel)
        self.frRetail.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frRetail)
        self.gridLayout.setObjectName(u"gridLayout")
        self.view_retail = QGraphicsView(self.frRetail)
        self.view_retail.setObjectName(u"view_retail")

        self.gridLayout.addWidget(self.view_retail, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frRetail, 1, 0, 1, 1)

        retailForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(retailForm)

        QMetaObject.connectSlotsByName(retailForm)
    # setupUi

    def retranslateUi(self, retailForm):
        retailForm.setWindowTitle(QCoreApplication.translate("retailForm", u"MainWindow", None))
        self.lb_r_sku.setText(QCoreApplication.translate("retailForm", u"SKU", None))
        self.lb_r_region.setText(QCoreApplication.translate("retailForm", u"Region", None))
    # retranslateUi

