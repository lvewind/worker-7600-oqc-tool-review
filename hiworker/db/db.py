import sqlite3
import os
import re
from config import *
import wmi

w = wmi.WMI()
cpu = w.Win32_Processor()


class DB:
    def __init__(self, data_sql: list, data_path="data\\user", db_file_name="user.db", sql_file_name="user.sql"):
        self.data_base_sql = data_sql
        self.app_path = os.path.abspath(os.getcwd())
        self.user_path = os.path.join(self.app_path, data_path)
        if not os.path.exists(self.user_path):
            os.makedirs(self.user_path, exist_ok=True)
        self.db_file = os.path.join(self.user_path, db_file_name)
        self.sql_file = os.path.join(self.user_path, sql_file_name)

        self.create_table()
        # self.create_table_from_sql_file()
        # self.cursor = self.con.cursor()
        # self.cursor.execute('INSERT INTO run_list VALUES (1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1)')

    def create_table(self):
        self.data_base_sql = [x.replace('\n', ' ') for x in self.data_base_sql]
        self.data_base_sql = [re.sub(r" +", " ", x) for x in self.data_base_sql]
        con = sqlite3.connect(self.db_file, check_same_thread=False)
        c = con.cursor()
        for sql_item in self.data_base_sql:
            try:
                c.execute(sql_item)
            except sqlite3.OperationalError as e:
                print(e)
        con.close()

    def create_table_from_sql_file(self):
        try:
            with open(self.sql_file) as f:
                sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
                sql_list = [x.replace('\n', ' ') for x in sql_list]
                sql_list = [re.sub(r" +", " ", x) for x in sql_list]
                con = sqlite3.connect(self.db_file, check_same_thread=False)
                c = con.cursor()
                for sql_item in sql_list:
                    try:
                        c.execute(sql_item)
                    except sqlite3.OperationalError:
                        pass
        except FileNotFoundError:
            pass
        con.close()


db_create = DB(data_sql=data_base_sql, data_path=db_config.get("data_path"), db_file_name=db_config.get("db_file_name"))
del db_create
