# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(731, 741)
        MainWindow.setMinimumSize(QSize(731, 741))
        MainWindow.setMaximumSize(QSize(731, 741))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        MainWindow.setFont(font)
        self.action_setting = QAction(MainWindow)
        self.action_setting.setObjectName(u"action_setting")
        self.action_doc_folder = QAction(MainWindow)
        self.action_doc_folder.setObjectName(u"action_doc_folder")
        self.action_txt_to_excel = QAction(MainWindow)
        self.action_txt_to_excel.setObjectName(u"action_txt_to_excel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_operation = QGroupBox(self.centralwidget)
        self.groupBox_operation.setObjectName(u"groupBox_operation")
        self.groupBox_operation.setGeometry(QRect(330, 10, 391, 571))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.groupBox_operation.setFont(font1)
        self.groupBox_operation.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.groupBox_operation)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 170, 391, 401))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.textBrowser.setFont(font2)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)
        self.groupBox_7 = QGroupBox(self.groupBox_operation)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(0, 20, 341, 91))
        self.groupBox_7.setFont(font1)
        self.pushButton_start_test_item = QPushButton(self.groupBox_7)
        self.pushButton_start_test_item.setObjectName(u"pushButton_start_test_item")
        self.pushButton_start_test_item.setGeometry(QRect(0, 0, 41, 91))
        self.pushButton_start_test_item.setFont(font1)
        self.pushButton_check_ui_and_set_wifi = QPushButton(self.groupBox_7)
        self.pushButton_check_ui_and_set_wifi.setObjectName(u"pushButton_check_ui_and_set_wifi")
        self.pushButton_check_ui_and_set_wifi.setGeometry(QRect(50, 0, 41, 41))
        self.pushButton_check_ui_and_set_wifi.setMinimumSize(QSize(31, 0))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(9)
        font3.setBold(False)
        self.pushButton_check_ui_and_set_wifi.setFont(font3)
        self.pushButton_iperf_1 = QPushButton(self.groupBox_7)
        self.pushButton_iperf_1.setObjectName(u"pushButton_iperf_1")
        self.pushButton_iperf_1.setGeometry(QRect(200, 0, 41, 41))
        self.pushButton_iperf_1.setMinimumSize(QSize(31, 0))
        self.pushButton_iperf_1.setFont(font3)
        self.pushButton_iperf_24 = QPushButton(self.groupBox_7)
        self.pushButton_iperf_24.setObjectName(u"pushButton_iperf_24")
        self.pushButton_iperf_24.setGeometry(QRect(250, 0, 41, 41))
        self.pushButton_iperf_24.setMinimumSize(QSize(31, 0))
        self.pushButton_iperf_24.setFont(font3)
        self.pushButton_iperf_5 = QPushButton(self.groupBox_7)
        self.pushButton_iperf_5.setObjectName(u"pushButton_iperf_5")
        self.pushButton_iperf_5.setGeometry(QRect(300, 0, 41, 41))
        self.pushButton_iperf_5.setMinimumSize(QSize(31, 0))
        self.pushButton_iperf_5.setFont(font3)
        self.pushButton_stop = QPushButton(self.groupBox_7)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(200, 50, 41, 41))
        self.pushButton_stop.setMinimumSize(QSize(31, 0))
        self.pushButton_stop.setFont(font3)
        self.pushButton_connect_lan_dhcp = QPushButton(self.groupBox_7)
        self.pushButton_connect_lan_dhcp.setObjectName(u"pushButton_connect_lan_dhcp")
        self.pushButton_connect_lan_dhcp.setGeometry(QRect(50, 50, 41, 41))
        self.pushButton_connect_lan_dhcp.setMinimumSize(QSize(31, 0))
        self.pushButton_connect_lan_dhcp.setFont(font3)
        self.pushButton_iperf_one_key = QPushButton(self.groupBox_7)
        self.pushButton_iperf_one_key.setObjectName(u"pushButton_iperf_one_key")
        self.pushButton_iperf_one_key.setGeometry(QRect(150, 0, 41, 41))
        self.pushButton_iperf_one_key.setMinimumSize(QSize(31, 0))
        self.pushButton_iperf_one_key.setFont(font1)
        self.pushButton_output_current = QPushButton(self.groupBox_7)
        self.pushButton_output_current.setObjectName(u"pushButton_output_current")
        self.pushButton_output_current.setGeometry(QRect(300, 50, 41, 41))
        self.pushButton_output_current.setMinimumSize(QSize(31, 0))
        self.pushButton_output_current.setFont(font3)
        self.pushButton_clear_wifi = QPushButton(self.groupBox_7)
        self.pushButton_clear_wifi.setObjectName(u"pushButton_clear_wifi")
        self.pushButton_clear_wifi.setGeometry(QRect(100, 50, 41, 41))
        self.pushButton_clear_wifi.setMinimumSize(QSize(31, 0))
        self.pushButton_clear_wifi.setFont(font3)
        self.pushButton_disconnect_lan = QPushButton(self.groupBox_7)
        self.pushButton_disconnect_lan.setObjectName(u"pushButton_disconnect_lan")
        self.pushButton_disconnect_lan.setGeometry(QRect(150, 50, 41, 41))
        self.pushButton_disconnect_lan.setMinimumSize(QSize(31, 0))
        self.pushButton_disconnect_lan.setFont(font3)
        self.pushButton_one_key = QPushButton(self.groupBox_7)
        self.pushButton_one_key.setObjectName(u"pushButton_one_key")
        self.pushButton_one_key.setGeometry(QRect(250, 50, 41, 41))
        self.pushButton_one_key.setMinimumSize(QSize(31, 0))
        self.pushButton_one_key.setFont(font3)
        self.pushButton_auto_one_key = QPushButton(self.groupBox_7)
        self.pushButton_auto_one_key.setObjectName(u"pushButton_auto_one_key")
        self.pushButton_auto_one_key.setGeometry(QRect(100, 0, 41, 41))
        self.pushButton_auto_one_key.setMinimumSize(QSize(31, 0))
        self.pushButton_auto_one_key.setFont(font3)
        self.groupBox_10 = QGroupBox(self.groupBox_operation)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(100, 120, 291, 41))
        self.pushButton_config_bridge = QPushButton(self.groupBox_10)
        self.pushButton_config_bridge.setObjectName(u"pushButton_config_bridge")
        self.pushButton_config_bridge.setGeometry(QRect(50, 0, 41, 41))
        self.pushButton_config_bridge.setMinimumSize(QSize(31, 0))
        self.pushButton_config_bridge.setFont(font3)
        self.pushButton_libre_speedtest = QPushButton(self.groupBox_10)
        self.pushButton_libre_speedtest.setObjectName(u"pushButton_libre_speedtest")
        self.pushButton_libre_speedtest.setGeometry(QRect(100, 0, 41, 41))
        self.pushButton_libre_speedtest.setMinimumSize(QSize(31, 0))
        self.pushButton_libre_speedtest.setFont(font3)
        self.pushButton_output_current_bridge = QPushButton(self.groupBox_10)
        self.pushButton_output_current_bridge.setObjectName(u"pushButton_output_current_bridge")
        self.pushButton_output_current_bridge.setGeometry(QRect(200, 0, 41, 41))
        self.pushButton_output_current_bridge.setMinimumSize(QSize(31, 0))
        self.pushButton_output_current_bridge.setFont(font3)
        self.pushButton_bridge_input = QPushButton(self.groupBox_10)
        self.pushButton_bridge_input.setObjectName(u"pushButton_bridge_input")
        self.pushButton_bridge_input.setGeometry(QRect(150, 0, 41, 41))
        self.pushButton_bridge_input.setFont(font3)
        self.pushButton_reconnect_bridge = QPushButton(self.groupBox_10)
        self.pushButton_reconnect_bridge.setObjectName(u"pushButton_reconnect_bridge")
        self.pushButton_reconnect_bridge.setGeometry(QRect(250, 0, 41, 41))
        self.pushButton_reconnect_bridge.setMinimumSize(QSize(31, 0))
        self.pushButton_reconnect_bridge.setFont(font3)
        self.pushButton_onekey_bridge = QPushButton(self.groupBox_10)
        self.pushButton_onekey_bridge.setObjectName(u"pushButton_onekey_bridge")
        self.pushButton_onekey_bridge.setGeometry(QRect(0, 0, 41, 41))
        self.pushButton_onekey_bridge.setMinimumSize(QSize(31, 0))
        self.pushButton_onekey_bridge.setFont(font1)
        self.groupBox_3 = QGroupBox(self.groupBox_operation)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 120, 91, 41))
        self.groupBox_3.setFont(font3)
        self.lineEdit_v = QLineEdit(self.groupBox_3)
        self.lineEdit_v.setObjectName(u"lineEdit_v")
        self.lineEdit_v.setGeometry(QRect(0, 0, 41, 21))
        self.lineEdit_v.setFont(font1)
        self.lineEdit_a = QLineEdit(self.groupBox_3)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setGeometry(QRect(0, 20, 41, 21))
        self.lineEdit_a.setFont(font3)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(38, 0, 16, 21))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(38, 20, 16, 21))
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButton_input_usb_power = QPushButton(self.groupBox_3)
        self.pushButton_input_usb_power.setObjectName(u"pushButton_input_usb_power")
        self.pushButton_input_usb_power.setGeometry(QRect(50, 0, 41, 41))
        self.pushButton_input_usb_power.setFont(font3)
        self.groupBox_11 = QGroupBox(self.groupBox_operation)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(350, 20, 41, 91))
        self.checkBox_is_test_bridge = QCheckBox(self.groupBox_11)
        self.checkBox_is_test_bridge.setObjectName(u"checkBox_is_test_bridge")
        self.checkBox_is_test_bridge.setGeometry(QRect(15, 70, 20, 21))
        self.label = QLabel(self.groupBox_11)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 0, 21, 71))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 311, 571))
        self.groupBox.setFont(font3)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tableWidget_products_list = QTableWidget(self.groupBox)
        if (self.tableWidget_products_list.columnCount() < 5):
            self.tableWidget_products_list.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_products_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_products_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_products_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_products_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_products_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_products_list.setObjectName(u"tableWidget_products_list")
        self.tableWidget_products_list.setGeometry(QRect(0, 140, 311, 431))
        self.tableWidget_products_list.setFont(font2)
        self.tableWidget_products_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_products_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_products_list.setAutoScroll(True)
        self.tableWidget_products_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_products_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_products_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_products_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_products_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_products_list.horizontalHeader().setVisible(True)
        self.tableWidget_products_list.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_products_list.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_products_list.verticalHeader().setVisible(False)
        self.tableWidget_products_list.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_products_list.verticalHeader().setDefaultSectionSize(18)
        self.pushButton_filter = QPushButton(self.groupBox)
        self.pushButton_filter.setObjectName(u"pushButton_filter")
        self.pushButton_filter.setGeometry(QRect(270, 110, 41, 21))
        self.pushButton_filter.setFont(font3)
        self.pushButton_add_test_item = QPushButton(self.groupBox)
        self.pushButton_add_test_item.setObjectName(u"pushButton_add_test_item")
        self.pushButton_add_test_item.setGeometry(QRect(270, 60, 41, 41))
        self.pushButton_add_test_item.setFont(font1)
        self.pushButton_edit_test_item = QPushButton(self.groupBox)
        self.pushButton_edit_test_item.setObjectName(u"pushButton_edit_test_item")
        self.pushButton_edit_test_item.setGeometry(QRect(270, 30, 41, 21))
        self.pushButton_edit_test_item.setFont(font3)
        self.dateEdit_1 = QDateEdit(self.groupBox)
        self.dateEdit_1.setObjectName(u"dateEdit_1")
        self.dateEdit_1.setGeometry(QRect(0, 110, 151, 22))
        self.dateEdit_1.setFont(font3)
        self.dateEdit_1.setKeyboardTracking(False)
        self.dateEdit_1.setDateTime(QDateTime(QDate(2021, 12, 12), QTime(0, 0, 0)))
        self.dateEdit_2 = QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(160, 110, 101, 22))
        self.dateEdit_2.setFont(font3)
        self.dateEdit_2.setKeyboardTracking(False)
        self.dateEdit_2.setDateTime(QDateTime(QDate(2021, 12, 22), QTime(0, 0, 0)))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 20, 151, 36))
        self.groupBox_2.setFont(font3)
        self.lineEdit_input_serial_number = QLineEdit(self.groupBox_2)
        self.lineEdit_input_serial_number.setObjectName(u"lineEdit_input_serial_number")
        self.lineEdit_input_serial_number.setGeometry(QRect(0, 15, 151, 20))
        self.lineEdit_input_serial_number.setFont(font3)
        self.lineEdit_input_serial_number.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_input_serial_number.setMaxLength(17)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 60, 151, 36))
        self.groupBox_4.setFont(font3)
        self.lineEdit_input_mac = QLineEdit(self.groupBox_4)
        self.lineEdit_input_mac.setObjectName(u"lineEdit_input_mac")
        self.lineEdit_input_mac.setGeometry(QRect(0, 15, 151, 20))
        self.lineEdit_input_mac.setFont(font3)
        self.lineEdit_input_mac.setMaxLength(17)
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(160, 20, 101, 36))
        self.groupBox_5.setFont(font3)
        self.lineEdit_input_web_manage_password = QLineEdit(self.groupBox_5)
        self.lineEdit_input_web_manage_password.setObjectName(u"lineEdit_input_web_manage_password")
        self.lineEdit_input_web_manage_password.setGeometry(QRect(0, 15, 101, 20))
        self.lineEdit_input_web_manage_password.setFont(font3)
        self.lineEdit_input_web_manage_password.setMaxLength(10)
        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(160, 60, 101, 36))
        self.groupBox_6.setFont(font3)
        self.lineEdit_input_wifi_password = QLineEdit(self.groupBox_6)
        self.lineEdit_input_wifi_password.setObjectName(u"lineEdit_input_wifi_password")
        self.lineEdit_input_wifi_password.setGeometry(QRect(0, 15, 101, 20))
        self.lineEdit_input_wifi_password.setFont(font3)
        self.lineEdit_input_wifi_password.setMaxLength(10)
        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 590, 351, 101))
        self.groupBox_8.setFont(font3)
        self.textBrowser_ping_100 = QTextBrowser(self.groupBox_8)
        self.textBrowser_ping_100.setObjectName(u"textBrowser_ping_100")
        self.textBrowser_ping_100.setGeometry(QRect(0, 20, 351, 81))
        self.textBrowser_ping_100.setFont(font2)
        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(370, 590, 351, 101))
        self.groupBox_9.setFont(font3)
        self.textBrowser_ping_254 = QTextBrowser(self.groupBox_9)
        self.textBrowser_ping_254.setObjectName(u"textBrowser_ping_254")
        self.textBrowser_ping_254.setGeometry(QRect(0, 20, 351, 81))
        self.textBrowser_ping_254.setFont(font2)
        self.pushButton_check_log = QPushButton(self.centralwidget)
        self.pushButton_check_log.setObjectName(u"pushButton_check_log")
        self.pushButton_check_log.setGeometry(QRect(800, 30, 41, 41))
        self.pushButton_check_log.setMinimumSize(QSize(31, 0))
        self.pushButton_check_log.setFont(font3)
        self.pushButton_sw_reset = QPushButton(self.centralwidget)
        self.pushButton_sw_reset.setObjectName(u"pushButton_sw_reset")
        self.pushButton_sw_reset.setGeometry(QRect(750, 80, 41, 41))
        self.pushButton_sw_reset.setMinimumSize(QSize(31, 0))
        self.pushButton_sw_reset.setFont(font3)
        self.pushButton_start_test_item_bridge = QPushButton(self.centralwidget)
        self.pushButton_start_test_item_bridge.setObjectName(u"pushButton_start_test_item_bridge")
        self.pushButton_start_test_item_bridge.setGeometry(QRect(750, 180, 91, 41))
        self.pushButton_start_test_item_bridge.setFont(font1)
        self.pushButton_open_bridge = QPushButton(self.centralwidget)
        self.pushButton_open_bridge.setObjectName(u"pushButton_open_bridge")
        self.pushButton_open_bridge.setGeometry(QRect(750, 130, 41, 41))
        self.pushButton_open_bridge.setMinimumSize(QSize(31, 0))
        self.pushButton_open_bridge.setFont(font3)
        self.pushButton_open_web_ui = QPushButton(self.centralwidget)
        self.pushButton_open_web_ui.setObjectName(u"pushButton_open_web_ui")
        self.pushButton_open_web_ui.setGeometry(QRect(750, 30, 41, 41))
        self.pushButton_open_web_ui.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 731, 23))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.lineEdit_input_serial_number, self.lineEdit_input_mac)
        QWidget.setTabOrder(self.lineEdit_input_mac, self.lineEdit_input_web_manage_password)
        QWidget.setTabOrder(self.lineEdit_input_web_manage_password, self.lineEdit_input_wifi_password)
        QWidget.setTabOrder(self.lineEdit_input_wifi_password, self.pushButton_edit_test_item)
        QWidget.setTabOrder(self.pushButton_edit_test_item, self.pushButton_add_test_item)
        QWidget.setTabOrder(self.pushButton_add_test_item, self.dateEdit_1)
        QWidget.setTabOrder(self.dateEdit_1, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.pushButton_filter)
        QWidget.setTabOrder(self.pushButton_filter, self.pushButton_start_test_item)
        QWidget.setTabOrder(self.pushButton_start_test_item, self.pushButton_check_ui_and_set_wifi)
        QWidget.setTabOrder(self.pushButton_check_ui_and_set_wifi, self.pushButton_connect_lan_dhcp)
        QWidget.setTabOrder(self.pushButton_connect_lan_dhcp, self.pushButton_open_web_ui)
        QWidget.setTabOrder(self.pushButton_open_web_ui, self.pushButton_clear_wifi)
        QWidget.setTabOrder(self.pushButton_clear_wifi, self.pushButton_check_log)
        QWidget.setTabOrder(self.pushButton_check_log, self.pushButton_sw_reset)
        QWidget.setTabOrder(self.pushButton_sw_reset, self.pushButton_disconnect_lan)
        QWidget.setTabOrder(self.pushButton_disconnect_lan, self.pushButton_output_current)
        QWidget.setTabOrder(self.pushButton_output_current, self.pushButton_one_key)
        QWidget.setTabOrder(self.pushButton_one_key, self.pushButton_iperf_one_key)
        QWidget.setTabOrder(self.pushButton_iperf_one_key, self.pushButton_iperf_1)
        QWidget.setTabOrder(self.pushButton_iperf_1, self.pushButton_iperf_24)
        QWidget.setTabOrder(self.pushButton_iperf_24, self.pushButton_iperf_5)
        QWidget.setTabOrder(self.pushButton_iperf_5, self.pushButton_stop)
        QWidget.setTabOrder(self.pushButton_stop, self.pushButton_config_bridge)
        QWidget.setTabOrder(self.pushButton_config_bridge, self.pushButton_libre_speedtest)
        QWidget.setTabOrder(self.pushButton_libre_speedtest, self.pushButton_open_bridge)
        QWidget.setTabOrder(self.pushButton_open_bridge, self.lineEdit_v)
        QWidget.setTabOrder(self.lineEdit_v, self.lineEdit_a)
        QWidget.setTabOrder(self.lineEdit_a, self.pushButton_input_usb_power)
        QWidget.setTabOrder(self.pushButton_input_usb_power, self.tableWidget_products_list)
        QWidget.setTabOrder(self.tableWidget_products_list, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.textBrowser_ping_100)
        QWidget.setTabOrder(self.textBrowser_ping_100, self.textBrowser_ping_254)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_setting)
        self.menu.addAction(self.action_doc_folder)
        self.menu.addAction(self.action_txt_to_excel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LGU+7600_OQC_by_lvewind", None))
        self.action_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_doc_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00TXT\u6570\u636e\u76ee\u5f55", None))
        self.action_txt_to_excel.setText(QCoreApplication.translate("MainWindow", u"TXT TO EXCEL", None))
        self.groupBox_operation.setTitle(QCoreApplication.translate("MainWindow", u"Current Item\uff1a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u7b49\u7ebf','\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>", None))
        self.groupBox_7.setTitle("")
        self.pushButton_start_test_item.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\n"
"\u6d4b\u8bd5", None))
        self.pushButton_check_ui_and_set_wifi.setText(QCoreApplication.translate("MainWindow", u"UI \n"
"WIFI", None))
        self.pushButton_iperf_1.setText(QCoreApplication.translate("MainWindow", u"iperf\n"
"LAN", None))
        self.pushButton_iperf_24.setText(QCoreApplication.translate("MainWindow", u"iperf\n"
"2.4G", None))
        self.pushButton_iperf_5.setText(QCoreApplication.translate("MainWindow", u"iperf\n"
"5G", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\n"
"\u6d4b\u901f", None))
        self.pushButton_connect_lan_dhcp.setText(QCoreApplication.translate("MainWindow", u"DHCP", None))
        self.pushButton_iperf_one_key.setText(QCoreApplication.translate("MainWindow", u"iperf\n"
"ALL", None))
        self.pushButton_output_current.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\n"
"\u5f53\u524d", None))
        self.pushButton_clear_wifi.setText(QCoreApplication.translate("MainWindow", u"WPS", None))
        self.pushButton_disconnect_lan.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\n"
"LAN", None))
        self.pushButton_one_key.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u9664\n"
"\u5f53\u524d", None))
        self.pushButton_auto_one_key.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\n"
"\u68c0\u6d4b", None))
        self.groupBox_10.setTitle("")
        self.pushButton_config_bridge.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\n"
"\u6865\u63a5", None))
        self.pushButton_libre_speedtest.setText(QCoreApplication.translate("MainWindow", u"\u6865\u63a5\n"
"\u6d4b\u901f", None))
        self.pushButton_output_current_bridge.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\n"
"\u6865\u63a5", None))
        self.pushButton_bridge_input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\n"
"\u6570\u636e", None))
        self.pushButton_reconnect_bridge.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u8fde\n"
"\u6865\u63a5", None))
        self.pushButton_onekey_bridge.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\n"
"\u6865\u63a5", None))
        self.groupBox_3.setTitle("")
        self.lineEdit_v.setText("")
        self.lineEdit_a.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A", None))
#if QT_CONFIG(statustip)
        self.pushButton_input_usb_power.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_input_usb_power.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_input_usb_power.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox_11.setTitle("")
        self.checkBox_is_test_bridge.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u68c0\n"
"\u6d4b\n"
"\u6865\n"
"\u63a5", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u5217\u8868", None))
        ___qtablewidgetitem = self.tableWidget_products_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem1 = self.tableWidget_products_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"S/N", None));
        ___qtablewidgetitem2 = self.tableWidget_products_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"MAC", None));
        ___qtablewidgetitem3 = self.tableWidget_products_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"USB", None));
        ___qtablewidgetitem4 = self.tableWidget_products_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"IoT", None));
        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.pushButton_add_test_item.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_edit_test_item.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.dateEdit_1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"S/N", None))
        self.lineEdit_input_serial_number.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.lineEdit_input_mac.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Web_Passwd", None))
        self.lineEdit_input_web_manage_password.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Wifi_Passwd", None))
        self.lineEdit_input_wifi_password.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Ping 192.168.0.100", None))
        self.textBrowser_ping_100.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u7b49\u7ebf','\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1'; font-weight:400;\"><br /></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Ping 192.168.123.254", None))
        self.textBrowser_ping_254.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u7b49\u7ebf','\u5fae\u8f6f\u96c5\u9ed1','\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_check_log.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\n"
"\u65e5\u5fd7", None))
        self.pushButton_sw_reset.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\n"
"ip200", None))
        self.pushButton_start_test_item_bridge.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5\u6865\u63a5", None))
        self.pushButton_open_bridge.setText(QCoreApplication.translate("MainWindow", u"\u6865\u63a5\n"
"\u9875\u9762", None))
        self.pushButton_open_web_ui.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\n"
"\u9875\u9762", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

