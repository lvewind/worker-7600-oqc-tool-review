from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium.common
import time
import os
from app.app_signal.app_signal import *
from app.data import oqc_test_result
from app.pc_control.network import ping_bridge
from hiworker.win32.handle import Win32Handle
import win32gui
from pywintypes import error as pywintypes_error


class LGU7600Driver:
    """
    LGU+ GAPK-7600
    Chrome Legacy WindowLGU+ GAPK-7600 - Google Chrome
    """
    def __init__(self, bin_path="bin", driver_file="chromedriver.exe"):
        self.driver_url = os.path.join(os.path.abspath(os.getcwd()), bin_path, driver_file)
        self.login_success = "로그인 후 비정상 종료(로그아웃버튼 사용하지 않은 경우)하면 10분 이내에 재접속이 불가능하오니 로그아웃버튼으로 종료 바랍니다."
        self.no_passwd = "패스워드를 입력해 주세요."
        self.no_p_code = "보안문자를 입력해 주세요."
        self.login_failed = "로그인에 실패하였습니다. 패스워드 또는 보안문자를 다시 확인하세요."
        self.have_login = "다른사용자가 로그인 중이므로 로그인하실수 없습니다."
        self.driver = ""
        self.sn = ""
        self.mac_addr = ""
        self.web_passwd = ""
        self.wifi_passwd = ""
        self.stop = False

        self.main_ap_ssid = ""

        self.skip_reset = False
        
    def init_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('window-size=1000,1000')
            return webdriver.Chrome(executable_path=self.driver_url, options=options)

        except selenium.common.exceptions.SessionNotCreatedException as e:
            print(e)

    def set_product(self, product: dict):
        self.sn = product.get("sn")
        self.mac_addr = product.get("mac_addr")
        self.web_passwd = product.get("web_passwd")
        self.wifi_passwd = product.get("wifi_passwd")
        # print(self.sn, self.mac_addr, self.web_passwd, self.wifi_passwd)

    def check_ui(self, test_speed: bool, only_open=False):
        chrome_driver = self.init_driver()
        if self.open_web_page(chrome_driver):
            if not only_open:
                if not self.check_dhcp(chrome_driver):
                    signal_main_ui.refresh_text_browser.emit("DHCP异常, 请重试")
                    self.logout_web(chrome_driver, 5)
                self.get_mac_addr_sn_version(chrome_driver)
                self.set_wifi(chrome_driver)
                if self.check_iot(chrome_driver):

                    signal_main_ui.refresh_text_browser.emit("UI 信息检测完成, 正在退出登录")
                    self.logout_web(chrome_driver, 5)

                    if test_speed:
                        signal_main_ui.refresh_text_browser.emit("开启测速...")
                        signal_main_ui.iperf_all.emit()

            else:
                signal_main_ui.refresh_text_browser.emit("当前为仅打开页面, 进行自动检测前请先关闭该浏览器窗口.")
        else:
            signal_main_ui.refresh_text_browser.emit("页面打开失败,请重试")
            chrome_driver.quit()

    def config_bridge(self, only_open=False, show_input=True):
        chrome_driver = self.init_driver()
        if self.open_bridge_page(chrome_driver):
            if not only_open:
                if not self.config_bridge_5g(chrome_driver):
                    signal_main_ui.refresh_text_browser.emit("5G SSID 设置失败")
                else:
                    signal_main_ui.refresh_text_browser.emit("5G SSID 设置成功， 等待页面响应")
                    time.sleep(35)
                    if self.logout_web(chrome_driver, 5):
                        if show_input:
                            signal_main_ui.refresh_text_browser.emit("浏览器已关闭, 可以进行测速")
                            signal_main_ui.show_input_dialog.emit()
                        return True

            else:
                signal_main_ui.refresh_text_browser.emit("当前为仅打开页面, 进行自动检测前请先关闭该浏览器窗口")
        else:
            signal_main_ui.refresh_text_browser.emit("页面打开失败,请重试")
            chrome_driver.quit()

    def open_web_page(self, chrome_driver: webdriver.Chrome):
        if self.sn:
            try:
                signal_main_ui.refresh_text_browser.emit("GET 192.168.123.254")
                handles = chrome_driver.window_handles
                chrome_driver.switch_to.window(handles[0])
                url = "http://192.168.123.254/"
                # url = "http://cn.bing.com"
                chrome_driver.get(url)
                chrome_driver.switch_to.default_content()
                # 切换frame
                chrome_driver.switch_to.frame("index")
                try:
                    index_menu = chrome_driver.find_element_by_id("gnb1")
                    if index_menu.is_displayed():
                        signal_main_ui.refresh_text_browser.emit("\nLogin")
                        return True
                except selenium.common.exceptions.NoSuchElementException:
                    pass

                mac_1 = chrome_driver.find_element_by_id("1depth_mac").text
                if not mac_1 == self.mac_addr_decode(self.mac_addr):
                    signal_main_ui.refresh_text_browser.emit("\nCurrent AP is NOT the same with Current Item.")
                    return
                # 打开登陆界面
                chrome_driver.find_element_by_id("ID_internetCk_2depth_click").click()
                time.sleep(1)
                if self.input_web_passwd(chrome_driver, self.web_passwd, wait_passwd=0.1):
                    return True
                else:
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

    def open_bridge_page(self, chrome_driver: webdriver.Chrome):
        if self.sn:
            signal_main_ui.refresh_text_browser.emit("GET 192.168.123.254")
            url = "http://192.168.123.254/"
            # 打开bridge界面
            signal_main_ui.refresh_text_browser.emit("打开桥接页面入口")
            self.stop = False
            bridge_button_confirm = 0
            for t in range(1, 80):
                if self.stop:
                    return
                try:
                    chrome_driver.get(url)
                    chrome_driver.switch_to.default_content()
                    # 切换frame
                    chrome_driver.switch_to.frame("index")
                    main_ap_mac = chrome_driver.find_element_by_id("1depth_mac").text
                    if main_ap_mac:
                        self.main_ap_ssid = "U+Net" + str(main_ap_mac[-5]) + str(main_ap_mac[-4]) + str(main_ap_mac[-2]) + str(main_ap_mac[-1])
                        bridge_button = chrome_driver.find_element_by_xpath('//*[@id="ID_2depth01"]/a')
                        if bridge_button.is_displayed():
                            bridge_button_confirm += 1
                        if bridge_button_confirm >= 2:
                            bridge_button.click()
                            break
                        else:
                            signal_main_ui.refresh_text_browser.emit("等待桥接..." + str(t))
                except selenium.common.exceptions.NoSuchElementException:
                    signal_main_ui.refresh_text_browser.emit("等待桥接..." + str(t))
                except selenium.common.exceptions.ElementNotInteractableException:
                    signal_main_ui.refresh_text_browser.emit("等待桥接..." + str(t))
                except selenium.common.exceptions.WebDriverException as e:
                    signal_main_ui.refresh_text_browser.emit(str(e))
                    return
                time.sleep(3)
            else:
                signal_main_ui.refresh_text_browser.emit("桥接超时, 请重试")
                return

            handles = chrome_driver.window_handles
            chrome_driver.switch_to.window(handles[1])
            try:
                chrome_driver.switch_to.default_content()
                # 切换frame
                chrome_driver.switch_to.frame("index")
                # try:
                #     external_ip = chrome_driver.find_element_by_id("external_ip")
                #     if external_ip.is_displayed():
                #         external_ip = external_ip.text
                #         if external_ip:
                #             signal_main_ui.save_bridge_ip.emit(external_ip)
                #             ping_bridge(external_ip, ok_times=5, max_times=24, threshold=5)
                #
                # except selenium.common.exceptions.NoSuchElementException as e:
                #     pass

                try:
                    index_menu = chrome_driver.find_element_by_id("gnb1")
                    if index_menu.is_displayed():
                        signal_main_ui.refresh_text_browser.emit("\nLogin")
                        return True
                except selenium.common.exceptions.NoSuchElementException as e:
                    print("No Login" + str(e))
                    try:
                        mac_1 = chrome_driver.find_element_by_id("1depth_mac").text
                        if not mac_1 == self.mac_addr_decode(self.mac_addr):
                            signal_main_ui.refresh_text_browser.emit("\nCurrent AP is NOT the same with Current Item.")
                            return
                        else:
                            chrome_driver.find_element_by_xpath('//*[@id="1depth_dummyimg"]').click()
                            if self.input_web_passwd(chrome_driver, self.web_passwd):
                                return True
                            else:
                                return False
                    except selenium.common.exceptions.NoSuchElementException as e:
                        print(e)
            except selenium.common.exceptions.NoSuchFrameException as e:
                print(e)
            except selenium.common.exceptions.NoSuchWindowException as e:
                print(e)

    @staticmethod
    def logout_web(chrome_driver: webdriver.Chrome, wait_time: int):
        signal_main_ui.refresh_text_browser.emit("退出登录")
        for t in range(10):
            try:
                logout = chrome_driver.find_element_by_xpath('//*[@id="header_container"]/ul[2]/li[2]/form/div/a/div')
                logout.click()
                time.sleep(0.5)
            except selenium.common.exceptions.NoSuchElementException as e:
                print(e)

            try:
                alert_popup_yes = chrome_driver.find_element_by_id("alert_popup_yes")
                if alert_popup_yes.is_displayed():
                    alert_popup_yes.click()
                    signal_main_ui.refresh_text_browser.emit("退出成功,等待关闭浏览器")
                    for i in range(wait_time):
                        time.sleep(1)
                        signal_main_ui.refresh_text_browser.emit(str(wait_time - i))
                    chrome_driver.quit()
                    return True
            except selenium.common.exceptions.NoSuchElementException as e:
                print(e)

            time.sleep(0.5)
        else:
            print("Time out to Logout")
            return

    def input_web_passwd(self, chrome_driver: webdriver.Chrome, passwd: str, wait_passwd=0.7):
        try:
            signal_main_ui.refresh_text_browser.emit("Set Top Browser Window")
            win_hwnd = Win32Handle()
            win_hwnd.set_handle_option(correction_window=False)
            hwnd = win_hwnd.get_handle("LGU+ GAPK-7600 - Google Chrome")
            win32gui.SetForegroundWindow(hwnd)
        except pywintypes_error:
            signal_main_ui.refresh_text_browser.emit("Browser Window Set Top Failed.")

        if not passwd:
            signal_main_ui.refresh_text_browser.emit("Current Item Passwd is Empty，Please Check it !”")
            return False
        else:
            signal_main_ui.refresh_text_browser.emit("Input Password...")
            el_input_passwd = chrome_driver.find_element_by_id("password")
            if not el_input_passwd.is_displayed():
                signal_main_ui.refresh_text_browser.emit("Input Password Failed， Retry Please")
                return False
            else:
                # el_input_passwd.send_keys(passwd)
                time.sleep(wait_passwd)
                el_input_passwd.send_keys(passwd)
                signal_main_ui.refresh_text_browser.emit("Input Password Successful")
                signal_main_ui.refresh_text_browser.emit("Waiting CAPTCHA")
                chrome_driver.find_element_by_id("pcode").click()
                p_codes = ""
                check_p_code_time = 0
                while len(p_codes) < 5:
                    el_p_code_input = chrome_driver.find_element_by_id("pcode")
                    p_codes = el_p_code_input.get_attribute("value")
                    time.sleep(0.2)
                    check_p_code_time += 0.2
                    if check_p_code_time >= 100:
                        signal_main_ui.refresh_text_browser.emit("Input CAPTCHA timeout，Retry Please")
                        return False
                else:
                    p_codes_lower = p_codes.lower()
                    signal_main_ui.refresh_text_browser.emit("CAPTCHA：" + p_codes_lower)
                    chrome_driver.find_element_by_id("pcode").clear()
                    chrome_driver.find_element_by_id("pcode").send_keys(p_codes_lower)
                    signal_main_ui.refresh_text_browser.emit("Login...")
                    chrome_driver.find_element_by_id("ID_btn_login").click()
                    alert_popup_msg = chrome_driver.find_element_by_id("alert_popup_msg")
                    wait_pop_msg_time = 0
                    while not alert_popup_msg.is_displayed():
                        time.sleep(0.2)
                        wait_pop_msg_time += 0.2
                        if wait_pop_msg_time >= 100:
                            signal_main_ui.refresh_text_browser.emit("Login timeout， Retry Please")
                            return False
                    else:
                        alert_popup_msg_text = alert_popup_msg.text
                        if self.login_success in alert_popup_msg_text:
                            signal_main_ui.refresh_text_browser.emit("Login Successful\n")
                            chrome_driver.find_element_by_id("alert_popup_close").click()
                            return True
                        else:
                            if self.no_passwd in alert_popup_msg_text:
                                signal_main_ui.refresh_text_browser.emit("Click Open WEB button Please.")
                            elif self.no_p_code in alert_popup_msg_text:
                                signal_main_ui.refresh_text_browser.emit("Waiting CAPTCHA.")
                            elif self.login_failed in alert_popup_msg_text:
                                signal_main_ui.refresh_text_browser.emit("Login Failed, Passwd or CAPTCHA is wrong")
                            elif self.have_login in alert_popup_msg_text:
                                signal_main_ui.refresh_text_browser.emit("Login Failed, Other client login.")
                            try:
                                chrome_driver.find_element_by_id("alert_popup_close").click()
                            except selenium.common.exceptions.ElementNotInteractableException as e:
                                print(e)
                            return False

    def config_bridge_5g(self, chrome_driver: webdriver.Chrome):
        if self.is_home_page(chrome_driver):
            for t in range(6):
                try:
                    button_5g = chrome_driver.find_element_by_xpath(
                        '//*[@id="container_main"]/ul/li/div[2]/ul/li/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/table/tbody/tr/td[1]/div[3]/a/div')
                    if button_5g.is_displayed():
                        button_5g.click()
                        time.sleep(1)
                        break
                except selenium.common.exceptions.NoSuchElementException as e:
                    print(e)
                time.sleep(0.5)
            else:
                print("Time out to find element")
                return

            for t in range(6):
                try:
                    ssid = chrome_driver.find_element_by_id("ssid")
                    if not ssid.is_displayed():
                        continue
                    ssid.clear()
                    ssid.send_keys(self.main_ap_ssid + "_5G_bridge")
                    button_apply = chrome_driver.find_element_by_id("applyWireless")
                    if button_apply.is_displayed():
                        button_apply.click()
                        return True
                except selenium.common.exceptions.NoSuchElementException:
                    time.sleep(0.5)
            else:
                print("Time out to Set SSID 5G")
                return
        else:
            signal_main_ui.refresh_text_browser.emit("页面异常，请重试")

    def config_bridge_2_4g(self, chrome_driver: webdriver.Chrome):
        if self.is_home_page(chrome_driver):
            for t in range(6):
                try:
                    button_2_4g = chrome_driver.find_element_by_xpath(
                        '//*[@id="container_main"]/ul/li/div[2]/ul/li/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr/td[1]/div[3]/a/div')
                    if button_2_4g.is_displayed():
                        button_2_4g.click()
                        time.sleep(1.5)
                        break
                except selenium.common.exceptions.NoSuchElementException as e:
                    print(e)
                time.sleep(0.5)
            else:
                print("Time out to find element")
                return
            for t in range(6):
                try:
                    ssid = chrome_driver.find_element_by_id("ssid")
                    if not ssid.is_displayed():
                        continue
                    ssid.clear()
                    ssid.send_keys(self.main_ap_ssid + "_bridge")
                    if self.set_wifi(chrome_driver, init=False):
                        # chrome_driver.find_element_by_id("applyWireless").click()
                        return True
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    time.sleep(0.5)
                    continue
            else:
                print("Time out to set SSID 2.4G")
                return
        else:
            signal_main_ui.refresh_text_browser.emit("页面异常，请重试")

    @staticmethod
    def is_home_page(chrome_driver: webdriver.Chrome):
        time.sleep(1)
        for t in range(6):
            try:
                iot_text = chrome_driver.find_element_by_id("iot_text")
                if iot_text.is_displayed():
                    return True
            except selenium.common.exceptions.NoSuchElementException as e:
                print(e)
                try:
                    home = chrome_driver.find_element_by_id("gnb1")
                    home.click()
                    time.sleep(0.5)
                except selenium.common.exceptions.NoSuchElementException as e:
                    print(e)
            time.sleep(0.5)
        else:
            print("Time out to find element")
            return

    def reset_bridge(self):
        chrome_driver = self.init_driver()
        self.skip_reset = False
        if self.open_bridge_page(chrome_driver):
            self.hover(chrome_driver, "id", "gnb4")
            system_a = chrome_driver.find_element_by_id("System_a")
            if system_a.is_displayed():
                system_a.click()
                time.sleep(1)
            id_btn_reset = chrome_driver.find_element_by_id("ID_btn_reset")
            if id_btn_reset.is_displayed():
                id_btn_reset.click()
                time.sleep(1)
            id_btn_reset_yes = chrome_driver.find_element_by_id("ID_btn_reset_yes")
            if id_btn_reset_yes.is_displayed():
                id_btn_reset_yes.click()
                reset_time = 0
                for t in range(70):
                    signal_main_ui.refresh_text_browser.emit("等待重置: " + str(70 - reset_time))
                    time.sleep(1)
                    reset_time += 1
                    if self.skip_reset:
                        signal_main_ui.refresh_text_browser.emit("已跳过重置倒计时!")
                        break
                else:
                    pass
            else:
                signal_main_ui.refresh_text_browser.emit("重置失败,请重试!")
            signal_main_ui.refresh_text_browser.emit("重置完成.")
        else:
            signal_main_ui.refresh_text_browser.emit("重置失败,请重试!")
        time.sleep(3)
        chrome_driver.quit()

    def skip_reset_bridge(self):
        self.skip_reset = True

    def check_log(self, chrome_driver: webdriver.Chrome):
        try:
            self.hover(chrome_driver, "id", "gnb2")
            chrome_driver.find_element_by_id("SystemLog_a").click()
            log_content = chrome_driver.find_element_by_id("ID_logcontents")
            log_list = log_content.find_elements_by_tag_name("td")
            g5_times = 0
            g2_times = 0
            for ele in log_list:
                if "5GHz" in ele.text:
                    g5_times += 1
                elif "2.4GHz" in ele.text:
                    g2_times += 1
                if g2_times > 1 or g5_times > 1:
                    signal_main_ui.refresh_text_browser.emit("Log dose not Reset")
                    break
            else:
                signal_main_ui.refresh_text_browser.emit("Log Reset OK")
        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
    
    def check_dhcp(self, chrome_driver: webdriver.Chrome):
        try:
            self.hover(chrome_driver, "id", "gnb2")
            chrome_driver.find_element_by_id("DHCP_a").click()
            dhcp_table = chrome_driver.find_element_by_id("ID_client_list")
            td_list = dhcp_table.find_elements_by_tag_name("td")
            for ele in td_list:
                if ele.text == "192.168.123.100":
                    signal_main_ui.refresh_text_browser.emit("DHCP OK " + ele.text)
                    oqc_test_result.oqc_result.update_row({"dhcp": "OK"}, "sn", self.sn)
                    return True
            else:
                signal_main_ui.refresh_text_browser.emit("DHCP error")
        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
    
    def check_iot(self, chrome_driver: webdriver.Chrome):
        for i in range(5):
            signal_main_ui.refresh_text_browser.emit("Prepare IoT..." + str(5 - i) + "\n")
            time.sleep(1)
        for i in range(5):
            signal_main_ui.refresh_text_browser.emit("检测 IoT...\n")
            time.sleep(2)
            try:
                chrome_driver.find_element_by_id("gnb1").click()
                iot_info = chrome_driver.find_element_by_id("iot_text").text
                if "0.0.0" in iot_info:
                    signal_main_ui.refresh_text_browser.emit("IoT OK...\n")
                    oqc_test_result.oqc_result.update_row({"iot": "OK"}, "sn", self.sn)
                    signal_load_table.load_products_list.emit()
                    return True
                else:
                    pass
            except selenium.common.exceptions.ElementNotInteractableException:
                signal_main_ui.refresh_text_browser.emit("IoT 异常\n")
            except selenium.common.exceptions.NoSuchElementException:
                signal_main_ui.refresh_text_browser.emit("IoT 异常\n")
            except selenium.common.exceptions.WebDriverException:
                signal_main_ui.refresh_text_browser.emit("IoT 异常\n")

        else:
            signal_main_ui.refresh_text_browser.emit("IoT 检测失败，请重试.\n")
            return False
    
    def get_mac_addr_sn_version(self, chrome_driver: webdriver.Chrome):
        try:
            self.hover(chrome_driver, "id", "gnb2")
            chrome_driver.find_element_by_id("span_Internet").click()
            ver = chrome_driver.find_element_by_id("current_version").text
            sn = chrome_driver.find_element_by_id("serial_number").text
            mac_addr = chrome_driver.find_element_by_id("mac").text

            if ver:
                oqc_test_result.oqc_result.update_row({"current_version": ver}, "sn", self.sn)
                signal_main_ui.refresh_text_browser.emit("version OK：" + ver)

            if sn == self.sn:
                oqc_test_result.oqc_result.update_row({"check_sn": sn}, "sn", self.sn)
                signal_main_ui.refresh_text_browser.emit("SN OK： " + sn)

            if mac_addr == self.mac_addr_decode(self.mac_addr):
                oqc_test_result.oqc_result.update_row({"mac_addr": mac_addr}, "sn", self.sn)
                signal_main_ui.refresh_text_browser.emit("MAC OK：" + mac_addr)

            oqc_test_result.oqc_result.update_row({"web_passwd": self.web_passwd,
                                                   "wifi_passwd": self.wifi_passwd,
                                                   "create_time": int(time.time())}, "sn", self.sn)

            signal_main_ui.refresh_text_browser.emit("\n")
            signal_main_ui.refresh_text_browser.emit(self.web_passwd)
            signal_main_ui.refresh_text_browser.emit(ver)
            signal_main_ui.refresh_text_browser.emit(sn)
            signal_main_ui.refresh_text_browser.emit(mac_addr)
            signal_main_ui.refresh_text_browser.emit(self.wifi_passwd)
            signal_main_ui.refresh_text_browser.emit("\n")

        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
    
    def set_wifi(self, chrome_driver: webdriver.Chrome, init=True):
        try:
            if init:
                self.hover(chrome_driver, "id", "gnb3")
                chrome_driver.find_element_by_id("wireless_a").click()
                time.sleep(1)
            ssid_2g = chrome_driver.find_element_by_id("ssid").get_attribute("value")
            signal_main_ui.refresh_text_browser.emit("WIFI名称：" + ssid_2g)
            oqc_test_result.oqc_result.update_row({"wifi_name": ssid_2g}, "sn", self.sn)

            if not chrome_driver.find_element_by_id("channel").is_enabled():
                chrome_driver.find_element_by_id("channelMode").click()
            signal_main_ui.refresh_text_browser.emit("SET Channel 13")
            select = Select(chrome_driver.find_element_by_id("channel"))
            select.select_by_visible_text("13")

            chrome_driver.find_element_by_xpath('//*[@id="ID_highsettitle"]/ul/li/table/tbody/tr/td').click()
            signal_main_ui.refresh_text_browser.emit("SET Bandwidth 40MHz")
            select = Select(chrome_driver.find_element_by_id("bwCap"))
            select.select_by_visible_text("40 MHz")
            signal_main_ui.refresh_text_browser.emit("SET： sideband Upper")
            select = Select(chrome_driver.find_element_by_id("ctrlsb"))
            select.select_by_visible_text("Upper")
            signal_main_ui.refresh_text_browser.emit("SAVE： WIFI Setting\n")
            chrome_driver.find_element_by_id("applyWireless").click()
            return True
        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)

    def main_ap_wps(self):
        pass

    @staticmethod
    def hover(chrome_driver: webdriver.Chrome, by, value):
        try:
            element = chrome_driver.find_element(by, value)
            webdriver.ActionChains(chrome_driver).move_to_element(element).perform()
        except selenium.common.exceptions.ElementNotInteractableException:
            print("error in: check_web_ui_info")
        except selenium.common.exceptions.NoSuchElementException:
            pass

    @staticmethod
    def mac_addr_decode(input_mac_addr: str):
        mac_1 = input_mac_addr.replace(".", "")
        n = 2
        mac_l = []
        for i, _ in enumerate(mac_1):
            if i % n == 0:
                mac_l.append(mac_1[i:i + n])
            i += n
        return ":".join(mac_l)
