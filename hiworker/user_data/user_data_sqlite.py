from ..thread.thread import ThreadLock
import json
import sqlite3


class UserDataSQLite(object):
    def __init__(self, table: str, db_connect):
        self.table = table
        self.db = db_connect
        self.cursor = db_connect.con.cursor()
        self.lock = ThreadLock()

    def add_row(self, data_dict: dict):
        columns, values = self.dict_to_query_add(data_dict)
        query = " ".join(["INSERT INTO", self.table, "DEFAULT VALUES"])
        if columns:
            query = " ".join(["INSERT INTO", self.table, columns, "VALUES", values])
        return self.execute_query_write(query)

    def update_row(self, data_dict: dict, ref_field, ref_value):
        if ref_value:
            placeholder = self.dict_to_query_update(data_dict)
            if placeholder:
                query = "".join(["UPDATE ", self.table, " SET ", placeholder, " WHERE ", ref_field, " = '", str(ref_value), "'"])
                self.execute_query_write(query)

    def update_rows_field(self, index_list: list, field: str, value):
        for index in index_list:
            self.update_row_field(index, field, value)

    def upgrade_sub_list_item(self, index: int, sub_list_id: int):
        sub_list = self.read_row_field(index, "sub_list")
        if not sub_list:
            sub_list = []
        if sub_list_id not in sub_list:
            sub_list.append(sub_list_id)
        self.update_rows_field([index], "sub_list", sub_list)

    def remove_sub_list_item(self, index: int, sub_list_id: int):
        sub_list = self.read_row_field(index, "sub_list")
        if type(sub_list) == list:
            sub_list.remove(sub_list_id)
            self.update_rows_field([index], "sub_list", sub_list)

    def update_row_field(self, index: int, field: str, value):
        placeholder = field + "=" + str(value) if type(value) == int else field + "=" + "'" + str(value) + "'"
        query = " ".join(["UPDATE", self.table, "SET", placeholder, "WHERE id =", str(index)])
        if field == "run_time":
            self.execute_query_write(query, commit=False)
        else:
            self.execute_query_write(query)

    def del_row(self, field_name: str, value):
        query = "".join(["DELETE FROM ", self.table, " WHERE ", field_name, " = '", str(value), "'"])
        return self.execute_query_write(query)

    def read_row(self, field_name: str, value):
        query = " ".join(["SELECT * FROM", self.table, "WHERE", field_name, "=", str(value)])
        return self.result_to_dict(self.execute_query_read(query))

    def read_row_field(self, index: int, field: str):
        query = " ".join(["SELECT", field, "FROM", self.table, "WHERE id =", str(index)])
        result = self.execute_query_read(query)
        if result and type(result) == tuple:
            if field == "sub_list" and result[0]:
                return json.loads(result[0])
            else:
                return result[0]
        else:
            return False

    def read_row_by_record_id(self, record_id: str):
        query = " ".join(["SELECT * FROM", self.table, "WHERE record_id =", record_id])
        return self.result_to_dict(self.execute_query_read(query))

    def get_name(self, index: int):
        self.read_row_field(index, "name")

    def get_ids(self):
        query = " ".join(["SELECT id FROM", self.table])
        try:
            self.lock.lock()
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.lock.unlock()
            if result:
                data_list = []
                for d in result:
                    data_list.append(d[0])
                return data_list
            else:
                return False
        except sqlite3.OperationalError:
            return False

    def get_all_data(self):
        data_list = []
        query = " ".join(["SELECT * FROM", self.table])
        self.lock.lock()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.lock.unlock()
        if result:
            for data_row in result:
                data_list.append(self.result_to_dict(data_row))
        if data_list:
            return data_list
        else:
            return False

    @staticmethod
    def list_sort_key(element: dict):
        return element["id"]

    def execute_query_write(self, query, commit=True):
        try:
            self.lock.lock()
            self.cursor.execute(query)
            if commit:
                self.db.con.commit()
            self.lock.unlock()
            return 0
        except sqlite3.OperationalError as e:
            print(e)
            self.lock.unlock()
            return 1
        except sqlite3.IntegrityError as e:
            print(e)
            self.lock.unlock()
            return 2

    def execute_query_read(self, query):
        try:
            self.lock.lock()
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.lock.unlock()
            if result:
                return result
            else:
                return False
        except sqlite3.OperationalError:
            return False

    def result_to_dict(self, result):
        if result:
            data_dict = {}
            try:
                for idx, key in enumerate(self.cursor.description):
                    if key[0] == "sub_list" and result[idx]:
                        data_dict.update({key[0]: json.loads(result[idx])})
                    else:
                        data_dict.update({key[0]: result[idx]})
                return data_dict
            except TypeError:
                pass
        else:
            return False

    @staticmethod
    def dict_to_query_add(data_dict: dict):
        columns = ""
        values = []
        if data_dict:
            for key, value in data_dict.items():
                columns += str(key) + ", "
                if type(value) == int or type(value) == str:
                    values.append(value)
                else:
                    values.append(json.dumps(value, ensure_ascii=False))
            values = json.dumps(values, ensure_ascii=False)
            columns = "(" + columns.rstrip(", ") + ")"
            values = "(" + values.rstrip("]").lstrip("[") + ")"
            return columns, values
        else:
            return False, False

    @staticmethod
    def dict_to_query_update(data_dict: dict):
        placeholder = ""
        for key, value in data_dict.items():
            if type(value) == int:
                placeholder += key + "=" + str(value) + ", "
            elif type(value) == str:
                placeholder += key + "= '" + str(value) + "', "
            else:
                placeholder += key + "= '" + json.dumps(value, ensure_ascii=False) + "', "
        return placeholder.rstrip(", ")
