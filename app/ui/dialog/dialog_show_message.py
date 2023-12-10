from PySide6 import QtWidgets
from app.source.ui.show_message import Ui_Dialog_show_message
from app.app_signal.app_signal import signal_main_ui


class DialogShowMessage(QtWidgets.QDialog, Ui_Dialog_show_message):
    def __init__(self):
        super(DialogShowMessage, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

    def show_message(self, message: str):
        self.label.setText(message)
        self.show()
