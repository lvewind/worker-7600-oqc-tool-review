# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_usb_power.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_save_usb_power(object):
    def setupUi(self, Dialog_save_usb_power):
        if not Dialog_save_usb_power.objectName():
            Dialog_save_usb_power.setObjectName(u"Dialog_save_usb_power")
        Dialog_save_usb_power.resize(320, 240)
        self.lineEdit_a = QLineEdit(Dialog_save_usb_power)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setGeometry(QRect(110, 100, 91, 41))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_a.setFont(font)
        self.lineEdit_v = QLineEdit(Dialog_save_usb_power)
        self.lineEdit_v.setObjectName(u"lineEdit_v")
        self.lineEdit_v.setGeometry(QRect(110, 38, 91, 41))
        self.lineEdit_v.setFont(font)
        self.label = QLabel(Dialog_save_usb_power)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 51, 21))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label_2 = QLabel(Dialog_save_usb_power)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 51, 16))
        self.label_2.setFont(font1)
        self.pushButton_save = QPushButton(Dialog_save_usb_power)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(120, 190, 75, 23))
        self.pushButton_save.setFont(font1)
        self.label_3 = QLabel(Dialog_save_usb_power)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 110, 31, 16))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog_save_usb_power)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 50, 31, 21))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Dialog_save_usb_power)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 150, 161, 31))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_save_usb_power)

        QMetaObject.connectSlotsByName(Dialog_save_usb_power)
    # setupUi

    def retranslateUi(self, Dialog_save_usb_power):
        Dialog_save_usb_power.setWindowTitle(QCoreApplication.translate("Dialog_save_usb_power", u"Dialog", None))
        self.lineEdit_a.setText(QCoreApplication.translate("Dialog_save_usb_power", u"0.5", None))
        self.lineEdit_v.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_save_usb_power", u"Voltage", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_save_usb_power", u"Current", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog_save_usb_power", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_save_usb_power", u"A", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_save_usb_power", u"V", None))
        self.label_5.setText("")
    # retranslateUi

