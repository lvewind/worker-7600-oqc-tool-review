from config.db import db_config
from .storage_sqlite import StorageSQLite
from .storage_json import StorageJSON


class Storage(StorageSQLite):
    def __init__(self, table: str):
        super(Storage, self).__init__(table, db_config)
