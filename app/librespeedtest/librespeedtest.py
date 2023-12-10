from selenium import webdriver
import selenium.common
import time
import os
from app.app_signal.app_signal import *
from app.data import oqc_test_result, oqc_setting, oqc_products_list
from app.pc_control.network import ConnectWifi, set_adapter_enable
from ..txt.txt import dict_to_txt_by_line


class LibreSpeedTest:
    """
    Auto LibreSpeedTest
    """
    def __init__(self, bin_path="bin", driver_file="chromedriver.exe"):
        self.driver_url = os.path.join(os.path.abspath(os.getcwd()), bin_path, driver_file)
        self.sn = ""
        self.mac_addr = ""
        self.connect_wifi = ConnectWifi()
        self.stop = False

    def start_speed_test(self, current_product: dict, wlan_eth: str, lan_eth: str):
        # if ping_bridge(bridge_ip, ok_times=10, max_times=24, threshold=5):
        signal_main_ui.refresh_text_browser.emit("开始LIBRE SPEED TEST")
        self.set_product(current_product)
        if self.sn:
            main_ap_ssid = oqc_setting.get_main_ap_ssid()
            main_ap_passwd = oqc_setting.get_main_ap_passwd()
            set_adapter_enable(lan_eth, enable=False)
            test_result = oqc_test_result.oqc_result.read_result("sn", self.sn)

            main_5g_down = int(test_result.get("main_5g_down")) if test_result.get("main_5g_down") else 0
            main_5g_up = int(test_result.get("main_5g_up")) if test_result.get("main_5g_up") else 0
            bridge_5g_down = int(test_result.get("bridge_5g_down")) if test_result.get("bridge_5g_down") else 0
            bridge_5g_up = int(test_result.get("bridge_5g_up")) if test_result.get("bridge_5g_up") else 0
            speed_test_result = {
                "main_5g_down": main_5g_down,
                "main_5g_up": main_5g_up,
                "bridge_5g_down": bridge_5g_down,
                "bridge_5g_up": bridge_5g_up
            }
            # MAIN AP
            if (main_5g_down and main_5g_up) and (main_5g_down > 600 and main_5g_up > 350):
                signal_main_ui.refresh_text_browser.emit("跳过 MAIN AP")
            else:
                self.connect_wifi.delete_all_profile()
                self.connect_wifi.set_wifi_args(main_ap_ssid, main_ap_passwd, wlan_eth)
                if self.connect_wifi.connect_wifi():
                    for t in range(3):
                        time.sleep(1)
                        signal_main_ui.refresh_text_browser.emit(str(3-t))
                    main_5g_result = self.libre_speed_test()
                    if not main_5g_result:
                        signal_main_ui.refresh_text_browser.emit("MAIN AP 测速失败")
                        return
                    else:
                        speed_test_result.update({
                            "main_5g_down": main_5g_result[0],
                            "main_5g_up": main_5g_result[1]
                        })
                        oqc_test_result.oqc_result.edit_result(speed_test_result, "sn", self.sn)
                else:
                    return

            # BRIDGE AP
            if (bridge_5g_down and bridge_5g_up) and (bridge_5g_down > 350 and bridge_5g_up > 280):
                signal_main_ui.refresh_text_browser.emit("跳过 BRIDGE AP")
            else:
                self.connect_wifi.delete_all_profile()
                self.connect_wifi.set_wifi_args(str(main_ap_ssid) + "_bridge", main_ap_passwd, wlan_eth)
                if self.connect_wifi.connect_wifi():
                    for t in range(3):
                        time.sleep(1)
                        signal_main_ui.refresh_text_browser.emit(str(3-t))
                    bridge_5g_result = self.libre_speed_test()
                    if not bridge_5g_result:
                        signal_main_ui.refresh_text_browser.emit("BRIDGE AP 测速失败")
                        return
                else:
                    return
                speed_test_result.update({
                    "bridge_5g_down": bridge_5g_result[0],
                    "bridge_5g_up": bridge_5g_result[1]
                })
                oqc_test_result.oqc_result.edit_result(speed_test_result, "sn", self.sn)
            self.connect_wifi.delete_all_profile()
            if speed_test_result.get("main_5g_down") > 600 and speed_test_result.get("main_5g_up") > 350:
                if speed_test_result.get("bridge_5g_down") > 350 and speed_test_result.get("bridge_5g_up") > 280:
                    signal_main_ui.refresh_text_browser.emit("\nBridge Speed Test Save: " + self.sn)
                    for key, value in speed_test_result.items():
                        if key == "sn":
                            continue
                        signal_main_ui.refresh_text_browser.emit(key + ": " + str(value) + " Mbits/sec")
                    signal_load_table.load_products_list.emit()
                    product = oqc_products_list.db_read_row(refer_value=self.sn, refer="sn")
                    speed_test_result.update({"web_passwd": product.get("web_passwd"),
                                              "check_sn": self.sn,
                                              "sn": self.sn,
                                              "mac_addr": product.get("mac_addr"),
                                              "create_time": product.get("create_time")})
                    dict_to_txt_by_line(speed_test_result, open_when_finished=True, is_bridge=True)
                else:
                    signal_main_ui.refresh_text_browser.emit("\nbridge_5g_down: " +
                                                             str(speed_test_result.get("bridge_5g_down")) +
                                                             "\nbridge_5g_up: " +
                                                             str(speed_test_result.get("bridge_5g_up")) +
                                                             "\n请重启AP后再次测试")
            else:
                signal_main_ui.refresh_text_browser.emit("\nmain_5g_down: " +
                                                         str(speed_test_result.get("main_5g_down")) +
                                                         "\nmain_5g_up: " +
                                                         str(speed_test_result.get("main_5g_up")) +
                                                         "\n请重启AP后再次测试")
        # else:
        #     signal_main_ui.refresh_text_browser.emit("BRIDGE AP 不稳定, 请重试")

    def set_product(self, product: dict):
        self.sn = product.get("sn")
        self.mac_addr = product.get("mac_addr")

    def libre_speed_test(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('window-size=800,900')
            chrome_driver = webdriver.Chrome(executable_path=self.driver_url, options=options)
        except selenium.common.exceptions.SessionNotCreatedException as e:
            print(e)
            return
        try:
            signal_main_ui.refresh_text_browser.emit("GET 192.168.0.100")
            handles = chrome_driver.window_handles
            chrome_driver.switch_to.window(handles[0])
            url = "http://192.168.0.100/"
            # url = "http://cn.bing.com"
            chrome_driver.get(url)
            time.sleep(1)
            chrome_driver.switch_to.default_content()
            start_stop_btn = chrome_driver.find_element_by_id("startStopBtn")
            start_stop_btn.click()
            time.sleep(1)
            if not start_stop_btn.get_attribute("class"):
                signal_main_ui.refresh_text_browser.emit("测速启动失败")
                chrome_driver.quit()
                return
            self.stop = False
            for t in range(20):
                if self.stop:
                    signal_main_ui.refresh_text_browser.emit("已终止")
                    return
                if start_stop_btn.get_attribute("class"):
                    signal_main_ui.refresh_text_browser.emit("正在测速" + str(20 - t))
                    time.sleep(1)
                else:
                    break
            download = chrome_driver.find_element_by_id("dlText")
            upload = chrome_driver.find_element_by_id("ulText")
            download_value = int(float(download.text))
            upload_value = int(float(upload.text))
            if download_value and upload_value:
                signal_main_ui.refresh_text_browser.emit("测速完成")
                chrome_driver.quit()
                return download_value, upload_value
            else:
                signal_main_ui.refresh_text_browser.emit("测速出错, 请重试")
                return False
        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
            return False
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            return False
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
            return False
