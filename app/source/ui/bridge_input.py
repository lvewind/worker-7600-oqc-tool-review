# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bridge_input.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_bridge_input(object):
    def setupUi(self, Dialog_bridge_input):
        if not Dialog_bridge_input.objectName():
            Dialog_bridge_input.setObjectName(u"Dialog_bridge_input")
        Dialog_bridge_input.setWindowModality(Qt.NonModal)
        Dialog_bridge_input.resize(291, 421)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_bridge_input.sizePolicy().hasHeightForWidth())
        Dialog_bridge_input.setSizePolicy(sizePolicy)
        Dialog_bridge_input.setMinimumSize(QSize(291, 421))
        Dialog_bridge_input.setMaximumSize(QSize(291, 421))
        Dialog_bridge_input.setModal(False)
        self.groupBox_2 = QGroupBox(Dialog_bridge_input)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 220, 231, 51))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        self.groupBox_2.setFont(font)
        self.lineEdit_main_5G_down = QLineEdit(self.groupBox_2)
        self.lineEdit_main_5G_down.setObjectName(u"lineEdit_main_5G_down")
        self.lineEdit_main_5G_down.setGeometry(QRect(10, 20, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lineEdit_main_5G_down.setFont(font1)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 20, 71, 16))
        self.label_2.setFont(font)
        self.groupBox_4 = QGroupBox(Dialog_bridge_input)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 40, 231, 51))
        self.groupBox_4.setFont(font)
        self.lineEdit_bridge_5G_down = QLineEdit(self.groupBox_4)
        self.lineEdit_bridge_5G_down.setObjectName(u"lineEdit_bridge_5G_down")
        self.lineEdit_bridge_5G_down.setGeometry(QRect(10, 20, 131, 31))
        self.lineEdit_bridge_5G_down.setFont(font1)
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 20, 71, 16))
        self.label_4.setFont(font)
        self.pushButton_save = QPushButton(Dialog_bridge_input)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(110, 370, 75, 23))
        self.pushButton_save.setFont(font)
        self.pushButton_save.setFocusPolicy(Qt.NoFocus)
        self.label_5 = QLabel(Dialog_bridge_input)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 350, 221, 16))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_sn = QLabel(Dialog_bridge_input)
        self.label_sn.setObjectName(u"label_sn")
        self.label_sn.setGeometry(QRect(40, 10, 231, 21))
        self.label_sn.setFont(font)
        self.groupBox_5 = QGroupBox(Dialog_bridge_input)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 110, 231, 51))
        self.groupBox_5.setFont(font)
        self.lineEdit_bridge_5G_up = QLineEdit(self.groupBox_5)
        self.lineEdit_bridge_5G_up.setObjectName(u"lineEdit_bridge_5G_up")
        self.lineEdit_bridge_5G_up.setGeometry(QRect(10, 20, 131, 31))
        self.lineEdit_bridge_5G_up.setFont(font1)
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 20, 71, 16))
        self.label_6.setFont(font)
        self.groupBox_6 = QGroupBox(Dialog_bridge_input)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(30, 290, 231, 51))
        self.groupBox_6.setFont(font)
        self.lineEdit_main_5G_up = QLineEdit(self.groupBox_6)
        self.lineEdit_main_5G_up.setObjectName(u"lineEdit_main_5G_up")
        self.lineEdit_main_5G_up.setGeometry(QRect(10, 20, 131, 31))
        self.lineEdit_main_5G_up.setFont(font1)
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 20, 71, 16))
        self.label_7.setFont(font)
        QWidget.setTabOrder(self.lineEdit_main_5G_down, self.lineEdit_main_5G_up)
        QWidget.setTabOrder(self.lineEdit_main_5G_up, self.lineEdit_bridge_5G_down)
        QWidget.setTabOrder(self.lineEdit_bridge_5G_down, self.lineEdit_bridge_5G_up)

        self.retranslateUi(Dialog_bridge_input)

        QMetaObject.connectSlotsByName(Dialog_bridge_input)
    # setupUi

    def retranslateUi(self, Dialog_bridge_input):
        Dialog_bridge_input.setWindowTitle(QCoreApplication.translate("Dialog_bridge_input", u"Bridge\u6570\u636e\u8f93\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_bridge_input", u"Main 5G Down", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_bridge_input", u"Mbits/sec", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_bridge_input", u"Bridge 5G Down", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_bridge_input", u"Mbits/sec", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog_bridge_input", u"\u4fdd\u5b58", None))
        self.label_5.setText("")
        self.label_sn.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_bridge_input", u"Bridge 5G Up", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_bridge_input", u"Mbits/sec", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog_bridge_input", u"Main 5G Up", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_bridge_input", u"Mbits/sec", None))
    # retranslateUi

