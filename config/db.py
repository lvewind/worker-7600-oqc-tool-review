data_base_sql = [
    """CREATE TABLE oqc_products_list ( 
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    sn text unique, 
                                    mac_addr text, 
                                    web_passwd text, 
                                    wifi_passwd text,
                                    test_state INTEGER,
                                    create_time INTEGER)""",

    """CREATE TABLE oqc_test_result (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    sn text unique,
                                    web_passwd text,
                                    
                                    current_version text,
                                    check_sn text,
                                    mac_addr text,
                                    usb_power text,
                                    wifi_name text,
                                    wifi_passwd text,
                                    
                                    iperf_2g text,
                                    iperf_5g text,
                                    iperf_1g text,
                                    
                                    iot text,
                                    dhcp text,
                                    
                                    main_2_4g_up text,
                                    main_5g_up text,
                                    main_2_4g_down text,
                                    main_5g_down text,
                                    
                                    bridge_2_4g_up text,
                                    bridge_5g_up text,
                                    bridge_2_4g_down text,
                                    bridge_5g_down text,
                                    
                                    create_time INTEGER)""",

    """CREATE TABLE oqc_user (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name text,
                            job_number INTEGER)""",

    """CREATE TABLE oqc_setting (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            lan_eth text,
                            wlan_eth text,
                            bridge_ctrl_eth text,
                            auto_txt INTEGER,
                            open_after_txt INTEGER,
                            auto_speed INTEGER,
                            auto_ip_200 INTEGER,
                            main_ap_ssid text,
                            main_ap_passwd text)"""
]

# 创建数据库连接
db_config = {
    "data_path": "data\\user",
    "db_file_name": "user.db",
    "sql_file_name": "user.sql"
}
