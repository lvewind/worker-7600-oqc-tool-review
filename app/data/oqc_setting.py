from hiworker.storage import Storage


class OqcSetting(Storage):
    """
    不良品列表
    """
    def __init__(self, table):
        super(OqcSetting, self).__init__(table)
        try:
            self.db_add_row({"id": 1})
        except:
            pass

    def set_eth(self, lan_eth, wlan_eth, bridge_ctrl_eth):
        eth = {"lan_eth": lan_eth, "wlan_eth": wlan_eth, "bridge_ctrl_eth": bridge_ctrl_eth}
        return self.db_update_row(eth, "id", 1)

    def set_txt(self, auto_txt, open_after_txt):
        if auto_txt:
            auto_txt = 1
        else:
            auto_txt = 0

        if open_after_txt:
            open_after_txt = 1
        else:
            open_after_txt = 0
        return self.db_update_row({"auto_txt": auto_txt, "open_after_txt": open_after_txt}, "id", 1)

    def set_auto_speed(self, auto_speed):
        if auto_speed:
            auto_speed = 1
        else:
            auto_speed = 0
        return self.db_update_row({"auto_speed": auto_speed}, "id", 1)

    def set_auto_ip_200(self, auto_ip_200):
        if auto_ip_200:
            auto_ip_200 = 1
        else:
            auto_ip_200 = 0
        return self.db_update_row({"auto_ip_200": auto_ip_200}, "id", 1)

    def set_main_ap_ssid(self, main_ap_ssid):
        return self.db_update_row({"main_ap_ssid": main_ap_ssid}, "id", 1)

    def set_main_ap_passwd(self, main_ap_passwd):
        return self.db_update_row({"main_ap_passwd": main_ap_passwd}, "id", 1)

    def get_auto_txt(self):
        return self.db_read_row(1, "id").get("auto_txt")

    def get_auto_ip_200(self):
        return self.db_read_row(1, "id").get("auto_ip_200")

    def get_lan_eth(self):
        return self.db_read_row(1, "id").get("lan_eth")

    def get_wlan_eth(self):
        return self.db_read_row(1, "id").get("wlan_eth")

    def get_bridge_ctrl_eth(self):
        return self.db_read_row(1, "id").get("bridge_ctrl_eth")

    def get_auto_speed(self):
        return self.db_read_row(1, "id").get("auto_speed")

    def get_auto_text(self):
        return self.db_read_row(1, "id").get("auto_txt")

    def get_open_text(self):
        return self.db_read_row(1, "id").get("open_after_txt")

    def get_main_ap_ssid(self):
        return self.db_read_row(1, "id").get("main_ap_ssid")

    def get_main_ap_passwd(self):
        return self.db_read_row(1, "id").get("main_ap_passwd")


oqc_setting = OqcSetting("oqc_setting")
