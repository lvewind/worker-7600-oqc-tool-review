from PySide6.QtWidgets import QMenu
from PySide6 import QtGui


# 运行列表右键菜单
class ProductsListMenu(QMenu):
    def __init__(self):
        super(ProductsListMenu, self).__init__()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.setFont(font)
        self.save_usb_power = self.addAction("Input USB Power")

        self.addSeparator()
        self.delete_product = self.addAction("Delete")

        self.addSeparator()
        self.output_txt = self.addAction("Output TXT")
        self.addSeparator()
        self.output_txt_bridge = self.addAction("Output TXT Bridge")

        self.addSeparator()
        self.open_txt = self.addAction("Open TXT")
        self.addSeparator()
        self.open_txt_bridge = self.addAction("Open TXT Bridge")
