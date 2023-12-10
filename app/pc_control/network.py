import hiworker
import subprocess
import re
import pywifi
import time
from pywifi import const
from app.app_signal.app_signal import signal_main_ui


def set_adapter_enable(net_connection_id, enable=True):
    if enable:
        status = "enable"
    else:
        status = "disable"
    subprocess.Popen(["netsh", "interface", "set", "interface", net_connection_id, status],
                     shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    time.sleep(3)


def reconnect_bridge_eth(net_connection_id):
    set_adapter_enable(net_connection_id, enable=False)
    set_adapter_enable(net_connection_id, enable=True)


def check_adapter_on(net_connection_id, set_on=True):
    """
    检测或开启网卡
    :param net_connection_id:
    :param set_on:
    :return:
    """
    if net_connection_id:
        if not hiworker.is_adapter_exist(net_connection_id):
            signal_main_ui.refresh_text_browser.emit("Network adapter：" + net_connection_id + "non-existent")
            return False
    else:
        signal_main_ui.refresh_text_browser.emit("Network adapter does not set")
        return False

    enable_times = 0
    while enable_times <= 3:
        if hiworker.is_adapter_enable(net_connection_id):
            return True
        set_adapter_enable(net_connection_id, set_on)
        enable_times += 1
    else:
        signal_main_ui.refresh_text_browser.emit("Network adapter：" + net_connection_id + "Enable Fail，Try again.")
        return False


def set_adapter_dhcp(net_connection_id: str, net_connection_id_wlan: str, disable_before=True):
    if net_connection_id:
        signal_main_ui.refresh_text_browser.emit("SET DHCP：" + net_connection_id)
    else:
        signal_main_ui.refresh_text_browser.emit("SET DHCP：Failed")

    if disable_before:
        set_adapter_enable(net_connection_id_wlan, False)  # 禁用无线网卡
        set_adapter_enable(net_connection_id, False)  # 禁用有线网卡
        time.sleep(1)
        check_adapter_on(net_connection_id_wlan)  # 启用无线网卡

    if not check_adapter_on(net_connection_id):  # 启用有线网卡， 启用失败则停止
        return 0

    dhcp_times = 0
    while dhcp_times <= 3:
        subprocess.Popen(["netsh", "interface", "ip", "set", "addr", net_connection_id, "dhcp"],
                         shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        if hiworker.is_adapter_dhcp_enabled(net_connection_id):
            signal_main_ui.refresh_text_browser.emit("DHCP：" + net_connection_id + " Successful\n")
            return True
        else:
            dhcp_times += 1
            time.sleep(3)
    else:
        signal_main_ui.refresh_text_browser.emit("DHCP：" + net_connection_id + "Enable Fail，Try again.\n")


def set_adapter_ip_200(net_connection_id):
    signal_main_ui.refresh_text_browser.emit("SET IP 192.168.123.200：" + net_connection_id)
    disconnect_wlan()
    if not check_adapter_on(net_connection_id):
        return 0

    ipv4_times = 0
    while ipv4_times <= 3:
        subprocess.Popen(["netsh", "interface", "ipv4", "set", "address", net_connection_id,
                          "static", "192.168.123.200", "255.255.255.0"], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ipv4_times += 1
        time.sleep(1)
        if hiworker.get_adapter_ipv4(net_connection_id) == "192.168.123.200":
            signal_main_ui.refresh_text_browser.emit("SET IP 192.168.123.200：成功\n")
            break
    else:
        signal_main_ui.refresh_text_browser.emit("SET IP 192.168.123.200：Failed，Retry Please\n")


def renew_dhcp(net_connection_id):
    subprocess.Popen(["ipconfig", "/renew", net_connection_id],
                     shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def ping_server(ip_addr: str):
    p = subprocess.Popen(["ping", ip_addr, "-t"],
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    for line in p.stdout:
        line = line.decode(encoding="ansi")
        line = line.strip("\r\n")
        if "100" in ip_addr:
            signal_main_ui.refresh_text_browser_ping_100.emit(line)
        else:
            signal_main_ui.refresh_text_browser_ping_254.emit(line)
    p.stdout.close()


def ping_bridge(ip_addr: str, ok_times: int, max_times: int, threshold: int):
    if not ip_addr:
        ip_addr = "192.168.123.254"
    ping_times = 0
    ping_time = []
    p = subprocess.Popen(["ping", ip_addr, "-t"],
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    for line in p.stdout:
        line = line.decode(encoding="ansi")
        line = line.strip("\r\n")
        signal_main_ui.refresh_text_browser.emit(str(line))
        ok_ping = re.search(r'\d*ms', line, re.I)
        if ok_ping:
            ping_ms = ok_ping.group()
            ping_ms = int(ping_ms[0:-2])
            if ping_ms <= threshold:
                ping_time.append(ping_ms)
            else:
                ping_time = []
        else:
            ping_time = []
        if len(ping_time) >= ok_times:
            p.kill()
            return True
        if ping_times >= max_times:
            return False
        else:
            ping_times += 1
    p.stdout.close()
    return False


def disconnect_wlan():
    subprocess.Popen(["netsh", "wlan", "disconnect"],
                     shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    time.sleep(1)


def connect_wlan(wifi_name: str):
    subprocess.Popen(["netsh", "wlan", "connect", "name=" + wifi_name],
                     shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def delete_wlan_all_profile():
    wlan_profile_list = []
    p = subprocess.Popen(["netsh", "wlan", "show", "profile"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in p.stdout:
        if not line:
            continue
        line = line.decode(encoding="ansi")
        line = line.strip("\r\n")
        index = line.find("U+Net")
        if not index == -1:
            wlan_profile_list.append(line[index:].strip())
    time.sleep(1)
    if wlan_profile_list:
        for wifi_name in wlan_profile_list:
            subprocess.Popen(["netsh", "wlan", "delete", "profile", "name=" + wifi_name],
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            time.sleep(1)


class ConnectWifi(hiworker.Thread):
    def __init__(self):
        super(ConnectWifi, self).__init__()
        self.wifi_name = ""
        self.passwd = ""
        self.wifi = pywifi.PyWiFi()
        self.wlan_eth = ""
        self.connect_status = False

    def run(self) -> None:
        self.connect_wifi()

    def connect_wifi(self):
        if not check_adapter_on(self.wlan_eth):
            return 0
        signal_main_ui.refresh_text_browser.emit("连接: " + self.wifi_name)
        self.connect_status = False
        try:
            iface = self.wifi.interfaces()[0]
            time.sleep(1)
            assert iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
            profile = pywifi.Profile()
            profile.ssid = self.wifi_name
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = self.passwd
            tmp_profile = iface.add_network_profile(profile)
            signal_main_ui.refresh_text_browser.emit("Connecting...")
            iface.connect(tmp_profile)
            connect_time = 0
            while connect_time < 5:
                time.sleep(1)
                connect_time += 1
                if iface.status() == const.IFACE_CONNECTED:
                    self.connect_status = True
                    signal_main_ui.refresh_text_browser.emit("Connect Successful")
                    return True
            else:
                self.connect_status = False
                signal_main_ui.refresh_text_browser.emit("Connect time out，Retry Please")
                return False
        except IndexError:
            signal_main_ui.refresh_text_browser.emit("Wireless LAN is disabled.")

    def delete_all_profile(self):
        try:
            iface = self.wifi.interfaces()[0]
            iface.remove_all_network_profiles()
        except IndexError:
            signal_main_ui.refresh_text_browser.emit("Network adapter is disabled")

    def set_wifi_args(self, wifi_name: str, passwd: str, wlan_eth):
        self.wifi_name = wifi_name
        self.passwd = passwd
        self.wlan_eth = wlan_eth
