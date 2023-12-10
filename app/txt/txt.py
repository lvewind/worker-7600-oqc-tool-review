import os
import time
import subprocess
from app.app_signal.app_signal import signal_main_ui, signal_load_table
from app.data.oqc_product_list import oqc_products_list


txt_path = os.path.join(os.getcwd(), "doc")

if not os.path.exists(txt_path):
    os.makedirs(txt_path, exist_ok=True)

bridge_txt_path = os.path.join(os.getcwd(), "bridge")

if not os.path.exists(bridge_txt_path):
    os.makedirs(bridge_txt_path, exist_ok=True)


def dict_to_txt_by_line(result_data_dict: dict, open_when_finished=False, is_bridge=False):
    if not result_data_dict:
        return 0
    day_path = generate_txt_path(result_data_dict, is_bridge)
    if not os.path.exists(day_path):
        os.makedirs(day_path, exist_ok=True)

    sn = result_data_dict.get("sn")

    if sn:
        txt_name = sn + ".txt"
        for key, value in result_data_dict.items():
            if not is_bridge:
                if key in ("main_2_4g_up", "main_5g_up", "main_2_4g_down", "main_5g_down", 
                           "bridge_2_4g_up", "bridge_5g_up", "bridge_2_4g_down", "bridge_5g_down"):
                    continue
            else:
                if key in ("current_version", "usb_power", "wifi_name", "wifi_passwd",
                           "iperf_2g", "iperf_5g", "iperf_1g", "iot", "dhcp", ):
                    continue
            if not value and not is_bridge:
                signal_main_ui.refresh_text_browser.emit(str(key) + " Data is empty, Output fail")
                return
                # signal_main_ui.refresh_text_browser.emit("正在导出：" + txt_name)
        txt_file = os.path.join(day_path, txt_name)

        fw = open(txt_file, "w", encoding="ansi")
        fw.write(str(result_data_dict.get("web_passwd", "\n")))
        fw.write("\n")
        if not is_bridge:
            fw.write(str(result_data_dict.get("current_version", "\n")))
            fw.write("\n")
        fw.write(str(result_data_dict.get("check_sn", "\n")))
        fw.write("\n")
        fw.write(str(result_data_dict.get("mac_addr", "\n")) + "\n")
        if not is_bridge:
            fw.write(str(result_data_dict.get("usb_power", "\n")) + "\n")
            fw.write(str(result_data_dict.get("wifi_passwd", "\n")) + "\n")
            fw.write("\n")
            fw.write("WIFI\n")
            fw.write("2.4G\n")
            fw.write(str(result_data_dict.get("iperf_2g", "\n")) + "\n")

            fw.write("\n")
            fw.write("5G\n")
            fw.write(str(result_data_dict.get("iperf_5g", "\n")) + "\n")

            fw.write("\n")
            fw.write("LAN\n")
            fw.write("1G\n")
            fw.write(str(result_data_dict.get("iperf_1g", "\n")) + "\n")
        else:
            fw.write("\n\n")
            fw.write("main_5g_down: " + str(result_data_dict.get("main_5g_down", "\n")) + "  Mbits/sec\n")
            fw.write("main_5g_up: " + str(result_data_dict.get("main_5g_up", "\n")) + "  Mbits/sec")

            fw.write("\n\n")
            fw.write("bridge_5g_down: " + str(result_data_dict.get("bridge_5g_down", "\n")) + "  Mbits/sec\n")
            fw.write("bridge_5g_up: " + str(result_data_dict.get("bridge_5g_up", "\n")) + "  Mbits/sec")

        fw.close()
        signal_main_ui.refresh_text_browser.emit("\nOutput Success：" + txt_name + "\n")
        oqc_products_list.edit_product({"test_state": 1}, "sn", sn)
        signal_load_table.load_products_list.emit()
        signal_main_ui.set_has_output.emit()

        if open_when_finished:
            try:
                subprocess.Popen(['notepad', txt_file])
            except:
                pass
    else:
        signal_main_ui.refresh_text_browser.emit("\nError: SN lost\n")


def open_txt(target_dict: dict, is_bridge=False):
    day_path = generate_txt_path(target_dict, is_bridge)
    sn = target_dict.get("sn")
    if sn:
        txt_name = sn + ".txt"

        txt_file = os.path.join(day_path, txt_name)
        # signal_main_ui.refresh_text_browser.emit("打开：" + txt_file)
        try:
            subprocess.Popen(['notepad', txt_file])
        except:
            pass


def generate_txt_path(target_dict, is_bridge=False):
    create_time = target_dict.get("create_time")
    if create_time:
        localtime = time.localtime(create_time)
    else:
        localtime = time.localtime(time.time())
    if is_bridge:
        month_path = os.path.join(bridge_txt_path, str(localtime[1]) + "月")
    else:
        month_path = os.path.join(txt_path, str(localtime[1]) + "月")
    return os.path.join(month_path, str(localtime[2]))
