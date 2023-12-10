from ..thread import ThreadLock
import json
import sqlite3
import threading
import os

sqlite_mutex = threading.Lock()


class StorageSQLite(object):
    def __init__(self, table: str, db_config: dict):
        self.table = table
        self.lock = ThreadLock()
        self.data = []
        self.parent_table = ""
        self.save_to_file = True
        data_path = db_config.get("data_path")
        db_file_name = db_config.get("db_file_name")
        self.db_file = os.path.join(data_path, db_file_name)
        self.refresh_data()

    def refresh_data(self):
        self.data = self.db_get_all_data()

    def db_add_row(self, data_dict: dict):
        columns, values = self.dict_to_query_add(data_dict)
        query = " ".join(["INSERT INTO", self.table, "DEFAULT VALUES"])
        if columns:
            query = " ".join(["INSERT INTO", self.table, columns, "VALUES", values])
        return self.execute_query_write(query)
        #     self.get_all_data()
        #     last_data_row = self.data[-1]
        #     return last_data_row.get("id")
        # else:
        #     return 0

    def db_add_rows(self, data_dict_list: list):
        add_results = []
        if data_dict_list:
            for data_dict in data_dict_list:
                add_result = self.db_add_row(data_dict)
                add_results.append(add_result)
        return add_results

    def db_del_row(self, refer="id", refer_value=None):
        if type(refer_value) == str:
            query = " ".join(["DELETE FROM", self.table, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
        else:
            query = " ".join(["DELETE FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        self.execute_query_write(query)

    def db_del_rows(self, refer_value_list: list, refer="id"):
        if refer_value_list:
            for refer_value in refer_value_list:
                self.db_del_row(refer=refer, refer_value=refer_value)

    def db_update_row(self, data_dict: dict, refer="id", ref_value=None):
        if ref_value:
            refer_value = ref_value
        else:
            refer_value = data_dict.get(refer)
        placeholder = self.dict_to_query_update(data_dict)
        if placeholder:
            if type(refer_value) == str:
                query = " ".join(["UPDATE", self.table, "SET", placeholder, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
            else:
                query = " ".join(["UPDATE", self.table, "SET", placeholder, "WHERE", refer, "=", str(refer_value)])
            return self.execute_query_write(query)

    def db_update_rows(self, data_dict_list: list, refer="id"):
        if data_dict_list:
            for data_dict in data_dict_list:
                self.db_update_row(data_dict, refer=refer)

    def db_update_rows_field(self, index_list: list, field: str, value):
        if index_list:
            for index in index_list:
                self.db_update_row({"id": index, field: value})

    def db_read_row(self, refer_value, refer="id"):
        if type(refer_value) == str:
            query = " ".join(["SELECT * FROM", self.table, "WHERE", refer, "=", "'" + str(refer_value) + "'"])
        else:
            query = " ".join(["SELECT * FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        return self.execute_query_read(query)

    def db_read_rows(self, refer_value_list: list, refer="id"):
        rows = []
        if refer_value_list:
            for refer_value in refer_value_list:
                rows.append(self.db_read_row(refer_value, refer=refer))
        return rows

    def db_read_row_field(self, target_field: str, refer_value: str, refer="id"):
        query = " ".join(["SELECT", target_field, "FROM", self.table, "WHERE", refer, "=", str(refer_value)])
        result = self.execute_query_read(query)
        if result and type(result) == tuple:
            if result[0]:
                return json.loads(result[0])
            else:
                return False
        else:
            return False

    def db_get_all_data(self):
        data_list = []
        query = " ".join(["SELECT * FROM", self.table])
        db = sqlite3.connect(self.db_file)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            for data_row in result:
                data_list.append(self.result_to_dict(data_row, cursor.description))
        db.close()
        if data_list:
            self.data = data_list
            return data_list
        else:
            return []

    @staticmethod
    def list_sort_key(element: dict):
        return element["id"]

    def execute_query_write(self, query, commit=True):
        with sqlite_mutex:
            try:
                db = sqlite3.connect(self.db_file)
                cursor = db.cursor()
                cursor.execute(query)
                if commit:
                    db.commit()
                db.close()
                return 1
            except sqlite3.OperationalError as e:
                print("sqlite3.OperationalError", e)
                return 0
            except sqlite3.IntegrityError as e:
                print("sqlite3.IntegrityError", e)
                return 0

    def execute_query_read(self, query):
        try:
            db = sqlite3.connect(self.db_file)
            cursor = db.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                result = self.result_to_dict(result, cursor.description)
            db.close()
            return result
        except sqlite3.OperationalError as e:
            print(e)
            return False

    @staticmethod
    def result_to_dict(result, description):
        data_dict = {}
        if result:
            try:
                for idx, key in enumerate(description):
                    if type(result[idx]) == str and len(result[idx]) > 2 and \
                            (("[" == result[idx][0] and "]" == result[idx][-1]) or ("{" == result[idx][0] and "}" == result[idx][-1])):
                        data_dict.update({key[0]: json.loads(result[idx])})
                    else:
                        data_dict.update({key[0]: result[idx]})
            except TypeError:
                pass
        return data_dict

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
                placeholder += key + " =" + str(value) + ", "
            elif type(value) == str:
                placeholder += key + " = '" + str(value) + "', "
            else:
                placeholder += key + " = '" + json.dumps(value, ensure_ascii=False) + "', "
        return placeholder.rstrip(", ")
