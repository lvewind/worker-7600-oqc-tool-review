from ..json.json import JsonReadWrite


class UserDataJSON(JsonReadWrite):
    def __init__(self, filename, json_path="data/user/"):
        self.table = filename
        if self.table:
            self.json_file_name = self.table + ".json"
        else:
            self.json_file_name = ""
        super(UserDataJSON, self).__init__(json_path, self.json_file_name)
        self.data = []
        self.load_list()

    def add_row(self, new_dict: dict, save_to_file=True):
        """
        添加数据行
        :param new_dict:
        :param save_to_file:
        :return:
        """
        if new_dict.get("id"):
            self.update_row(new_dict)
            return new_dict.get("id")
        else:
            if self.data:
                self.data.sort(key=self.list_sort_key)
            if len(self.data) <= 0:
                current_id = 1
            else:
                current_id = self.data[len(self.data) - 1].get("id", 0) + 1
            target_dict = {"id": current_id}
            target_dict.update(new_dict)
            self.data.append(target_dict)
            if save_to_file:
                self.save()
            return current_id

    def update_row(self, new_data: dict, save_to_file=True):
        """
        更新数据行
        :param save_to_file:
        :param new_data:
        :return:
        """
        for data_row in self.data:
            if new_data.get("id") == data_row.get("id"):
                data_row.update(new_data)
                if save_to_file:
                    self.save()
                return new_data.get("id")
        else:
            self.data.append(new_data)

    def update_rows_field(self, index_list, field: str, value, save_to_file=True):
        """
        更新列表数据中的字典字段
        :param index_list: int, list
        :param field:
        :param value:
        :param save_to_file: 是否立即写入文件
        :return:
        """
        if type(index_list) == list:
            for index in index_list:
                self.update_row_field(index, field, value, save_to_file)
        elif type(index_list) == int:
            self.update_row_field(index_list, field, value, save_to_file)

    def update_row_field(self, index: int, field: str, value, save_to_file=True):
        if self.data:
            for data_row in self.data:
                if index == data_row.get("id"):
                    data_row.update({field: value})
                    if save_to_file:
                        if not field == "run_time":
                            self.save()
                    return index
            else:
                self.data.append({"id": index, field: value})
                return index
        else:
            self.data.append({"id": index, field: value})
            return index

    def upgrade_sub_list_item(self, index: int, sub_list_id: int):
        """
        更新“sub_list"字段中的列表项
        """
        sub_list = self.read_row_field(index, "sub_list")
        if not sub_list:
            sub_list = []
        if sub_list_id not in sub_list:
            sub_list.append(sub_list_id)
        self.update_rows_field([index], "sub_list", sub_list)

    def remove_sub_list_item(self, index: int, sub_list_id: int):
        """
        移除“sub_list"字段中的列表项
        """

        sub_list = self.read_row_field(index, "sub_list")
        if type(sub_list) == list:
            sub_list.remove(sub_list_id)
            self.update_rows_field([index], "sub_list", sub_list)

    def del_row(self, field_name: str, value):
        """
        删除数据row
        :param field_name:
        :param value:
        :return:
        """
        # 枚举数据列表，删除含有对应id值的列表项字典
        for data_row in self.data:
            if value == data_row.get(field_name):
                self.data.remove(data_row)
                self.save()
                return value

    def read_row(self, field_name: str, field_value):
        """
        读取包含数据值的行
        :param field_name:
        :param field_value:
        :return:
        """
        for data_dict in self.data:
            if field_value == data_dict.get(field_name):
                return data_dict
        else:
            return False

    def read_row_field(self, index: int, field: str):
        """
        读取列表数据中的字典字段
        :param index:
        :param field:
        :return:
        """
        # 枚举数据列表，返回符合条件的字典value
        for data_dict in self.data:
            if index == data_dict.get("id", 0):
                if data_dict.get(field, ""):
                    return data_dict.get(field)
                else:
                    return 0

    def read_row_by_record_id(self, record_id: str):
        if self.data:
            for data_dict in self.data:
                if record_id == data_dict.get("record_id", 0):
                    return data_dict
            else:
                return False
        else:
            return False

    def get_name(self, index):
        name = self.read_row_field(index, "name")
        if name:
            return name
        else:
            return ""

    def get_ids(self):
        id_list = []
        if self.data:
            for data_dict in self.data:
                row_id = data_dict.get("id", 0)
                if row_id:
                    id_list.append(row_id)
            return id_list

    def get_all_data(self):
        self.load_list()
        return self.data

    def save(self):
        """
        保存数据
        :return:
        """
        self.save_json(self.data)

    def load_list(self):
        """
        加载数据列表
        :return:
        """
        self.data = self.load_single_json_file()

    @staticmethod
    def list_sort_key(element: dict):
        return element["id"]
