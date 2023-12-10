from PySide6 import QtWidgets
from app.source.ui.bridge_input import Ui_Dialog_bridge_input
from app.data.oqc_test_result import oqc_result
from app.data.oqc_product_list import oqc_products_list
from app.app_signal.app_signal import signal_main_ui, signal_load_table
import re
from ...txt.txt import dict_to_txt_by_line


class DialogBridgeSpeedTestSave(QtWidgets.QDialog, Ui_Dialog_bridge_input):
    def __init__(self):
        super(DialogBridgeSpeedTestSave, self).__init__()
        self.setupUi(self)
        self.sn = ""
        self.pushButton_save.clicked.connect(self.save_bridge_input)

        self.lineEdit_bridge_5G_down.returnPressed.connect(self.lineEdit_bridge_5G_up.setFocus)
        self.lineEdit_bridge_5G_down.returnPressed.connect(self.lineEdit_bridge_5G_up.selectAll)
        self.lineEdit_bridge_5G_up.returnPressed.connect(self.lineEdit_main_5G_down.setFocus)
        self.lineEdit_bridge_5G_up.returnPressed.connect(self.lineEdit_main_5G_down.selectAll)

        self.lineEdit_main_5G_down.returnPressed.connect(self.lineEdit_main_5G_up.setFocus)
        self.lineEdit_main_5G_down.returnPressed.connect(self.lineEdit_main_5G_up.selectAll)
        # self.lineEdit_main_5G_up.returnPressed.connect(self.lineEdit_bridge_5G_down.setFocus)
        self.lineEdit_main_5G_up.returnPressed.connect(self.save_bridge_input)

        self.bridge_input_str = {}

    def save_bridge_input(self):
        if self.sn:
            self.bridge_input_str.update({"main_5g_down": self.lineEdit_main_5G_down.text()})
            self.bridge_input_str.update({"main_5g_up": self.lineEdit_main_5G_up.text()})
            self.bridge_input_str.update({"bridge_5g_down": self.lineEdit_bridge_5G_down.text()})
            self.bridge_input_str.update({"bridge_5g_up": self.lineEdit_bridge_5G_up.text()})

            for key, value in self.bridge_input_str.items():
                if value:
                    if not re.match(r"^[-+]?[0-9]*\.?[0-9]+$", value):
                        self.label_5.setText(key + "不是数字")
                        return
                else:
                    self.bridge_input_str.update({key: 0})

            success = oqc_result.edit_result(self.bridge_input_str, "sn", self.sn)
            if success:
                signal_main_ui.refresh_text_browser.emit("\nBridge Speed Test Save: " + self.sn)
                for key, value in self.bridge_input_str.items():
                    if key == "sn":
                        continue
                    signal_main_ui.refresh_text_browser.emit(key + ": " + str(value) + " Mbits/sec")
                signal_load_table.load_products_list.emit()
                product = oqc_products_list.db_read_row(refer_value=self.sn, refer="sn")
                self.bridge_input_str.update({"web_passwd": product.get("web_passwd"),
                                              "check_sn": self.sn,
                                              "sn": self.sn,
                                              "mac_addr": product.get("mac_addr"),
                                              "create_time": product.get("create_time")})
                dict_to_txt_by_line(self.bridge_input_str, open_when_finished=True, is_bridge=True)
                self.bridge_input_str = {}
                self.lineEdit_main_5G_down.clear()
                self.lineEdit_main_5G_up.clear()
                self.lineEdit_bridge_5G_down.clear()
                self.lineEdit_bridge_5G_up.clear()
                self.close()

            else:
                self.label_5.setText("Bridge Speed Test Write Error !")

        else:
            self.label_5.setText("The selected item is Error")

    def show_bridge_speed_test_save(self, sn: str):
        if sn:
            self.sn = sn
            self.label_sn.setText(sn)
        else:
            self.sn = ""
        self.lineEdit_bridge_5G_down.setFocus()
        self.show()
