# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_manage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(371, 581)
        Dialog.setMinimumSize(QSize(371, 581))
        Dialog.setMaximumSize(QSize(371, 581))
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 130, 351, 441))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 351, 51))
        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(10, 20, 81, 22))
        self.dateEdit.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 21, 20))
        self.dateEdit_2 = QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(120, 20, 81, 22))
        self.dateEdit_2.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_2.setMinimumDate(QDate(2021, 1, 1))
        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(210, 20, 61, 23))
        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(280, 20, 61, 23))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 70, 351, 51))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 191, 20))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 20, 61, 22))
        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(280, 20, 61, 23))
        QWidget.setTabOrder(self.dateEdit, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.tableWidget)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u7ba1\u7406", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u65e5\u671f\u9009\u62e9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u81f3", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"\u4eca\u5929", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"\u672c\u5468", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u67e5\u627e", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4", None))

        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"\u67e5\u627e", None))
    # retranslateUi

