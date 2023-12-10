# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_message.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog_show_message(object):
    def setupUi(self, Dialog_show_message):
        if not Dialog_show_message.objectName():
            Dialog_show_message.setObjectName(u"Dialog_show_message")
        Dialog_show_message.setWindowModality(Qt.ApplicationModal)
        Dialog_show_message.resize(320, 240)
        self.pushButton = QPushButton(Dialog_show_message)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 170, 101, 31))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.label = QLabel(Dialog_show_message)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 261, 41))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_show_message)

        QMetaObject.connectSlotsByName(Dialog_show_message)
    # setupUi

    def retranslateUi(self, Dialog_show_message):
        Dialog_show_message.setWindowTitle(QCoreApplication.translate("Dialog_show_message", u"\u63d0\u793a", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_show_message", u"\u786e\u5b9a", None))
        self.label.setText("")
    # retranslateUi

