from PySide6 import QtWidgets
from app.source.ui.save_usb_power import Ui_Dialog_save_usb_power
from app.data.oqc_test_result import oqc_result
from app.app_signal.app_signal import signal_main_ui, signal_load_table


class DialogSaveUSBPower(QtWidgets.QDialog, Ui_Dialog_save_usb_power):
    def __init__(self):
        super(DialogSaveUSBPower, self).__init__()
        self.setupUi(self)
        self.pushButton_save.clicked.connect(self.save_usb_power)
        self.sn = ""

    def save_usb_power(self):
        if self.sn:
            v = self.lineEdit_v.text()
            a = self.lineEdit_a.text()
            if a and v:
                try:
                    v_f = float(v)
                    if v_f < 4:
                        self.label_5.setText("Voltage too High，Check it Again")
                        return
                    if v_f > 5:
                        self.label_5.setText("Voltage too Low，Check it Again")
                        return
                except ValueError:
                    self.label_5.setText("Only input Number")
                    return
                power = str(v) + "V  " + str(a) + "A"
                success = oqc_result.edit_result({"usb_power": power}, "sn", self.sn)
                if success:
                    signal_main_ui.refresh_text_browser.emit(self.sn + "：USB " + power + "Saved")
                    signal_load_table.load_products_list.emit()
                self.close()
            else:
                self.label_5.setText("Value Can not be Null")
        else:
            self.label_5.setText("The selected item is Error")

    def show_usb_power(self, sn: str):
        if sn:
            self.sn = sn
        else:
            self.sn = ""
        self.lineEdit_v.clear()
        self.lineEdit_v.setFocus()
        self.show()
