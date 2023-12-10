from PySide6 import QtWidgets
from app.source.ui.app_setting import Ui_Dialog_app_setting
from app.data.oqc_setting import oqc_setting
import hiworker
from app.app_signal.app_signal import signal_main_ui


class DialogAppSetting(QtWidgets.QDialog, Ui_Dialog_app_setting):
    def __init__(self):
        super(DialogAppSetting, self).__init__()
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_save.clicked.connect(self.save_setting)
        self.pushButton_save.clicked.connect(self.close)

    def save_setting(self):
        lan_eth = self.comboBox_lan_eth.currentText()
        wlan_eth = self.comboBox_wlan_eth.currentText()
        bridge_ctrl_eth = self.comboBox_bridge_ctrl_eth.currentText()
        auto_txt = self.checkBox_auto_txt.isChecked()
        open_after_txt = self.checkBox_open_after_txt.isChecked()
        auto_speed = self.checkBox_test_speed_after_ui.isChecked()
        auto_ip_200 = self.checkBox_auto_set_ip_200.isChecked()

        main_ap_ssid = self.lineEdit_main_ap_ssid.text()
        main_ap_passwd = self.lineEdit_main_ap_passwd.text()

        oqc_setting.set_eth(lan_eth, wlan_eth, bridge_ctrl_eth)
        oqc_setting.set_txt(auto_txt, open_after_txt)
        oqc_setting.set_auto_speed(auto_speed)
        oqc_setting.set_auto_ip_200(auto_ip_200)
        oqc_setting.set_main_ap_ssid(main_ap_ssid)
        oqc_setting.set_main_ap_passwd(main_ap_passwd)
        signal_main_ui.refresh_eth.emit()

    def list_sys_eth(self):
        self.comboBox_lan_eth.clear()
        self.comboBox_wlan_eth.clear()
        self.comboBox_bridge_ctrl_eth.clear()
        eth_name_list = hiworker.get_network_eth_list()
        self.comboBox_lan_eth.addItems(eth_name_list)
        self.comboBox_wlan_eth.addItems(eth_name_list)
        self.comboBox_bridge_ctrl_eth.addItems(eth_name_list)
        current_lan = oqc_setting.get_lan_eth()
        current_wlan = oqc_setting.get_wlan_eth()
        current_bridge_ctrl_eth = oqc_setting.get_bridge_ctrl_eth()
        for i in range(self.comboBox_lan_eth.count()):
            if current_lan == self.comboBox_lan_eth.itemText(i):
                self.comboBox_lan_eth.setCurrentIndex(i)
                break
        for i in range(self.comboBox_wlan_eth.count()):
            if current_wlan == self.comboBox_wlan_eth.itemText(i):
                self.comboBox_wlan_eth.setCurrentIndex(i)
                break
        for i in range(self.comboBox_bridge_ctrl_eth.count()):
            if current_bridge_ctrl_eth == self.comboBox_bridge_ctrl_eth.itemText(i):
                self.comboBox_bridge_ctrl_eth.setCurrentIndex(i)
                break

    def set_ui(self):
        auto_speed = oqc_setting.get_auto_speed()
        open_text = oqc_setting.get_open_text()
        auto_text = oqc_setting.get_auto_text()
        auto_ip_200 = oqc_setting.get_auto_ip_200()
        self.checkBox_test_speed_after_ui.setChecked(True if auto_speed else False)
        self.checkBox_auto_txt.setChecked(True if auto_text else False)
        self.checkBox_open_after_txt.setChecked(True if open_text else False)
        self.checkBox_auto_set_ip_200.setChecked(True if auto_ip_200 else False)

    def show_app_setting(self):
        self.list_sys_eth()
        self.set_ui()
        self.show()
