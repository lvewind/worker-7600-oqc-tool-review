# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog_app_setting(object):
    def setupUi(self, Dialog_app_setting):
        if not Dialog_app_setting.objectName():
            Dialog_app_setting.setObjectName(u"Dialog_app_setting")
        Dialog_app_setting.resize(360, 575)
        Dialog_app_setting.setMinimumSize(QSize(360, 480))
        self.pushButton_cancel = QPushButton(Dialog_app_setting)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(60, 510, 75, 23))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        self.pushButton_cancel.setFont(font)
        self.groupBox_2 = QGroupBox(Dialog_app_setting)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 100, 301, 51))
        self.groupBox_2.setFont(font)
        self.comboBox_wlan_eth = QComboBox(self.groupBox_2)
        self.comboBox_wlan_eth.setObjectName(u"comboBox_wlan_eth")
        self.comboBox_wlan_eth.setGeometry(QRect(10, 20, 281, 22))
        self.comboBox_wlan_eth.setFont(font)
        self.pushButton_save = QPushButton(Dialog_app_setting)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(210, 510, 75, 23))
        self.pushButton_save.setFont(font)
        self.groupBox = QGroupBox(Dialog_app_setting)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 30, 301, 51))
        self.groupBox.setFont(font)
        self.comboBox_lan_eth = QComboBox(self.groupBox)
        self.comboBox_lan_eth.setObjectName(u"comboBox_lan_eth")
        self.comboBox_lan_eth.setGeometry(QRect(10, 20, 281, 22))
        self.comboBox_lan_eth.setFont(font)
        self.groupBox_3 = QGroupBox(Dialog_app_setting)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 170, 301, 51))
        self.groupBox_3.setFont(font)
        self.comboBox_bridge_ctrl_eth = QComboBox(self.groupBox_3)
        self.comboBox_bridge_ctrl_eth.setObjectName(u"comboBox_bridge_ctrl_eth")
        self.comboBox_bridge_ctrl_eth.setGeometry(QRect(10, 20, 281, 22))
        self.comboBox_bridge_ctrl_eth.setFont(font)
        self.checkBox_auto_txt = QCheckBox(Dialog_app_setting)
        self.checkBox_auto_txt.setObjectName(u"checkBox_auto_txt")
        self.checkBox_auto_txt.setGeometry(QRect(40, 410, 161, 21))
        self.checkBox_auto_txt.setFont(font)
        self.checkBox_open_after_txt = QCheckBox(Dialog_app_setting)
        self.checkBox_open_after_txt.setObjectName(u"checkBox_open_after_txt")
        self.checkBox_open_after_txt.setGeometry(QRect(40, 440, 131, 21))
        self.checkBox_open_after_txt.setFont(font)
        self.checkBox_test_speed_after_ui = QCheckBox(Dialog_app_setting)
        self.checkBox_test_speed_after_ui.setObjectName(u"checkBox_test_speed_after_ui")
        self.checkBox_test_speed_after_ui.setGeometry(QRect(40, 380, 161, 21))
        self.checkBox_test_speed_after_ui.setFont(font)
        self.checkBox_auto_set_ip_200 = QCheckBox(Dialog_app_setting)
        self.checkBox_auto_set_ip_200.setObjectName(u"checkBox_auto_set_ip_200")
        self.checkBox_auto_set_ip_200.setGeometry(QRect(40, 470, 241, 21))
        self.checkBox_auto_set_ip_200.setFont(font)
        self.groupBox_4 = QGroupBox(Dialog_app_setting)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 240, 301, 51))
        self.lineEdit_main_ap_ssid = QLineEdit(self.groupBox_4)
        self.lineEdit_main_ap_ssid.setObjectName(u"lineEdit_main_ap_ssid")
        self.lineEdit_main_ap_ssid.setGeometry(QRect(10, 20, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.lineEdit_main_ap_ssid.setFont(font1)
        self.groupBox_5 = QGroupBox(Dialog_app_setting)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 310, 301, 51))
        self.lineEdit_main_ap_passwd = QLineEdit(self.groupBox_5)
        self.lineEdit_main_ap_passwd.setObjectName(u"lineEdit_main_ap_passwd")
        self.lineEdit_main_ap_passwd.setGeometry(QRect(10, 20, 281, 31))
        self.lineEdit_main_ap_passwd.setFont(font1)

        self.retranslateUi(Dialog_app_setting)

        QMetaObject.connectSlotsByName(Dialog_app_setting)
    # setupUi

    def retranslateUi(self, Dialog_app_setting):
        Dialog_app_setting.setWindowTitle(QCoreApplication.translate("Dialog_app_setting", u"\u8bbe\u7f6e", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_app_setting", u"\u53d6\u6d88", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_app_setting", u"\u65e0\u7ebf\u7f51\u5361\u9009\u62e9", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog_app_setting", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_app_setting", u"\u6709\u7ebf\u7f51\u5361\u9009\u62e9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog_app_setting", u"Brideg \u63a7\u5236\u7f51\u5361", None))
        self.checkBox_auto_txt.setText(QCoreApplication.translate("Dialog_app_setting", u"\u4e00\u952e\u4e09\u8fde\u540e\u81ea\u52a8\u751f\u6210TXT", None))
        self.checkBox_open_after_txt.setText(QCoreApplication.translate("Dialog_app_setting", u"\u751f\u6210TXT\u540e\u6253\u5f00\u6587\u4ef6", None))
        self.checkBox_test_speed_after_ui.setText(QCoreApplication.translate("Dialog_app_setting", u"\u7f51\u9875\u68c0\u6d4b\u5b8c\u6210\u540e\u81ea\u52a8\u6d4b\u901f", None))
        self.checkBox_auto_set_ip_200.setText(QCoreApplication.translate("Dialog_app_setting", u"\u6d4b\u8bd5\u5b8c\u6210\u540e\u81ea\u52a8\u8bbe\u7f6eip200(\u65e7\u7248\u672c\u9002\u7528)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_app_setting", u"MAIN AP 5G SSID", None))
        self.lineEdit_main_ap_ssid.setText(QCoreApplication.translate("Dialog_app_setting", u"U+Net5563_5G", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_app_setting", u"MAIN AP 5G PASSWD", None))
        self.lineEdit_main_ap_passwd.setText(QCoreApplication.translate("Dialog_app_setting", u"17@6OU6395", None))
    # retranslateUi

