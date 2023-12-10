from PySide6.QtCore import QObject, Signal


class SignalData(QObject):
    add_item = Signal(dict)


class SignalDialog(QObject):
    pass


class SignalLoadTable(QObject):
    load_products_list = Signal()
    find_sn_in_products_list = Signal(str)


class SignalMainUI(QObject):
    refresh_text_browser = Signal(str)
    refresh_text_browser_ping_100 = Signal(str)
    refresh_text_browser_ping_254 = Signal(str)
    refresh_eth = Signal()
    run_iperf3 = Signal()
    set_has_output = Signal()
    check_iot_again = Signal()
    iperf_all = Signal()
    show_message = Signal(str)
    show_input_dialog = Signal()
    save_bridge_ip = Signal(str)


class CloseSelf(QObject):
    close_self = Signal(str)


signal_data = SignalData()
signal_dialog = SignalDialog()
signal_load_table = SignalLoadTable()
signal_main_ui = SignalMainUI()
close_self = CloseSelf()

