# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bob.ui'
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
    QHeaderView, QLabel, QMainWindow, QSizePolicy,
    QTabWidget, QTableView, QWidget)

class Ui_bobForm(QMainWindow):
    def setupUi(self, bobForm):
        if not bobForm.objectName():
            bobForm.setObjectName(u"bobForm")
        bobForm.resize(636, 769)
        self.centralwidget = QWidget(bobForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
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
        self.lb_region_3 = QLabel(self.frHeader)
        self.lb_region_3.setObjectName(u"lb_region_3")
        font1 = QFont()
        font1.setFamilies([u"Stencil"])
        font1.setPointSize(9)
        self.lb_region_3.setFont(font1)
        self.lb_region_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_region_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_region_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_region_3, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frHeader, 0, 0, 1, 2)

        self.frBob = QFrame(self.centralwidget)
        self.frBob.setObjectName(u"frBob")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frBob.sizePolicy().hasHeightForWidth())
        self.frBob.setSizePolicy(sizePolicy)
        self.frBob.setFont(font)
        self.frBob.setStyleSheet(u"#frBob\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frBob.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBob.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frBob)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_region = QLabel(self.frBob)
        self.lb_region.setObjectName(u"lb_region")
        self.lb_region.setFont(font1)
        self.lb_region.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_region.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_region.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_region, 0, 0, 1, 1)

        self.lb_sku = QLabel(self.frBob)
        self.lb_sku.setObjectName(u"lb_sku")
        self.lb_sku.setFont(font1)
        self.lb_sku.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_sku.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_sku.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_sku, 1, 0, 1, 1)

        self.bob_tab = QTabWidget(self.frBob)
        self.bob_tab.setObjectName(u"bob_tab")
        self.img = QWidget()
        self.img.setObjectName(u"img")
        self.gridLayout_7 = QGridLayout(self.img)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.view_bob_img = QGraphicsView(self.img)
        self.view_bob_img.setObjectName(u"view_bob_img")
        self.view_bob_img.setMinimumSize(QSize(280, 600))
        self.view_bob_img.setMaximumSize(QSize(300, 605))

        self.gridLayout_7.addWidget(self.view_bob_img, 0, 0, 1, 1)

        self.bob_tab.addTab(self.img, "")
        self.print = QWidget()
        self.print.setObjectName(u"print")
        self.gridLayout_8 = QGridLayout(self.print)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.view_bob_print = QGraphicsView(self.print)
        self.view_bob_print.setObjectName(u"view_bob_print")
        self.view_bob_print.setMinimumSize(QSize(280, 600))
        self.view_bob_print.setMaximumSize(QSize(280, 600))

        self.gridLayout_8.addWidget(self.view_bob_print, 0, 0, 1, 1)

        self.bob_tab.addTab(self.print, "")

        self.gridLayout_4.addWidget(self.bob_tab, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frBob, 1, 0, 1, 1)

        self.frPrinting = QFrame(self.centralwidget)
        self.frPrinting.setObjectName(u"frPrinting")
        self.frPrinting.setFont(font)
        self.frPrinting.setStyleSheet(u"#frPrinting\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frPrinting.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPrinting.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frPrinting)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableView = QTableView(self.frPrinting)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_9.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frPrinting, 1, 1, 1, 1)

        bobForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(bobForm)

        self.bob_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(bobForm)
    # setupUi

    def retranslateUi(self, bobForm):
        bobForm.setWindowTitle(QCoreApplication.translate("bobForm", u"MainWindow", None))
        self.lb_region_3.setText(QCoreApplication.translate("bobForm", u"Check FAI By Real Image - Printing Plan - BOB ,Carton , Ship Label", None))
        self.lb_region.setText(QCoreApplication.translate("bobForm", u"Region", None))
        self.lb_sku.setText(QCoreApplication.translate("bobForm", u"SKU", None))
        self.bob_tab.setTabText(self.bob_tab.indexOf(self.img), QCoreApplication.translate("bobForm", u"BOB", None))
        self.bob_tab.setTabText(self.bob_tab.indexOf(self.print), QCoreApplication.translate("bobForm", u"Printing", None))
    # retranslateUi

