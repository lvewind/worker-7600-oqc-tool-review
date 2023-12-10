from PySide6.QtWidgets import QTableWidgetItem, QTableWidget
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QBrush, QColor
from ..user_data.user_data import UserData
import datetime
import re
from copy import deepcopy
from operator import itemgetter


class TableLoad:

    # 初始化表格
    @classmethod
    def init_table_header(cls, table: QTableWidget, header_dict: dict, is_horizontal=True):
        """
        初始化表头
        :param table: 要初始化的表名称
        :param header_dict: 表头字典{“header_name”： , "width": ,}
        :param is_horizontal: 默认为水平表头
        :return:
        """
        if is_horizontal:
            table.setColumnCount(len(header_dict))
            table.setRowCount(0)
        else:
            table.setColumnCount(0)
            table.setRowCount(len(header_dict))
        if header_dict:
            for value in header_dict.values():
                item = QtWidgets.QTableWidgetItem()
                col = value.get("col")
                if is_horizontal:
                    table.setHorizontalHeaderItem(col, item)
                    item = table.horizontalHeaderItem(col)
                    item.setText(value.get("header_name"))
                    col_width = value.get("width", 0)
                    if col_width:
                        table.setColumnWidth(col, col_width)
                else:
                    row = col
                    table.setHorizontalHeaderItem(row, item)
                    item = table.horizontalHeaderItem(row)
                    item.setText(value.get("header_name"))
                    row_height = value.get("height", 0)
                    if row_height:
                        table.setRowHeight(row, row_height)

    @classmethod
    def init_table_col(cls, table: QTableWidget, col_dict: dict, col=0, align="center"):
        table.setRowCount(len(col_dict))
        for value in col_dict.values():
            table.setRowHeight(value.get("row"), 18)
            cls.set_table_item(table, value.get("row_name"), value.get("row"), col, align=align)

    @classmethod
    def init_table_row(cls, table: QTableWidget, row_text: dict, row=0):
        table.setColumnCount(len(row_text))
        for (key, text) in row_text.items():
            cls.set_table_item(table, str(text), row, int(key))

    # 加载表格数据
    @classmethod
    def load_table_common(cls, table: QTableWidget, table_data: list, col_header: dict,
                          select_last_row=False, sort="", reverse=False):
        table.setRowCount(0)
        data_list_cp = deepcopy(table_data)
        if data_list_cp:
            if sort:
                data_list = sorted(data_list_cp, key=itemgetter(sort), reverse=reverse)
            else:
                data_list = data_list_cp

            if data_list:
                current_row = table.currentRow()
                for row, data_dict in enumerate(data_list):  # 枚举列表，获取字典以及对应的行数
                    row_count = table.rowCount()  # 获取当前表格总行数
                    if row >= row_count:  # 数据行大于等于表格行
                        row = table.rowCount()  # 获取当前行数
                        table.insertRow(row)  # 追加新行
                        table.setRowHeight(row, 20)  # 设置行高
                        if data_dict:
                            for key, value in data_dict.items():
                                cls.load_table_common_item(table, data_dict, row, key, col_header)
                    else:
                        if data_dict:
                            for key, value in data_dict.items():
                                cls.load_table_common_item(table, data_dict, row, key, col_header)   # 加载当前行数据
                else:
                    # 删除多余的表格行
                    row_count = table.rowCount()  # 获取当前表格总行数
                    data_count = len(data_list)  # 获取数据条目数量
                    if row_count > data_count:  # 有多出的表格行
                        row_del_count = row_count - data_count  # 获取需要删除的数量
                        for row_del in range(row_del_count):
                            table.removeRow(data_count)
                if select_last_row:
                    table.selectRow(table.rowCount() - 1)
                else:
                    table.selectRow(current_row)


    @classmethod
    def load_table_common_item(cls, table: QTableWidget, data_dict: dict, row, col_name, col_header: dict):
        for key, col_setting in col_header.items():
            if key == col_name:
                align = col_setting.get("align")
                if not align:
                    align = "center"
                col_text = data_dict.get(key)   # 获取单元格数据
                col = col_setting.get("col")  # 获取列号
                is_bool = col_setting.get("is_bool")
                if is_bool:
                    if col_text:
                        col_text = "ok"
                    else:
                        col_text = ""
                    cls.set_table_item(table, col_text, row, col, [255, 255, 255])
                    break
                elif col_text:                    # 单元格数据有效
                    extend = col_setting.get("extend")  # 获取扩展项
                    if extend:
                        data_id = int(col_text)
                        col_text = [str(col_text)]  # 转化为列表形式
                        if not extend.get("show_self"):     # 不需要显示自身原来的值
                            col_text = []
                        extend_data = extend.get("extend_data")    # 获取扩展项数据定义字典
                        if extend_data:
                            for extend_data_item in extend_data:
                                condition = extend_data_item.get("condition")    # 获取数据条件项
                                if condition:   # 条件项存在
                                    condition_data_object = condition.get("data_object")    # 获取条件项数据对象
                                    if condition_data_object:
                                        condition_data_field = condition.get("data_field")  # 获取条件项数据字段
                                        # 条件值不满足时，进入下一个扩展数据项检测
                                        if condition_data_object == "self":
                                            if not data_dict.get(condition_data_field) == condition.get("value"):
                                                continue
                                        else:
                                            if not condition_data_object.read_row_field.get(condition_data_field) == \
                                                   condition.get("value"):
                                                continue
                                prefix = extend_data_item.get("prefix")
                                if prefix:
                                    col_text.append(prefix)

                                data_object = extend_data_item.get("data_object")
                                if data_object:
                                    if data_object == "self":
                                        extend_result = data_dict.get(extend_data_item.get("data_field"))
                                    else:
                                        extend_result = data_object.read_row_field(data_id, extend_data_item.get("data_field"))
                                    if extend_result:
                                        sub = extend_data_item.get("sub")
                                        if sub:
                                            sub_data_object = sub.get("data_object")
                                            extend_result = sub_data_object.read_row_field(int(extend_result),
                                                                                           sub.get("data_field"))
                                        else:
                                            chs = extend_data_item.get("chs")
                                            if chs:
                                                extend_result = chs.get(str(extend_result))

                                        col_text.append(str(extend_result))
                            col_text = ", ".join(col_text)
                    else:
                        chs = col_setting.get("chs")
                        if chs:
                            col_text = chs.get(str(col_text))
                if col_setting.get("use_row_number"):
                    col_text = str(row + 1)
                bg_color = [255, 255, 255]
                if col_setting.get("color_enable"):
                    test_state = data_dict.get("test_state")
                    if test_state:
                        color_dict = col_setting.get("color")
                        bg_color = color_dict.get(str(test_state), [255, 255, 255])
                str_trim = col_setting.get("str_trim")
                if str_trim:
                    col_text = col_text[-4:]
                cls.set_table_item(table, col_text, row, col, bg_color, is_time=col_setting.get("is_time"), align=align)
                break

    @classmethod
    def load_table_common_item_with_text(cls, table: QTableWidget, text, row, col_name: str, col_header: dict):
        for key, col_setting in col_header.items():
            if key == col_name:
                col = col_setting.get("col")    # 获取列号
                if text:
                    cls.set_table_item(table, text, row, col)  # 显示数据
                else:
                    cls.set_table_item(table, "", row, col)
                break

    @classmethod
    def load_table_sub_common(cls, table: QTableWidget, parent_table: QTableWidget,
                              table_data: UserData, parent_table_data: UserData, col_header: dict):
        table.setRowCount(0)
        # 获取父表当前id
        parent_current_id = TableRead.get_current_row_id(parent_table)
        # 获取父表子项
        parent_sub_list = parent_table_data.read_row_field(parent_current_id, "sub_list")

        if parent_sub_list:
            table.setRowCount(len(parent_sub_list))  # 设置表格行数
            for row, sub_list_id in enumerate(parent_sub_list):     # 遍历父表sub_list
                table.setRowHeight(row, 18)  # 设置行高
                data_dict = table_data.read_row(sub_list_id)
                if type(data_dict) == dict:
                    for key, col_setting in col_header.items():
                        col = col_setting.get("col")  # 获取列号
                        text = data_dict.get(key)
                        is_time = col_setting.get("is_time")
                        is_bool = col_setting.get("is_bool")
                        if is_bool:
                            if text:
                                text = "是"
                            else:
                                text = ""
                        if text == "auto":
                            text = "自动"
                        chs = col_setting.get("chs")
                        if chs:
                            text = chs.get(str(text))

                        extend = col_setting.get("extend")
                        if extend:
                            text = []
                            extend_data = extend.get("extend_data")  # 获取扩展项数据定义字典
                            if extend_data:
                                for extend_data_item in extend_data:
                                    data_object = extend_data_item.get("data_object")
                                    if data_object:
                                        data_id = data_dict.get(extend_data_item.get("data_id_key"))
                                        data_field = extend_data_item.get("data_field")
                                        result = data_object.read_row_field(int(data_id), data_field)
                                        chs = extend_data_item.get("chs")
                                        if chs:
                                            result = chs.get(result)
                                        if not result:
                                            result = ""
                                        text.append(str(result))
                                text = ", ".join(text)

                        cls.set_table_item(table, text, row, col, is_time=is_time)

    @classmethod
    def load_table_run_count(cls, table: QTableWidget, data_dict: dict, row_index: dict):
        if data_dict and row_index:
            for row_field, row_setting in row_index.items():
                field_value = data_dict.get(row_field)
                cls.set_table_item(table, field_value, row_setting.get("row"), 1)

    @classmethod
    def load_table_run_count_item(cls, table: QTableWidget, row_name: str, value: int, row_index: dict):
        for row_field, row_setting in row_index.items():
            if row_field == row_name:
                cls.set_table_item(table, value, row_setting.get("row"), 1)
                break

    @classmethod
    def set_table_item(cls, list_table: QTableWidget, text, row, col, bg_color=None, is_time=False, align="center"):
        if not list_table.item(row, col):
            list_table.setItem(row, col, QTableWidgetItem(""))
            if align == "center":
                list_table.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            elif align == "left":
                list_table.item(row, col).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            elif align == "right":
                list_table.item(row, col).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        if text:
            if is_time:
                time_sec = int(text)
                list_table.item(row, col).setText(str(datetime.timedelta(seconds=time_sec)))
            else:
                list_table.item(row, col).setText(str(text))
        else:
            list_table.item(row, col).setText("")
        if bg_color:
            list_table.item(row, col).setBackground(QBrush(QColor(bg_color[0], bg_color[1], bg_color[2])))

    @staticmethod
    def sort_by_dict_key(item, key):
        return item.get(key)


class TableRead:

    @classmethod
    def filter_not_number_input(cls, input_data: str):
        """
        # 过滤输入的非数字数据
        :param input_data:
        :return:
        """
        data_number = re.sub(r"\D", "", input_data)
        if not data_number == "":
            return int(data_number)
        else:
            return 0

    @classmethod
    def get_current_row_col_data(cls, current_table: QTableWidget, col: int):
        current_row = current_table.currentRow()
        if current_row >= 0:
            return cls.get_item_data(current_table, current_row, col)
        else:
            return False

    @classmethod
    def get_item_data(cls, current_table: QTableWidget, row: int, col: int):
        if current_table.item(row, col):
            item_data = current_table.item(row, col).text()
            return item_data
        else:
            return False

    @classmethod
    def get_current_row_id(cls, current_table: QTableWidget):
        """
        # 获取当前表格选中row的ID
        :param current_table: 当前表格
        :return:
        """
        current_id = cls.get_current_row_col_data(current_table, 0)
        if current_id:
            return int(current_id)
        else:
            return False

    @classmethod
    def get_row_id(cls, current_table: QTableWidget, row):
        """
        # 获取当前表格指定row的ID
        :param current_table: 当前表格
        :param row: 表格row
        :return:
        """
        if row >= 0:
            current_id = current_table.item(row, 0).text()
            return int(current_id)
        else:
            return False

    @classmethod
    def get_current_selected_rows(cls, current_table: QTableWidget):
        """
        获取当前表格被选中的rows
        :param current_table:
        :return:
        """
        selected_rows = []
        rows = current_table.rowCount()
        for row in range(rows):
            if current_table.item(row, 0):
                if current_table.item(row, 0).isSelected():
                    selected_rows.append(row)
        return selected_rows

    @classmethod
    def get_selected_rows_id_list(cls, current_table: QTableWidget):
        """
        获取当前表格被选中的rows的id字段
        :param current_table:
        :return:
        """
        selected_rows_id = []
        rows = current_table.rowCount()
        for row in range(rows):
            if current_table.item(row, 0):
                if current_table.item(row, 0).isSelected():
                    selected_rows_id.append(int(current_table.item(row, 0).text()))
        return selected_rows_id

    @classmethod
    def get_all_rows_id_list(cls, current_table: QTableWidget):
        """
        获取当前表格被选中的rows的id字段
        :param current_table:
        :return:
        """
        all_rows_id = []
        rows = current_table.rowCount()
        for row in range(rows):
            if current_table.item(row, 0):
                all_rows_id.append(int(current_table.item(row, 0).text()))
            else:
                pass
        return all_rows_id
