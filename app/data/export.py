from app.source.ui.main_export import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal
import os
import xlwings as xw
import time
from threading import Thread


class SignalApp(QObject):
    signal_info = Signal(str)


signal_app = SignalApp()


class GAPK7600Txt2Excel(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GAPK7600Txt2Excel, self).__init__()
        self.setupUi(self)
        self.file_path = ""
        self.file_list = []
        self.start_count = 0
        self.pushButton_select_path.clicked.connect(self.select_txt_directory)
        self.pushButton_start_mp.clicked.connect(self.start_mp)
        self.pushButton_start_spec.clicked.connect(self.start_spec)
        self.pushButton_start_bridge.clicked.connect(self.start_bridge)
        signal_app.signal_info.connect(self.set_info)

    def show(self) -> None:
        self.label_info.clear()
        super(GAPK7600Txt2Excel, self).show()

    def start_mp(self):
        self.label_info.clear()
        if self.get_txt_file_list():
            Thread(target=self.txt_2_excel_mp).start()

    def start_spec(self):
        self.label_info.clear()
        if self.get_txt_file_list():
            Thread(target=self.txt_2_excel_spec).start()

    def start_bridge(self):
        self.label_info.clear()
        if self.get_txt_file_list():
            Thread(target=self.txt_2_excel_bridge).start()

    def txt_2_excel_mp(self):
        self.start_count = self.spinBox_start_count.value()

        save_name = "GAPK-7600 _측정값 정리_MP_" \
                    + time.strftime("%Y%m%d%H%M%S", time.localtime()) \
                    + "_" + str(self.start_count)\
                    + "~" + str(self.start_count + len(self.file_list) - 1)\
                    + ".xlsx"

        if not self.check_option():
            return

        wb_mp = xw.Book()
        sht = wb_mp.sheets["Sheet1"]
        sheet_name = "GAPK-7600 (" + time.strftime("%m%d", time.localtime()) \
                     + "_" + str(self.start_count) \
                     + "~" + str(self.start_count + len(self.file_list) - 1) + ")"

        sht.name = sheet_name
        sht.range('B1').value = "GAPK7600 _" + str(self.start_count) + "~" + str(self.start_count + len(self.file_list) - 1)
        sht.range('B1:D1').merge(across=True)
        sht.range('B1:E1').api.Borders(9).LineStyle = 9

        sht.range(1, 1).column_width = 2.75
        sht.range(1, 2).column_width = 6.13
        sht.range(1, 3).column_width = 11.38
        sht.range(1, 4).column_width = 11.38
        sht.range(1, 5).column_width = 61.13

        sht.range(1, 1).row_height = 39

        active_window = wb_mp.app.api.ActiveWindow
        active_window.FreezePanes = False
        active_window.SplitRow = 1
        active_window.FreezePanes = True

        result_data = {}
        for file_name in self.file_list:

            result_lines = []
            try:
                with open(os.path.join(self.file_path, file_name), "r", encoding="utf-8") as fr:
                    txt_content = fr.readlines()
                    if txt_content:
                        sn = ""
                        for line in txt_content:
                            if "KABGA" in line:
                                sn = line.strip()
                            elif "]" in line:
                                result_lines.append(line)
                        result_data.update({sn: result_lines})

            finally:
                pass
        if result_data:
            self.set_result_range_mp(sht, result_data)
            sht.range((1, 1), (len(result_data)*8 + 1, 5)).api.Font.Name = '宋体'
            sht.range((1, 1), (len(result_data)*8 + 1, 5)).api.Font.Size = 10
        wb_mp.save(save_name)
        signal_app.signal_info.emit("已完成")

    def set_result_range_mp(self, sht, result_data: dict):
        for index, sn in enumerate(result_data.keys()):
            signal_app.signal_info.emit("当前项目: " + sn)
            result_lines = result_data.get(sn)
            n = index * 8

            sht.range(2 + n, 2).value = self.start_count + index
            sht.range((2 + n, 2), (9 + n, 2)).merge()

            sht.range(2 + n, 1).row_height = 27
            sht.range(2 + n, 3).value = "S/N"
            sht.range(2 + n, 5).value = sn
            sht.range((2 + n, 3), (2 + n, 4)).merge()

            sht.range(3 + n, 1).row_height = 66.75
            sht.range(3 + n, 3).value = "WIFI"
            sht.range(3 + n, 4).value = "WIFI _5G"

            sht.range((3 + n, 3), (4 + n, 3)).merge()

            sht.range(4 + n, 1).row_height = 66.75
            sht.range(4 + n, 4).value = "WIFI _2.4G"

            sht.range(5 + n, 1).row_height = 66.75
            sht.range(5 + n, 3).value = "유선"
            sht.range(5 + n, 4).value = "1G"

            sht.range(6 + n, 1).row_height = 14
            sht.range(6 + n, 3).value = "인사이더"
            sht.range(6 + n, 4).value = "2.4G"
            sht.range((6 + n, 3), (7 + n, 3)).merge()

            sht.range(7 + n, 1).row_height = 14
            sht.range(7 + n, 4).value = "5G"

            sht.range(8 + n, 1).row_height = 54
            sht.range(8 + n, 3).value = "벤치비"
            sht.range(8 + n, 4).value = "1G"
            sht.range((8 + n, 3), (9 + n, 3)).merge()

            sht.range(9 + n, 1).row_height = 54
            sht.range(9 + n, 4).value = "100M"

            sht.range((2 + n, 2), (9 + n, 4)).api.HorizontalAlignment = -4108
            sht.range((2 + n, 2), (9 + n, 4)).api.VerticalAlignment = -4108

            sht.range((2 + n, 5), (9 + n, 5)).api.VerticalAlignment = -4108

            sht.range((2 + n, 2), (9 + n, 2)).api.Borders(10).LineStyle = 1

            sht.range((9 + n, 2), (9 + n, 5)).api.Borders(9).LineStyle = 9

            sht.range((2 + n, 4), (9 + n, 4)).api.Borders(10).LineStyle = 1
            sht.range((2 + n, 4), (9 + n, 4)).api.Borders(7).LineStyle = 1
            sht.range((2 + n, 5), (9 + n, 5)).api.Borders(10).LineStyle = 1

            sht.range((2 + n, 3), (2 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((3 + n, 3), (3 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((4 + n, 3), (4 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((5 + n, 3), (5 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((6 + n, 3), (6 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((7 + n, 3), (7 + n, 5)).api.Borders(9).LineStyle = 2
            sht.range((8 + n, 3), (8 + n, 5)).api.Borders(9).LineStyle = 2

            try:
                ret_2_g = result_lines[0] + result_lines[1] + result_lines[2]
                sht.range(4 + n, 5).value = ret_2_g
            except IndexError:
                self.textBrowser.append(sn + " 2.4G数据缺失")

            try:
                ret_5_g = result_lines[3] + result_lines[4] + result_lines[5]
                sht.range(3 + n, 5).value = ret_5_g
            except IndexError:
                self.textBrowser.append(sn + " 5G数据缺失")

            try:
                ret_1_g = result_lines[6] + result_lines[7] + result_lines[8]
                sht.range(5 + n, 5).value = ret_1_g
            except IndexError:
                self.textBrowser.append(sn + " 1G数据缺失")

    def txt_2_excel_spec(self):
        self.start_count = self.spinBox_start_count.value()
        save_name = "Throughput SPEC 검토_측정 결과 분석_" \
                    + time.strftime("%Y%m%d%H%M%S", time.localtime()) \
                    + "_" + str(self.start_count) \
                    + "~" + str(self.start_count + len(self.file_list) - 1) \
                    + ".xlsx"
        if not self.check_option():
            return
        wb_spec = xw.Book()
        sht = wb_spec.sheets['Sheet1']
        sht.name = "SPEC"
        sht.range(2, 1).row_height = 13.5
        sht.range(3, 1).row_height = 13.5
        sht.range(4, 1).row_height = 13.5
        sht.range(5, 1).row_height = 13.5
        result_dict = {}
        for file_name in self.file_list:
            result_lines = []

            try:
                with open(os.path.join(self.file_path, file_name), "r", encoding="utf-8") as fr:
                    txt_content = fr.readlines()
                    if txt_content:
                        sn = ""
                        for line in txt_content:
                            if "KABGA" in line:
                                sn = line.strip()
                            elif "Mbits" in line:
                                result_lines.append(line)
                        result_dict.update({sn: result_lines})

            finally:
                pass
        if result_dict:
            self.set_result_range_spec(sht, result_dict)
        wb_spec.save(save_name)
        signal_app.signal_info.emit("已完成")

    def set_result_range_spec(self, sht, result_dict: dict):
        for index, sn in enumerate(result_dict.keys()):
            signal_app.signal_info.emit("当前项目: " + sn)
            item = result_dict.get(sn)
            n = index + 5
            sht.range(2, n).value = "#" + str(self.start_count + index)
            try:
                sender_2g = int(str(item[0]).split(" ")[13])
                receiver_2g = int(str(item[1]).split(" ")[13])
                if sender_2g > receiver_2g:
                    ret_2_g = receiver_2g
                else:
                    ret_2_g = sender_2g
                sht.range(3, n).value = ret_2_g
            except IndexError:
                self.textBrowser.append(sn + " 2.4G数据缺失")

            try:
                sender_5g = int(str(item[2]).split(" ")[13])
                receiver_5g = int(str(item[3]).split(" ")[13])
                if sender_5g > receiver_5g:
                    ret_5_g = receiver_5g
                else:
                    ret_5_g = sender_5g

                sht.range(4, n).value = ret_5_g
            except IndexError:
                self.textBrowser.append(sn + " 5G数据缺失")

            try:
                sender_1g = int(str(item[4]).split(" ")[13])
                receiver_1g = int(str(item[5]).split(" ")[13])
                if sender_1g > receiver_1g:
                    ret_1_g = receiver_1g
                else:
                    ret_1_g = sender_1g

                sht.range(5, n).value = ret_1_g
            except IndexError:
                self.textBrowser.append(sn + " 1G数据缺失")

            sht.range(1, n).column_width = 3.5

            sht.range(2, n).api.Font.Name = '宋体'
            sht.range(3, n).api.Font.Name = '宋体'
            sht.range(4, n).api.Font.Name = '宋体'
            sht.range(5, n).api.Font.Name = '宋体'

            sht.range(2, n).api.Font.Size = 9
            sht.range(3, n).api.Font.Size = 9
            sht.range(4, n).api.Font.Size = 9
            sht.range(5, n).api.Font.Size = 9

    def txt_2_excel_bridge(self):
        self.start_count = self.spinBox_start_count.value()
        if not self.check_option():
            return
        save_name = "GAPK-7600_Bridge_SpeedTest_" \
                    + time.strftime("%Y%m%d%H%M%S", time.localtime()) \
                    + "_MP_100대_.xlsx"
        wb_bridge = xw.Book()
        sht = wb_bridge.sheets['Sheet1']
        sht.name = "BridgeSpeedTest_MP16차_100대_"
        # 设置列宽
        for c in range(1, 9):
            if c == 1:
                sht.range(4, c).column_width = 6.5
                continue
            if c == 4:
                sht.range(4, c).column_width = 19.25
                continue
            sht.range(4, c).column_width = 14

        # 设置表头行高
        sht.range(1, 1).row_height = 36
        sht.range(2, 1).row_height = 36
        sht.range(3, 1).row_height = 16.5
        # 设置表头内容
        sht.range(1, 2).value = "GAPK 7600 5G Bridge Speed Test"
        sht.range((1, 2), (1, 8)).merge()

        sht.range((2, 1), (3, 8)).color = (255, 242, 204)

        sht.range(2, 1).value = "No."
        sht.range((2, 1), (3, 1)).merge()

        sht.range(2, 2).value = "Main AP 성능 \n(S/N: KABGA762103034858)"
        sht.range((2, 2), (2, 3)).merge()

        sht.range(2, 4).value = "Bridge AP 성능"
        sht.range((2, 4), (2, 6)).merge()

        sht.range(2, 7).value = "percentage(B/M)"
        sht.range((2, 7), (2, 8)).merge()

        sht.range(3, 2).value = "down"
        sht.range(3, 3).value = "up"

        sht.range(3, 4).value = "S/N"

        sht.range(3, 5).value = "down"
        sht.range(3, 6).value = "up"

        sht.range(3, 7).value = "down"
        sht.range(3, 8).value = "up"

        sht.range((1, 1), (3, 8)).api.HorizontalAlignment = -4108
        sht.range((1, 1), (3, 8)).api.VerticalAlignment = -4108
        print(self.file_list)
        # 初始化数据字典
        result_dict = {}
        # 遍历TXT文件
        for file_name in self.file_list:
            item_dict = {}

            try:
                with open(os.path.join(self.file_path, file_name), "r", encoding="utf-8") as fr:
                    txt_content = fr.readlines()
                    if txt_content:
                        sn = ""
                        # 遍历TXT文件内容
                        for line in txt_content:
                            if "KABGA" in line:
                                sn = line.strip()
                                item_dict.update({"sn": sn})
                            elif "main_5g_down" in line:
                                item_dict.update({"main_5g_down": float(line.lstrip("main_5g_down:").rstrip("Mbits/sec\n"))})
                            elif "main_5g_up" in line:
                                item_dict.update({"main_5g_up": float(line.lstrip("main_5g_up:").rstrip("Mbits/sec\n"))})
                            elif "bridge_5g_down" in line:
                                item_dict.update({"bridge_5g_down": float(line.lstrip("bridge_5g_down:").rstrip("Mbits/sec\n"))})
                            elif "bridge_5g_up" in line:
                                item_dict.update({"bridge_5g_up": float(line.lstrip("bridge_5g_up:").rstrip("Mbits/sec\n"))})
            finally:
                pass
            if item_dict:
                result_dict.update({sn: item_dict.copy()})
        print(result_dict)
        if result_dict:
            for r in range(1, len(result_dict) + 8):
                for c in range(1, 9):
                    sht.range(r, c).api.Borders(7).LineStyle = 1
                    sht.range(r, c).api.Borders(8).LineStyle = 1
                    sht.range(r, c).api.Borders(9).LineStyle = 1
                    sht.range(r, c).api.Borders(10).LineStyle = 1
            self.set_result_range_bridge(sht, result_dict)
        sht.range((1, 1), (207, 1)).api.Font.Name = '等线'
        sht.range((1, 1), (207, 8)).api.Font.Size = 10

        wb = xw.books.active
        active_window = wb.app.api.ActiveWindow
        active_window.FreezePanes = False
        active_window.SplitColumn = 1
        active_window.SplitRow = 3
        active_window.FreezePanes = True

        wb_bridge.save(save_name)
        signal_app.signal_info.emit("已完成")

    @staticmethod
    def set_result_range_bridge(sht, result_dict: dict):
        for index, item in enumerate(result_dict.values()):
            signal_app.signal_info.emit("当前项目: " + item.get("sn"))
            n = index + 4
            sht.range(n, 1).row_height = 21
            sht.range(n, 1).value = index + 1
            sht.range(n, 1).api.HorizontalAlignment = -4108
            if item.get("main_5g_down"):
                sht.range(n, 2).value = item.get("main_5g_down")
            if item.get("main_5g_up"):
                sht.range(n, 3).value = item.get("main_5g_up")

            sht.range(n, 4).color = (255, 242, 204)
            sht.range(n, 4).value = item.get("sn")
            sht.range(n, 4).api.HorizontalAlignment = -4108
            if item.get("bridge_5g_down"):
                sht.range(n, 5).value = item.get("bridge_5g_down")
            if item.get("bridge_5g_up"):
                sht.range(n, 6).value = item.get("bridge_5g_up")

            try:
                sht.range(n, 7).api.NumberFormat = "0%"
                sht.range(n, 7).value = round(item.get("bridge_5g_down") / item.get("main_5g_down"), 2)
            except ZeroDivisionError:
                pass

            try:
                sht.range(n, 8).api.NumberFormat = "0%"
                sht.range(n, 8).value = round(item.get("bridge_5g_up") / item.get("main_5g_up"), 2)
            except ZeroDivisionError:
                pass

        result_count = len(result_dict)
        sht.range(result_count + 4, 1).row_height = 3.5

        sht.range(result_count + 5, 1).row_height = 14.25
        sht.range(result_count + 5, 1).value = "Max"
        sht.range(result_count + 5, 2).formula = '=MAX(B4:B' + str(result_count + 3) + ')'
        sht.range(result_count + 5, 3).formula = '=MAX(C4:C' + str(result_count + 3) + ')'
        sht.range(result_count + 5, 4).value = "-"
        sht.range(result_count + 5, 5).formula = '=MAX(E4:E' + str(result_count + 3) + ')'
        sht.range(result_count + 5, 6).formula = '=MAX(F4:F' + str(result_count + 3) + ')'
        sht.range(result_count + 5, 7).formula = '=MAX(G4:G' + str(result_count + 3) + ')'
        sht.range(result_count + 5, 8).formula = '=MAX(H4:H' + str(result_count + 3) + ')'

        sht.range(result_count + 6, 1).row_height = 14.25
        sht.range(result_count + 6, 1).value = "Min"
        sht.range(result_count + 6, 2).formula = '=MIN(B4:B' + str(result_count + 3) + ')'
        sht.range(result_count + 6, 3).formula = '=MIN(C4:C' + str(result_count + 3) + ')'
        sht.range(result_count + 6, 4).value = "-"
        sht.range(result_count + 6, 5).formula = '=MIN(E4:E' + str(result_count + 3) + ')'
        sht.range(result_count + 6, 6).formula = '=MIN(F4:F' + str(result_count + 3) + ')'
        sht.range(result_count + 6, 7).formula = '=MIN(G4:G' + str(result_count + 3) + ')'
        sht.range(result_count + 6, 8).formula = '=MIN(H4:H' + str(result_count + 3) + ')'

        sht.range(result_count + 7, 1).row_height = 14.25
        sht.range(result_count + 7, 1).value = "Avr"
        sht.range(result_count + 7, 2).formula = '=ROUND(AVERAGE(B4:B' + str(result_count + 3) + '), 0)'
        sht.range(result_count + 7, 3).formula = '=ROUND(AVERAGE(C4:C' + str(result_count + 3) + '), 0)'
        sht.range(result_count + 7, 4).value = "-"
        sht.range(result_count + 7, 5).formula = '=ROUND(AVERAGE(E4:E' + str(result_count + 3) + '), 0)'
        sht.range(result_count + 7, 6).formula = '=ROUND(AVERAGE(F4:F' + str(result_count + 3) + '), 0)'
        sht.range(result_count + 7, 7).formula = '=ROUND(AVERAGE(G4:G' + str(result_count + 3) + '), 2)'
        sht.range(result_count + 7, 8).formula = '=ROUND(AVERAGE(H4:H' + str(result_count + 3) + '), 2)'

        sht.range((result_count + 5, 1), (result_count + 6, 8)).color = (226, 239, 218)
        sht.range((result_count + 7, 1), (result_count + 7, 8)).color = (221, 235, 247)

        sht.range((result_count + 5, 1), (result_count + 7, 1)).api.HorizontalAlignment = -4108
        sht.range((result_count + 5, 1), (result_count + 7, 1)).api.VerticalAlignment = -4108

        sht.range((result_count + 5, 4), (result_count + 7, 4)).api.HorizontalAlignment = -4108
        sht.range((result_count + 5, 4), (result_count + 7, 4)).api.VerticalAlignment = -4108

    def get_txt_file_list(self):
        self.file_list = []
        try:
            file_list = os.listdir(self.file_path)

            for file_name in file_list:
                if "KABGA" in file_name:
                    self.file_list.append(file_name)
            else:
                if self.file_list:
                    return True
                else:
                    signal_app.signal_info.emit("文件夹中没有指定TXT")
                    return False

        except FileNotFoundError:
            signal_app.signal_info.emit("TXT文件夹路径不能为空")
            return False

    def check_option(self):
        if not self.file_path:
            signal_app.signal_info.emit("TXT文件夹路径不能为空")
            return False
        elif not self.start_count:
            signal_app.signal_info.emit("起始数量为空")
            return False
        elif not self.file_list:
            signal_app.signal_info.emit("文件夹中没有指定TXT")
            return False
        else:
            return True

    def set_info(self, info: str):
        self.label_info.setText(info)

    def select_txt_directory(self):
        self.file_path = QtWidgets.QFileDialog.getExistingDirectory(self, caption='请选择TXT所在文件夹')
        self.lineEdit_select_path.setText(self.file_path)
