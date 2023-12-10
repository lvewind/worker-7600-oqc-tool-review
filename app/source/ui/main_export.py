# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_export.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 391)
        MainWindow.setMinimumSize(QSize(351, 391))
        MainWindow.setMaximumSize(QSize(351, 391))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 331, 51))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setBold(True)
        self.groupBox.setFont(font)
        self.lineEdit_select_path = QLineEdit(self.groupBox)
        self.lineEdit_select_path.setObjectName(u"lineEdit_select_path")
        self.lineEdit_select_path.setGeometry(QRect(10, 20, 231, 22))
        self.lineEdit_select_path.setFont(font)
        self.pushButton_select_path = QPushButton(self.groupBox)
        self.pushButton_select_path.setObjectName(u"pushButton_select_path")
        self.pushButton_select_path.setGeometry(QRect(250, 20, 71, 23))
        self.pushButton_select_path.setFont(font)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 80, 161, 61))
        self.groupBox_2.setFont(font)
        self.spinBox_start_count = QSpinBox(self.groupBox_2)
        self.spinBox_start_count.setObjectName(u"spinBox_start_count")
        self.spinBox_start_count.setGeometry(QRect(40, 20, 111, 41))
        self.spinBox_start_count.setFont(font)
        self.spinBox_start_count.setMaximum(9999999)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 250, 331, 111))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        self.textBrowser.setFont(font1)
        self.pushButton_start_mp = QPushButton(self.centralwidget)
        self.pushButton_start_mp.setObjectName(u"pushButton_start_mp")
        self.pushButton_start_mp.setGeometry(QRect(20, 150, 91, 61))
        self.pushButton_start_mp.setFont(font)
        self.pushButton_start_spec = QPushButton(self.centralwidget)
        self.pushButton_start_spec.setObjectName(u"pushButton_start_spec")
        self.pushButton_start_spec.setGeometry(QRect(130, 150, 91, 61))
        self.pushButton_start_spec.setFont(font)
        self.pushButton_start_bridge = QPushButton(self.centralwidget)
        self.pushButton_start_bridge.setObjectName(u"pushButton_start_bridge")
        self.pushButton_start_bridge.setGeometry(QRect(240, 150, 91, 61))
        self.pushButton_start_bridge.setFont(font)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 220, 331, 21))
        self.label_info = QLabel(self.groupBox_3)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(0, 0, 331, 20))
        self.label_info.setFont(font)
        self.label_info.setAlignment(Qt.AlignCenter)
        self.checkBox_skip_2_4_bridge = QCheckBox(self.centralwidget)
        self.checkBox_skip_2_4_bridge.setObjectName(u"checkBox_skip_2_4_bridge")
        self.checkBox_skip_2_4_bridge.setGeometry(QRect(190, 100, 121, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"7600_TXT_2_EXCEL", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9TXT\u6587\u4ef6\u6240\u5728\u6587\u4ef6\u5939", None))
        self.pushButton_select_path.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u6570\u91cf", None))
        self.pushButton_start_mp.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210MP", None))
        self.pushButton_start_spec.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210SPEC", None))
        self.pushButton_start_bridge.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210Bridge", None))
        self.groupBox_3.setTitle("")
        self.label_info.setText("")
        self.checkBox_skip_2_4_bridge.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc72.4G Bridge", None))
    # retranslateUi

