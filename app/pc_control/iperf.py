import subprocess
import os
import psutil
import time
from ..app_signal.app_signal import signal_main_ui
from ..data.oqc_test_result import oqc_result
from ..data.oqc_setting import oqc_setting
from ..txt.txt import dict_to_txt_by_line
from .network import ConnectWifi, set_adapter_dhcp, set_adapter_enable, set_adapter_ip_200
from hiworker.thread.thread import Thread


# iperf3.exe -c 192.168.0.100 -t 60 -i 1 -R -w 5m
class Iperf(Thread):
    def __init__(self):
        super(Iperf, self).__init__()
        self.sn = ""
        self.net_type = 0
        self.auto_txt = False
        self.current_product = {}
        self.iperf_one_key = False
        self.connect_wifi = ConnectWifi()
        self.lan_eth = ""
        self.wlan_eth = ""

    def run(self) -> None:
        self.stop_flag = False
        if not self.iperf_one_key:
            self.save_result(self.do_iperf_7600())
        else:
            result = oqc_result.read_row("sn", self.current_product.get("sn"))
            iperf_2g = result.get("iperf_2g", " ")
            iperf_5g = result.get("iperf_5g", " ")
            iperf_1g = result.get("iperf_1g", " ")

            if not iperf_1g:
                self.net_type = 1
                self.save_result(self.do_iperf_7600())
            else:
                speed_1g_index = iperf_1g.find("Mbits") - 6
                if speed_1g_index > 5:
                    speed_1g = float((iperf_1g[speed_1g_index: speed_1g_index + 5]).strip())
                    if speed_1g < 949:
                        signal_main_ui.refresh_text_browser.emit("LAN 速度 " + str(speed_1g) + "Mbits，Retesting")
                        self.net_type = 1
                        self.save_result(self.do_iperf_7600())

            if not iperf_2g:
                if self.stop_flag:
                    return
                for i in range(3):
                    signal_main_ui.refresh_text_browser.emit("准备 2.4G: " + str(3-i))
                    time.sleep(1)
                self.net_type = 2
                self.save_result(self.do_iperf_7600())
            else:
                speed_2g_index = iperf_2g.find("Mbits") - 6
                if speed_2g_index > 5:
                    speed_2g = float((iperf_2g[speed_2g_index: speed_2g_index + 5]).strip())
                    if speed_2g < 390:
                        signal_main_ui.refresh_text_browser.emit("2.4G_速度 " + str(speed_2g) + "Mbits，Retesting")
                        for i in range(3):
                            signal_main_ui.refresh_text_browser.emit("准备 2.4G: " + str(3 - i))
                            time.sleep(1)
                        self.net_type = 2
                        self.save_result(self.do_iperf_7600())

            if not iperf_5g:
                if self.stop_flag:
                    return
                for i in range(3):
                    signal_main_ui.refresh_text_browser.emit("准备 5G: " + str(3-i))
                    time.sleep(1)
                self.net_type = 5
                self.save_result(self.do_iperf_7600())
            else:
                speed_5g_index = iperf_5g.find("Mbits") - 6
                if speed_5g_index > 5:
                    speed_5g = float((iperf_5g[speed_5g_index: speed_5g_index + 5]).strip())
                    if speed_5g < 900:
                        signal_main_ui.refresh_text_browser.emit("5G 速度 " + str(speed_5g) + "Mbits，Retesting")
                        if self.stop_flag:
                            return
                        for i in range(3):
                            signal_main_ui.refresh_text_browser.emit("准备 5G: " + str(3 - i))
                            time.sleep(1)
                        self.net_type = 5
                        self.save_result(self.do_iperf_7600())
            if self.stop_flag:
                return

            if not self.check_result_speed():
                return

            signal_main_ui.refresh_text_browser.emit("\n自动导出TXT...")
            result = oqc_result.read_row("sn", self.current_product.get("sn"))
            dict_to_txt_by_line(result, True)
            signal_main_ui.set_has_output.emit()
            time.sleep(0.5)
            signal_main_ui.refresh_text_browser.emit("清空WIFI记录...\n")
            self.connect_wifi.delete_all_profile()
            time.sleep(0.5)
            if oqc_setting.get_auto_ip_200():
                signal_main_ui.refresh_text_browser.emit("设置 IP 200...\n")
                set_adapter_ip_200(self.lan_eth)
            else:
                signal_main_ui.refresh_text_browser.emit("设置 DHCP...\n")
                set_adapter_dhcp(self.lan_eth, self.wlan_eth, disable_before=False)

    def set_iperf_option(self, product_dict: dict, net_type: int, lan_eth: str, wlan_eth: str,
                         iperf_one_key=False, auto_txt=False):
        self.current_product = product_dict
        self.net_type = net_type
        self.auto_txt = auto_txt
        self.lan_eth = lan_eth
        self.wlan_eth = wlan_eth
        self.iperf_one_key = iperf_one_key

    def do_iperf_7600(self, bin_path="bin", exe_file="iperf3.exe"):

        if not self.set_iperf_network():
            self.stop_flag = True
            return []
        time_sec = 3
        if self.net_type == 2:
            time_sec = 6
        for i in range(time_sec):
            signal_main_ui.refresh_text_browser.emit(str(time_sec-i))
            time.sleep(1)
        iperf_result = []
        iperf_path = os.path.join(os.path.abspath(os.getcwd()), bin_path, exe_file)
        ret = subprocess.Popen([iperf_path, "-c", "192.168.0.100", "-t", "60", "-i", "1", "-R", "-w", "5m", "--forceflush"],
                               shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        iot_check_time = 10
        for line in ret.stdout:
            if self.net_type == 1:
                iot_check_time -= 1
                if iot_check_time <= 0:
                    result = oqc_result.read_row("sn", self.current_product.get("sn"))
                    iot_status = result.get("iot")
                    if not iot_status:
                        signal_main_ui.check_iot_again.emit()
                        iot_check_time = 10
                    else:
                        iot_check_time = 60
            line = line.decode(encoding="ansi")
            line = line.strip("\r\n")
            signal_main_ui.refresh_text_browser.emit(line)
            iperf_result.append(line)
            if self.stop_flag or ("iperf3: error" in line):
                try:
                    parent_proc = psutil.Process(ret.pid)
                    for child_proc in parent_proc.children(recursive=True):
                        child_proc.kill()
                    parent_proc.kill()
                except:
                    pass
                return []
        ret.stdout.close()
        return iperf_result

    def set_iperf_network(self):
        if self.net_type == 1:
            self.connect_wifi.delete_all_profile()
            time.sleep(0.5)
            if set_adapter_dhcp(self.lan_eth, self.wlan_eth, disable_before=False):
                signal_main_ui.refresh_text_browser.emit("Testing: LAN 1G")
                return True
        else:
            self.connect_wifi.delete_all_profile()
            time.sleep(0.5)
            set_adapter_enable(net_connection_id=self.lan_eth, enable=False)
            if self.current_product.get("sn"):
                wifi_passwd = self.current_product.get("wifi_passwd")
                if not wifi_passwd:
                    signal_main_ui.refresh_text_browser.emit("WIFI is empty")
                    return
                wifi_name = "U+Net" + self.current_product.get("mac_addr")[-4:]
                if wifi_name:
                    if self.net_type == 5:
                        wifi_name = wifi_name + "_5G"
                    signal_main_ui.refresh_text_browser.emit("Connecting：" + wifi_name)
                    self.connect_wifi.set_wifi_args(wifi_name, wifi_passwd, self.wlan_eth)
                    if self.connect_wifi.connect_wifi():
                        signal_main_ui.refresh_text_browser.emit("Testing: " + wifi_name)
                        return True
                else:
                    signal_main_ui.refresh_text_browser.emit("WIFI SSID is empty")

    def save_result(self, iperf_result: list):
        if len(iperf_result) > 5 and iperf_result[-1] == "iperf Done.":
            result_text = str(iperf_result[-5]) + "\n" + str(iperf_result[-4]) + "\n" + str(iperf_result[-3])
            if self.net_type == 5:
                data_dict = {"iperf_5g": result_text}
            elif self.net_type == 2:
                data_dict = {"iperf_2g": result_text}
            else:
                data_dict = {"iperf_1g": result_text}
            oqc_result.update_row(data_dict, "sn", self.current_product.get("sn"))
        else:
            signal_main_ui.refresh_text_browser.emit("\nSpeed test is broken")
        signal_main_ui.refresh_text_browser.emit("\n")

    def check_result_speed(self):
        result = oqc_result.read_row("sn", self.current_product.get("sn"))
        if result:
            iperf_2g = result.get("iperf_2g", "")
            iperf_5g = result.get("iperf_5g", "")
            iperf_1g = result.get("iperf_1g", "")

            if iperf_2g:
                speed_2g_index = iperf_2g.find("Mbits") - 4
                if speed_2g_index > 5:
                    speed_2g = int((iperf_2g[speed_2g_index: speed_2g_index + 3]).strip())
                    if speed_2g >= 390:
                        signal_main_ui.refresh_text_browser.emit("WiFi 2G: " + str(speed_2g) + " Mbps")
                    else:
                        signal_main_ui.refresh_text_browser.emit("\nWiFi 2.4G 速度过低, 请重新测试\n")
                        return False
                else:
                    signal_main_ui.refresh_text_browser.emit("WiFi 2.4G 速度为空, 请重新测试")
                    return False
            else:
                signal_main_ui.refresh_text_browser.emit("WiFi 2.4G 速度为空, 请重新测试")
                return False

            if iperf_5g:
                speed_5g_index = iperf_5g.find("Mbits") - 4
                if speed_5g_index > 5:
                    speed_5g = int((iperf_5g[speed_5g_index: speed_5g_index + 3]).strip())
                    if speed_5g >= 900:
                        signal_main_ui.refresh_text_browser.emit("WiFi 5G: " + str(speed_5g) + " Mbps")
                    else:
                        signal_main_ui.refresh_text_browser.emit("\nWiFi 2.4G 速度过低, 请重新测试\n")
                        return False
                else:
                    signal_main_ui.refresh_text_browser.emit("WiFi 5G 速度为空, 请重新测试")
                    return False
            else:
                signal_main_ui.refresh_text_browser.emit("WiFi 5G 速度为空, 请重新测试")
                return False

            if iperf_1g:
                speed_1g_index = iperf_1g.find("Mbits") - 4
                if speed_1g_index > 0:
                    speed_1g = int((iperf_1g[speed_1g_index: speed_1g_index + 3]).strip())
                    if speed_1g >= 949:
                        signal_main_ui.refresh_text_browser.emit("LaN  1G: " + str(speed_1g) + " Mbps")
                    else:
                        signal_main_ui.refresh_text_browser.emit("\nLAN 速度过低, 请重新测试\n")
                        return False
                else:
                    signal_main_ui.refresh_text_browser.emit("LAN 速度为空, 请重新测试")
                    return False
            else:
                signal_main_ui.refresh_text_browser.emit("LAN 速度为空, 请重新测试")
                return False

            return True
        else:
            signal_main_ui.refresh_text_browser.emit("Speed test result is NULL，Retest Please")
            return False
