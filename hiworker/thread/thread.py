from PySide6.QtCore import QThread
from PySide6.QtCore import QMutex


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()
        self.stop_flag = False
        self.stop_status = False
        self.suspend = False
        self.close_env = True

    def stop(self):
        self.close_env = True
        self.stop_flag = True

    def suspend_on(self):
        self.suspend = True

    def suspend_off(self):
        self.suspend = False

    def stop_without_close_game(self):
        self.close_env = False
        self.stop_flag = True


class ThreadLock(QMutex):
    def __init__(self):
        super(ThreadLock, self).__init__()
