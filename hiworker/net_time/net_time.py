import http.client
import time
import socket


def get_web_server_time(host):
    stime = 0
    try:
        conn = http.client.HTTPConnection(host)
        conn.request("GET", "/")
        r = conn.getresponse()
        # r.getheaders() #获取所有的http头
        ts = r.getheader('date')  # 获取http头date部分
        # 将GMT时间转换成北京时间
        ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        # print("ltime: ", ltime)
        ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
        # print("ttime: ", ttime)
        stime = time.mktime(ltime) + 8 * 60 * 60
        # print("stime: ", stime)
        # print("local_time: ", time.time())
    except socket.gaierror:
        pass

    return int(stime)
