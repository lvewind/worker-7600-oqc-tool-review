from copy import deepcopy
from hiworker.storage import Storage


class UserData(Storage):
    def __init__(self, table_name: str):
        super(UserData, self).__init__(table_name)
        self.table_name = table_name
        self.parent_table = ""
        self.data = []
        self.refresh_data()
        self.save_to_file = True

    def add_row(self, data_dict: dict):
        success = self.db_add_row(data_dict)
        if success:
            self.refresh_data()
        return success

    def del_rows(self, id_list: list, parent_object_list: list, sub_object_list: list):
        for index in id_list:
            sub_id_list = self.read_row_field(index, "sub_list")
            if parent_object_list:
                for parent_object in parent_object_list:
                    if self.is_in_parent_table(index, parent_object):  # 需要删除的行在父表中
                        break
                    else:
                        if sub_object_list and sub_id_list:
                            sub_object_list[0].del_sub_rows(sub_id_list, [])
                        self.db_del_row("id", index)
            else:
                if sub_object_list and sub_id_list:
                    sub_object_list[0].del_sub_rows(sub_id_list, [])
                self.db_del_row("id", index)
        self.refresh_data()

    def del_row(self, field_name: str, value, parent_object_list: list, sub_object_list: list):
        row_data = self.read_row(field_name, value)
        index = row_data.get("id")
        sub_id_list = self.read_row_field(index, "sub_list")
        if parent_object_list:
            for parent_object in parent_object_list:
                if self.is_in_parent_table(index, parent_object):  # 需要删除的行在父表中
                    break
                else:
                    if sub_object_list and sub_id_list:
                        sub_object_list[0].del_sub_rows(sub_id_list, [])
                    self.db_del_row(field_name, value)
        else:
            if sub_object_list:
                sub_id_list = self.read_row_field(index, "sub_list")
                if sub_id_list:
                    sub_object_list[0].del_sub_rows(sub_id_list, [])
            self.db_del_row(field_name, value)
        self.refresh_data()

    def add_sub_row(self, data_dict: dict, parent_object: list):
        new_id = self.db_add_row(data_dict)
        if new_id:
            self.add_to_parent_sub_list_field(new_id, parent_object[0], parent_object[1])
            self.refresh_data()
        else:
            pass

    def del_sub_rows(self, id_list: list, parent_object: list):
        id_list = deepcopy(id_list)
        for index in id_list:
            self.db_del_row('id', index)
            if parent_object:
                self.remove_from_parent_sub_list_field(index, parent_object[0], parent_object[1])

        self.refresh_data()

    def update_row(self, data_dict: dict, ref_field, ref_value):
        if self.read_row(ref_field, ref_value):
            success = self.db_update_row(data_dict, refer=ref_field, ref_value=ref_value)
        else:
            data_dict.update({ref_field: ref_value})
            success = self.add_row(data_dict)
        if success:
            self.refresh_data()
        return success

    def update_items(self, id_list: list, items: dict):
        if items:
            for key, value in items.items():
                self.db_update_rows_field(id_list, key, value)
            self.refresh_data()

    def refresh_data(self):
        self.data = self.db_get_all_data()

    def read_row(self, filed_name: str, value):

        if self.data:
            for data_dict in self.data:
                if value == data_dict.get(filed_name):
                    return data_dict
            else:
                return {}
        else:
            return {}

    def read_row_field(self, index: int, field: str):
        """
        读取列表数据中的字典字段
        :param index:
        :param field:
        :return:
        """
        # 枚举数据列表，返回符合条件的字典value
        if self.data:
            for data_dict in self.data:
                if index == data_dict.get("id", 0):
                    return data_dict.get(field, "")
            else:
                return 0
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

    @staticmethod
    def not_in_parent_table(index, parent_table):
        if parent_table.data:
            for data_dict in parent_table.data:
                if data_dict.get("job_id") == index or \
                        data_dict.get("worker_id") == index or \
                        data_dict.get("plan_day_id") == index:
                    return False
            else:
                return True
        else:
            return True

    @staticmethod
    def is_in_parent_table(index, parent_table):
        if parent_table.data:
            for data_dict in parent_table.data:
                if data_dict.get("job_id") == index or \
                        data_dict.get("worker_id") == index or \
                        data_dict.get("plan_day_id") == index:
                    return True
            else:
                return False
        else:
            return False

    @staticmethod
    def remove_from_parent_sub_list_field(index, parent_id, parent_table):
        parent_table.db.remove_sub_list_item(parent_id, index)
        parent_table.refresh_data()

    @staticmethod
    def add_to_parent_sub_list_field(index, parent_id, parent_table):
        parent_table.db.upgrade_sub_list_item(parent_id, index)
        parent_table.refresh_data()
