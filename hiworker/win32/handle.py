# -*- coding: UTF-8 -*-
import win32gui
import win32con
import win32api
import time


class Win32Handle(object):
    def __init__(self):
        self.correction_window_position = [8, 8, 1152, 679]
        self.correction_client_rect = [0, 0, 1136, 640]
        self.inside_correction_rect = []
        self.is_inside_rect = False
        self.correction_window = True

    def set_handle_option(self, correction_window_position=None,
                          correction_client_rect=None,
                          inside_correction_rect=None,
                          is_inside_rect=False,
                          correction_window=True):
        """
        设置win32操作参数
        :param correction_window_position:
        :param correction_client_rect:
        :param inside_correction_rect:
        :param is_inside_rect:
        :param correction_window:
        :return:
        """
        self.correction_window_position = correction_window_position if correction_window_position else [8, 8, 1152, 679]
        self.correction_client_rect = correction_client_rect if correction_client_rect else [0, 0, 1136, 640]
        self.inside_correction_rect = inside_correction_rect if inside_correction_rect else []
        self.is_inside_rect = is_inside_rect
        self.correction_window = correction_window

    def get_handle(self, window_title: str):
        """
        获取窗口句柄
        :param window_title: 需要获取句柄的窗口标题
        :return:
        """
        # 获取屏幕大小
        screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        top_hwnd = win32gui.FindWindow(None, window_title)  # 获取窗口句柄
        if top_hwnd:
            # 窗口处于最小化，还原窗口
            while win32gui.IsIconic(top_hwnd):
                win32gui.ShowWindow(top_hwnd, win32con.SW_NORMAL)
            # 窗口正常
            else:
                # 获取顶层窗口位置
                window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(top_hwnd)
                # 窗口需要修正
                if self.correction_window:
                    # 窗口在屏幕之外，移动窗口到屏幕内
                    if (window_left < 8 or window_right > screen_x) or (window_top < 8 or window_bottom > screen_y):
                        win32gui.SetWindowPos(top_hwnd, win32con.HWND_NOTOPMOST,
                                              self.correction_window_position[0],
                                              self.correction_window_position[1],
                                              self.correction_window_position[2],
                                              self.correction_window_position[3],
                                              win32con.SWP_SHOWWINDOW)
                        time.sleep(0.2)
                    # 获取窗口大小
                    client_rect = win32gui.GetClientRect(top_hwnd)
                    # 窗口大小不符合
                    if (not client_rect[2] == 1136) or (not client_rect[3] == 640):
                        # 修改窗口大小， 位置不变
                        win32gui.SetWindowPos(top_hwnd, win32con.HWND_NOTOPMOST, window_left, window_top, 1152, 679,
                                              win32con.SWP_SHOWWINDOW)
                        time.sleep(0.2)
                # 非模拟器内部窗口，返回句柄
                if not self.is_inside_rect:
                    return top_hwnd
                # 模拟器内部窗口
                elif self.is_inside_rect:
                    the_render_hwnd = win32gui.FindWindowEx(top_hwnd, 0, None, "TheRender")  # 获取模拟器TheRender句柄
                    if the_render_hwnd:
                        return the_render_hwnd
                    else:
                        return 0
        else:
            return 0
