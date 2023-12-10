from config.db import db_config
from ..storage import StorageJSON, StorageSQLite


class AppSetting:
    def __init__(self, use_sqlite=True):
        self.data = []
        self.table = "app_setting"
        if use_sqlite:
            self.db = StorageSQLite(self.table, db_config)
        else:
            self.json_file_name = self.table + ".json"
            self.db = StorageJSON(self.json_file_name)
        self.parent_table = ""
        self.refresh_data()

    def refresh_data(self):
        self.data = self.db.get_all_data()
        # print(self.data)

    def read_option(self, option):
        if self.data:
            return self.data[0].get(option)

    def set_option(self, option, value):
        if self.db.read_row("id", 1):
            self.db.update_row_field(1, option, value)
        else:
            self.db.add_row({option: value})
        self.refresh_data()

    def get_onmyoji_pc_path(self):
        return self.read_option("onmyoji_pc_path")

    def get_emulator_path(self):
        return self.read_option("emulator_path")

    def get_sandboxie_path(self):
        return self.read_option("sandboxie_path")

    def get_cpu_sleep_time(self):
        return self.read_option("cpu_sleep_time")
