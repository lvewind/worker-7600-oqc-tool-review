from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCursor
from threading import Thread
import os
import time
import hiworker
import copy
from app import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.current_testing = False
        self.has_output = True
        self.dialog_app_setting = DialogAppSetting()
        self.dialog_save_usb_power = DialogSaveUSBPower()
        self.dialog_bridge_input = DialogBridgeSpeedTestSave()
        self.dialog_show_message = DialogShowMessage()
        self.init_data_edit()
        self.init_table_products_list()
        self.load_table_products_list()

        self.current_testing_sn = ""
        self.current_product = {}

        self.product_menu = ProductsListMenu()
        self.old_sn = ""
        self.lan_eth = ""
        self.wlan_eth = ""
        self.bridge_ctrl_eth = ""
        self.bridge_ip = ""
        self.get_eth()
        self.txt_to_excel = GAPK7600Txt2Excel()
        self.lgu_7600 = LGU7600Driver()

        self.ping_100 = Thread(target=ping_server, args=("192.168.0.100",), daemon=True)
        self.ping_100.start()
        self.ping_254 = Thread(target=ping_server, args=("192.168.123.254",), daemon=True)
        self.ping_254.start()
        self.connect_wifi = ConnectWifi()
        self.iperf3 = Iperf()
        self.libre_speed_test = LibreSpeedTest()
        self.bind_function()
        self.bind_signal()

    def show(self) -> None:
        super().show()
        stime = hiworker.get_web_server_time("www.baidu.com")

    def bind_function(self):
        """
        绑定按键
        :return:
        """

        self.action_setting.triggered.connect(self.dialog_app_setting.show_app_setting)
        self.action_doc_folder.triggered.connect(self.open_doc_folder)
        self.action_txt_to_excel.triggered.connect(self.show_txt_to_excel)

        self.pushButton_filter.clicked.connect(self.filter_table_products_list)

        self.pushButton_add_test_item.clicked.connect(self.add_product)
        self.pushButton_edit_test_item.clicked.connect(self.edit_product)
        self.pushButton_start_test_item.clicked.connect(self.set_current_product)
        self.pushButton_open_web_ui.clicked.connect(self.open_web_page)
        self.pushButton_config_bridge.clicked.connect(self.config_bridge_page)
        self.pushButton_open_bridge.clicked.connect(self.open_bridge_page)
        self.pushButton_check_ui_and_set_wifi.clicked.connect(self.check_web_ui_and_set_wifi)
        self.pushButton_one_key.clicked.connect(self.one_key_ui_iperf)
        self.pushButton_check_log.clicked.connect(self.check_web_log)
        self.pushButton_input_usb_power.clicked.connect(self.save_usb_power)
        self.pushButton_disconnect_lan.clicked.connect(self.disable_lan)
        self.pushButton_connect_lan_dhcp.clicked.connect(self.set_dhcp)

        self.pushButton_iperf_1.clicked.connect(self.iperf_lan_1g)
        self.pushButton_iperf_5.clicked.connect(self.iperf_wifi_5g)
        self.pushButton_iperf_24.clicked.connect(self.iperf_wifi_2g)

        self.pushButton_iperf_one_key.clicked.connect(self.iperf_all)

        self.pushButton_stop.clicked.connect(self.stop_iperf)
        self.pushButton_sw_reset.clicked.connect(self.set_sw_rest)
        self.pushButton_clear_wifi.clicked.connect(self.connect_wifi.delete_all_profile)
        self.pushButton_output_current.clicked.connect(self.output_current_item)

        self.lineEdit_input_serial_number.returnPressed.connect(self.lineEdit_input_mac.setFocus)
        self.lineEdit_input_serial_number.returnPressed.connect(self.lineEdit_input_mac.selectAll)
        self.lineEdit_input_mac.returnPressed.connect(self.lineEdit_input_web_manage_password.setFocus)
        self.lineEdit_input_mac.returnPressed.connect(self.lineEdit_input_web_manage_password.selectAll)
        self.lineEdit_input_web_manage_password.returnPressed.connect(self.lineEdit_input_wifi_password.setFocus)
        self.lineEdit_input_web_manage_password.returnPressed.connect(self.lineEdit_input_wifi_password.selectAll)
        self.lineEdit_input_wifi_password.returnPressed.connect(self.add_product)

        self.lineEdit_v.returnPressed.connect(self.lineEdit_a.setFocus)
        self.lineEdit_v.returnPressed.connect(self.lineEdit_a.selectAll)
        self.lineEdit_a.returnPressed.connect(self.lineEdit_v.setFocus)
        self.lineEdit_a.returnPressed.connect(self.lineEdit_v.selectAll)

        self.tableWidget_products_list.doubleClicked.connect(self.preview_product)

        self.product_menu.delete_product.triggered.connect(self.del_product)
        self.product_menu.save_usb_power.triggered.connect(self.show_usb_power_dialog)
        self.product_menu.output_txt.triggered.connect(self.output_txt)
        self.product_menu.open_txt.triggered.connect(self.open_txt_in_list)
        self.product_menu.open_txt_bridge.triggered.connect(self.open_txt_in_list_bridge)
        self.product_menu.output_txt_bridge.triggered.connect(self.output_txt_bridge)
        self.tableWidget_products_list.customContextMenuRequested.connect(self.show_product_list_menu)
        self.pushButton_one_key.clicked.connect(self.cancel_current_item)
        self.pushButton_bridge_input.clicked.connect(self.show_bridge_save_dialog)
        self.pushButton_output_current_bridge.clicked.connect(self.output_current_item_bridge)
        self.pushButton_libre_speedtest.clicked.connect(self.speed_test_bridge)
        self.pushButton_reconnect_bridge.clicked.connect(self.reconnect_bridge)
        self.pushButton_onekey_bridge.clicked.connect(self.one_key_bridge)

    def bind_signal(self):
        """
        绑定信号
        :return:
        """
        signal_load_table.load_products_list.connect(self.load_table_products_list)
        signal_load_table.find_sn_in_products_list.connect(self.find_product)
        signal_main_ui.refresh_text_browser.connect(self.refresh_text_browser)
        signal_main_ui.refresh_text_browser_ping_100.connect(self.refresh_text_browser_ping_100)
        signal_main_ui.refresh_text_browser_ping_254.connect(self.refresh_text_browser_ping_254)
        signal_main_ui.refresh_eth.connect(self.get_eth)
        signal_main_ui.run_iperf3.connect(self.run_iperf)
        signal_main_ui.set_has_output.connect(self.set_has_output)
        signal_main_ui.check_iot_again.connect(self.lgu_7600.check_iot)
        signal_main_ui.iperf_all.connect(self.iperf_all)
        signal_main_ui.show_input_dialog.connect(self.show_bridge_save_dialog)
        signal_main_ui.save_bridge_ip.connect(self.save_bridge_ip)

    def init_data_edit(self):
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def init_table_products_list(self):
        """
        初始化检测项列表
        :return:
        """
        hiworker.TableLoad.init_table_header(self.tableWidget_products_list, table_header.products_list)

    def refresh_text_browser(self, text):
        """
        刷新信息窗口
        :param text:
        :return:
        """
        self.textBrowser.append(text)

    def refresh_text_browser_ping_100(self, text):
        """
        刷新信息窗口
        :param text:
        :return:
        """
        self.textBrowser_ping_100.append(text)

    def refresh_text_browser_ping_254(self, text):
        """
        刷新信息窗口
        :param text:
        :return:
        """
        self.textBrowser_ping_254.append(text)

    """
    数据处理部分
    """
    def add_product(self):
        """
        添加产品
        :return:
        """
        product_dict = self.get_form_product_dict()
        if not product_dict.get("sn"):
            self.dialog_show_message.show_message("添加失败：SN不能为空")
            return 0
        if not product_dict.get("mac_addr"):
            self.dialog_show_message.show_message("添加失败：MAC不能为空")
            return 0
        if not len(product_dict.get("sn")) == 17:
            self.dialog_show_message.show_message("添加失败：SN 长度不正确")
            return 0
        if not len(product_dict.get("mac_addr")) == 14:
            self.dialog_show_message.show_message("添加失败：MAC地址错误")
            return 0
        if len(product_dict.get("web_passwd")) and not len(product_dict.get("web_passwd")) == 10:
            self.dialog_show_message.show_message("添加失败：登录密码长度错误")
            return 0
        if product_dict.get("wifi_passwd") and not len(product_dict.get("wifi_passwd")) == 10:
            self.dialog_show_message.show_message("添加失败：WIFI密码长度错误")
            return 0

        # 字符串转大写
        for key, value in product_dict.items():
            if value and type(value) == str:
                product_dict[key] = product_dict[key].upper()

        success = oqc_products_list.add_product(product_dict)
        if success:
            self.dialog_show_message.show_message("ADD Successful ！")
            self.clear_form()

            self.load_table_products_list()
            self.find_product(sn_need_find=product_dict.get("sn"))
            oqc_result.update_row({"sn":  product_dict.get("sn"),
                                   "web_passwd": product_dict.get("web_passwd"),
                                   "wifi_passwd": product_dict.get("wifi_passwd"),
                                   "create_time": int(time.time())},
                                  "sn", product_dict.get("sn"))
        else:
            self.dialog_show_message.show_message("ADD Failed！Error：" + str(success))

    def preview_product(self):
        select_sn = hiworker.TableRead.get_current_row_col_data(self.tableWidget_products_list, 1)
        self.old_sn = str(select_sn)
        select_product = oqc_products_list.read_row("sn", select_sn)
        self.lineEdit_input_serial_number.setText(select_product.get("sn"))
        self.lineEdit_input_mac.setText(select_product.get("mac_addr"))
        self.lineEdit_input_web_manage_password.setText(select_product.get("web_passwd"))
        self.lineEdit_input_wifi_password.setText(select_product.get("wifi_passwd"))

        self.lineEdit_input_serial_number.setFocus()
        self.lineEdit_input_serial_number.selectAll()

    def clear_form(self):
        """
        清空产品输入控件
        :return:
        """
        self.lineEdit_input_serial_number.clear()
        self.lineEdit_input_mac.clear()
        self.lineEdit_input_web_manage_password.clear()
        self.lineEdit_input_wifi_password.clear()
        self.lineEdit_input_serial_number.setFocus()

    def del_product(self):
        """
        删除产品
        :return:
        """
        sn_list = self.get_current_selected_sn()
        if sn_list:
            for sn in sn_list:
                data.oqc_products_list.del_product('sn', str(sn))
            self.load_table_products_list()

    def edit_product(self):
        """
        修改产品
        :return:
        """
        product_dict = self.get_form_product_dict()
        if not product_dict.get("sn") or not product_dict.get("mac_addr"):
            self.label_product_add_tip.setText("编辑失败：SN 或者 MAC 不能为空")
            return 0
        if not len(product_dict.get("sn")) == 17:
            self.label_product_add_tip.setText("编辑失败：SN 长度不正确")
            return 0
        if not len(product_dict.get("mac_addr")) == 14:
            self.label_product_add_tip.setText("编辑失败：MAC地址错误")
            return 0
        if len(product_dict.get("web_passwd")) and not len(product_dict.get("web_passwd")) == 10:
            self.label_product_add_tip.setText("编辑失败：登陆密码长度错误")
            return 0
        if product_dict.get("wifi_passwd") and not len(product_dict.get("wifi_passwd")) == 10:
            self.label_product_add_tip.setText("编辑失败：WIFI密码长度错误")
            return 0

        for key, value in product_dict.items():
            if value and type(value) == str:
                product_dict[key] = product_dict[key].upper()
        success = oqc_products_list.edit_product(product_dict, "sn", self.old_sn)
        if success:
            self.dialog_show_message.show_message("编辑成功！")
            self.clear_form()
            self.load_table_products_list()
            if product_dict.get("sn") == self.current_testing_sn:
                self.current_product = oqc_products_list.read_row("sn", self.current_testing_sn)
                self.lgu_7600.set_product(product_dict)

        else:
            self.dialog_show_message.show_message("编辑失败!")

    def get_form_product_dict(self):
        product_dict = {
            'sn': self.lineEdit_input_serial_number.text(),
            'mac_addr': self.lineEdit_input_mac.text(),
            'web_passwd': self.lineEdit_input_web_manage_password.text(),
            'wifi_passwd': self.lineEdit_input_wifi_password.text(),
            'create_time': int(time.time())
        }
        return product_dict

    def find_product(self, sn_need_find=""):
        """
        查找产品
        :return:
        """
        if not sn_need_find:
            target_sn = self.lineEdit_input_serial_number.text()
        else:
            target_sn = sn_need_find
        row_count = self.tableWidget_products_list.rowCount()
        for row in range(row_count):
            sn = self.tableWidget_products_list.item(row, 1).text()
            if target_sn == sn:
                self.tableWidget_products_list.selectRow(row)
                break

    def get_current_selected_sn(self):
        sn_list = []
        rows = hiworker.table_widget.TableRead.get_current_selected_rows(self.tableWidget_products_list)
        if len(rows) > 0:
            for row in rows:
                sn = self.tableWidget_products_list.item(row, 1).text()
                sn_list.append(sn)
        return sn_list

    def set_current_product(self):
        """
        设置当前检测项目
        :return:
        """
        if self.current_testing:
            signal_main_ui.refresh_text_browser.emit("请完成（导出）当前项目后再开始新项目")
            return
        self.textBrowser.clear()
        self.groupBox_operation.setTitle("当前项：")
        self.current_testing_sn = ""
        self.current_product = {}
        sn_list = self.get_current_selected_sn()
        if len(sn_list) > 1:
            signal_main_ui.refresh_text_browser.emit("请选择单个项目进行测试")
            return 0
        elif len(sn_list) <= 0:
            signal_main_ui.refresh_text_browser.emit("当前没有选中的列表项")
            return 0
        else:
            self.current_testing_sn = sn_list[0]
            if self.current_testing_sn:
                self.current_product = oqc_products_list.read_row("sn", self.current_testing_sn)
                mac = self.current_product.get("mac_addr")
                current_sn_before = self.current_testing_sn[0: -4]
                current_sn_behind = self.current_testing_sn[-4: len(self.current_testing_sn)]
                self.groupBox_operation.setTitle("当前项" + current_sn_before + " " + current_sn_behind + " : " + mac)
                signal_main_ui.refresh_text_browser.emit(self.current_testing_sn + "<>" + mac)
                signal_main_ui.refresh_text_browser.emit("-----------------------------------------")

                self.lgu_7600.set_product(self.current_product)
                self.current_testing = True
                if not self.checkBox_is_test_bridge.isChecked():
                    Thread(target=set_adapter_dhcp, args=(self.lan_eth, self.wlan_eth, False)).start()
            else:
                signal_main_ui.refresh_text_browser.emit("当前SN丢失，请检查对应项目")

    def view_product_result(self):
        """
        查看检测结果
        :return:
        """
        pass

    def filter_table_products_list(self):
        target_time_start = self.dateEdit_1.dateTime().currentSecsSinceEpoch()
        target_time_end = self.dateEdit_2.dateTime().currentSecsSinceEpoch() + 86400
        self.load_table_products_list(target_time_1=target_time_start, target_time_2=target_time_end)

    def load_table_products_list(self, target_time_1=None, target_time_2=None):
        """
        加载检测列表数据
        :return:
        """
        if target_time_1 and target_time_2:
            day_start = target_time_1
            day_end = target_time_2
        else:
            day_start = self.dateEdit_1.dateTime().currentSecsSinceEpoch()
            day_end = self.dateEdit_2.dateTime().currentSecsSinceEpoch() + 86400
        current_day_data = []
        if oqc_products_list.data:
            for data_dict in oqc_products_list.data:
                if data_dict:
                    timestamp = data_dict.get("create_time")
                    if day_start < timestamp < day_end:
                        data_dict_final = copy.copy(data_dict)
                        ret = oqc_result.read_row("sn", data_dict.get("sn"))
                        usb_power = ret.get("usb_power")
                        iot = ret.get("iot")
                        data_dict_final.update({"usb_power": usb_power, "iot": iot})
                        current_day_data.append(data_dict_final)

        hiworker.TableLoad.load_table_common(self.tableWidget_products_list,
                                             current_day_data,
                                             table_header.products_list,
                                             sort="create_time",
                                             reverse=True)

    def output_txt(self):
        sn_list = self.get_current_selected_sn()
        if sn_list:
            for sn in sn_list:
                data_dict = oqc_result.read_row("sn", sn)
                if data_dict:
                    dict_to_txt_by_line(data_dict)
                else:
                    self.textBrowser.append("项目：" + sn + " 没有测试数据，导出失败")
                # Thread(target=dict_to_txt_by_line, args=(data_dict, )).start()

    def output_current_item(self):
        if self.current_testing_sn:
            data_dict = oqc_result.read_row("sn", self.current_testing_sn)
            if data_dict:
                Thread(target=dict_to_txt_by_line, args=(data_dict, True, False)).start()
                self.has_output = True
            else:
                self.textBrowser.append("项目：" + self.current_testing_sn + "没有测试数据")

        else:
            self.textBrowser.append("没有当前项目")

    def output_txt_bridge(self):
        sn_list = self.get_current_selected_sn()
        if sn_list:
            for sn in sn_list:
                data_dict = oqc_result.read_row("sn", sn)
                if data_dict:
                    product = oqc_products_list.read_row("sn", sn)
                    data_dict.update({"web_passwd": product.get("web_passwd"),
                                      "create_time": product.get("create_time"),
                                      "mac_addr": product.get("mac_addr"),
                                      "check_sn": sn})
                    dict_to_txt_by_line(data_dict, is_bridge=True)
                else:
                    self.textBrowser.append("项目：" + sn + " 没有测试数据，导出失败")

    def output_current_item_bridge(self):
        if self.current_testing_sn:
            data_dict = oqc_result.read_row("sn", self.current_testing_sn)
            if data_dict:
                data_dict.update({"web_passwd": self.current_product.get("web_passwd"),
                                  "create_time": self.current_product.get("create_time"),
                                  "mac_addr": self.current_product.get("mac_addr"),
                                  "check_sn": self.current_testing_sn})
                Thread(target=dict_to_txt_by_line, args=(data_dict, True, True)).start()
                self.has_output = True
            else:
                self.textBrowser.append("项目：" + self.current_testing_sn + "没有测试数据")

        else:
            self.textBrowser.append("没有当前项目")

    def open_txt_in_list(self):
        current_select_sn = hiworker.TableRead.get_current_row_col_data(self.tableWidget_products_list, 1)
        data_dict = oqc_products_list.read_row("sn", current_select_sn)
        Thread(target=open_txt, args=(data_dict, )).start()

    def open_txt_in_list_bridge(self):
        current_select_sn = hiworker.TableRead.get_current_row_col_data(self.tableWidget_products_list, 1)
        data_dict = oqc_products_list.read_row("sn", current_select_sn)
        Thread(target=open_txt, args=(data_dict, True)).start()

    def show_product_list_menu(self):
        self.product_menu.popup(QCursor.pos())

    @staticmethod
    def open_doc_folder():
        folder = os.path.join(os.getcwd(), "doc")
        os.system("explorer.exe %s" % folder)

    """
    网页检测部分
    """

    def one_key_bridge(self):
        if self.current_product.get("sn"):
            Thread(target=self.run_one_key_bridge).start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def run_one_key_bridge(self):
        if ping_bridge("192.168.123.254", ok_times=36, max_times=300, threshold=100):
            if self.lgu_7600.config_bridge(show_input=False):
                if ping_bridge("192.168.123.254", ok_times=6, max_times=60, threshold=5):
                    self.libre_speed_test.start_speed_test(self.current_product, self.wlan_eth, self.lan_eth)
                else:
                    signal_main_ui.refresh_text_browser.emit("SSID重启超时, 请重试")
            else:
                signal_main_ui.refresh_text_browser.emit("已停止")
        else:
            signal_main_ui.refresh_text_browser.emit("桥接超时, 请重试")

    def save_bridge_ip(self, bridge_ip):
        self.bridge_ip = bridge_ip

    def open_web_page(self):
        """
        打开页面
        :return:
        """
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.check_ui, args=(False, False))
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def open_bridge_page(self):
        """
        打开页面
        :return:
        """
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.config_bridge, args=(True, ))
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def config_bridge_page(self):
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.config_bridge, args=(False, ))
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def reset_bridge(self):
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.reset_bridge)
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def skip_reset_bridge(self):
        self.lgu_7600.skip_reset_bridge()

    def reconnect_bridge(self):
        Thread(target=reconnect_bridge_eth, args=(self.bridge_ctrl_eth, )).start()

    def speed_test_bridge(self):
        if self.current_testing_sn:
            Thread(target=self.libre_speed_test.start_speed_test, args=(self.current_product, self.wlan_eth, self.lan_eth)).start()
        else:
            self.textBrowser.append("当前没有测试项目")

    def main_ap_wps(self):
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.main_ap_wps)
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def check_web_log(self):
        """
        检测日志
        :return:
        """
        t1 = Thread(target=self.lgu_7600.check_log)
        t1.start()

    def one_key_ui_iperf(self):
        if self.current_product.get("sn"):
            Thread(target=self.check_web_ui_and_set_wifi).start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def run_one_key_ui_iperf(self):
        if ping_bridge("192.168.123.254", ok_times=36, max_times=300, threshold=100):
            self.check_web_ui_and_set_wifi()
        else:
            signal_main_ui.refresh_text_browser.emit("连接超时, 请重试")

    def check_web_ui_and_set_wifi(self):
        """
        检测UI和设置WIFI
        :return:
        """
        test_speed = True if oqc_setting.get_auto_speed() else False
        if self.current_product.get("sn"):
            t1 = Thread(target=self.lgu_7600.check_ui, args=(test_speed, False))
            t1.start()
        else:
            signal_main_ui.refresh_text_browser.emit("当前没有测试项")

    def save_usb_power(self):
        v = self.lineEdit_v.text()
        a = self.lineEdit_a.text()

        if a and v:
            try:
                v_f = float(v)
                if v_f < 4:
                    self.dialog_show_message.show_message("USB power is Low，Check it please")
                    return
                if v_f > 5:
                    self.dialog_show_message.show_message("USB power is high，Check it please")
                    return
            except ValueError:
                self.dialog_show_message.show_message("Only Input Number Please")
                return
            if self.current_testing_sn:
                power = str(v) + "V  " + str(a) + "A"
                success = oqc_result.edit_result({"usb_power": power}, "sn", self.current_product.get("sn"))
                if success:
                    signal_main_ui.refresh_text_browser.emit("USB " + power + "Saved")
                    signal_load_table.load_products_list.emit()
                self.clear_usb_power()

            else:
                signal_main_ui.refresh_text_browser.emit("当前测试项未设置")
        else:
            signal_main_ui.refresh_text_browser.emit("USB电压或电流不能为空")

    def show_usb_power_dialog(self):
        sn = hiworker.TableRead.get_current_row_col_data(self.tableWidget_products_list, 1)
        if sn:
            self.dialog_save_usb_power.show_usb_power(sn)
        else:
            signal_main_ui.refresh_text_browser.emit("手动设置USB电压时SN为空")

    def show_bridge_save_dialog(self):
        sn = self.current_testing_sn
        if sn:
            self.dialog_bridge_input.show_bridge_speed_test_save(sn)
        else:
            signal_main_ui.refresh_text_browser.emit("当前测试项为空")

    def clear_usb_power(self):
        self.lineEdit_v.clear()
        # self.lineEdit_a.clear()

    """
    测速部分
    """
    def iperf_all(self):
        if self.current_testing_sn:
            self.iperf3.set_iperf_option(self.current_product, 1, self.lan_eth, self.wlan_eth, iperf_one_key=True)
            self.run_iperf()
        else:
            self.textBrowser.append("当前没有测试项目")

    def iperf_lan_1g(self):
        self.connect_wifi.delete_all_profile()
        if self.current_testing_sn:
            self.iperf3.set_iperf_option(self.current_product, 1, self.lan_eth, self.wlan_eth, oqc_setting.get_auto_txt())
            self.run_iperf()
        else:
            self.textBrowser.append("当前没有测试项目")

    def iperf_wifi_2g(self):
        if self.current_testing_sn:
            self.iperf3.set_iperf_option(self.current_product, 2, self.lan_eth, self.wlan_eth)
            self.run_iperf()
        else:
            self.textBrowser.append("当前没有测试项目")

    def iperf_wifi_5g(self):
        if self.current_testing_sn:
            self.iperf3.set_iperf_option(self.current_product, 5, self.lan_eth, self.wlan_eth)
            self.run_iperf()
        else:
            self.textBrowser.append("当前没有测试项目")

    def run_iperf(self):
        if not self.iperf3.isRunning():
            self.iperf3.start()

    def stop_iperf(self):
        self.iperf3.stop()

    """
    网络控制部分
    """
    def disable_lan(self):
        self.textBrowser.append("禁用：" + self.lan_eth)
        set_adapter_enable(self.lan_eth, False)

    def set_dhcp(self):
        Thread(target=set_adapter_dhcp, args=(self.lan_eth, self.wlan_eth, )).start()

    def set_lan_ip_200(self):
        Thread(target=set_adapter_ip_200, args=(self.lan_eth, )).start()
        self.current_testing = False

    def set_sw_rest(self):
        if self.current_testing and not self.has_output:
            self.textBrowser.append("请先导出当前项")
            return
        self.connect_wifi.delete_all_profile()
        time.sleep(1)
        Thread(target=set_adapter_ip_200, args=(self.lan_eth,)).start()
        self.current_testing = False
        self.has_output = False

    def cancel_current_item(self):
        self.has_output = True
        self.current_testing = False
        self.current_testing_sn = ""
        self.current_product = {}
        self.lgu_7600.set_product({})
        self.lgu_7600.stop = True
        self.libre_speed_test.stop = True
        self.textBrowser.clear()
        self.groupBox_operation.setTitle("当前操作项S/N：")

    def set_has_output(self):
        self.has_output = True
        self.current_testing = False

    def get_eth(self):
        self.lan_eth = oqc_setting.get_lan_eth()
        if self.lan_eth:
            if hiworker.is_adapter_exist(self.lan_eth):
                self.textBrowser.append("有线网卡：" + self.lan_eth)
            else:
                self.textBrowser.append("有线网卡：" + self.lan_eth + "不存在, 请重新选择")
        else:
            self.textBrowser.append("未选择有线网卡")

        self.wlan_eth = oqc_setting.get_wlan_eth()
        if self.wlan_eth:
            if hiworker.is_adapter_exist(self.wlan_eth):
                self.textBrowser.append("无线网卡：" + self.wlan_eth)
            else:
                self.textBrowser.append("无线网卡：" + self.wlan_eth + "不存在, 请重新选择")
        else:
            self.textBrowser.append("未选择无线网卡")

        self.bridge_ctrl_eth = oqc_setting.get_bridge_ctrl_eth()
        if self.bridge_ctrl_eth:
            if hiworker.is_adapter_exist(self.bridge_ctrl_eth):
                self.textBrowser.append("桥接控制网卡：" + self.bridge_ctrl_eth)
            else:
                self.textBrowser.append("桥接控制网卡：" + self.bridge_ctrl_eth + "不存在, 请重新选择")
        else:
            self.textBrowser.append("未选择桥接控制网卡")

        self.textBrowser.append("MAIN AP SSID: " + str(oqc_setting.get_main_ap_ssid()))
        self.textBrowser.append("MAIN AP PASSWD: " + str(oqc_setting.get_main_ap_passwd()))
        self.textBrowser.append("\n")

    def close_in_timer(self, close_message: str):
        for i in reversed(range(10)):
            self.refresh_text_browser(close_message + "，即将关闭: " + str(i))
            time.sleep(1)
        self.close()

    def show_txt_to_excel(self):
        self.txt_to_excel.show()
