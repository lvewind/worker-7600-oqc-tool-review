from hiworker.storage import Storage


class OqcProductsList(Storage):
    """
    产品列表
    """
    def __init__(self, table):
        super(OqcProductsList, self).__init__(table)

    def add_product(self, product: dict):
        return self.db_add_row(product)

    def del_product(self, field_name: str, value):
        return self.db_del_row(field_name, value, [], [])

    def edit_product(self, data_item: dict, ref_field, ref_value):
        return self.db_update_row(data_item, ref_field, ref_value)

    def get_sn(self, index):
        value = self.db_read_row_field(index, "sn")
        if value:
            return value
        else:
            return ""

    def get_mac_addr(self, index):
        value = self.db_read_row_field(index, "mac_addr")
        if value:
            return value
        else:
            return ""

    def get_web_passwd(self, index):
        value = self.db_read_row_field(index, "web_passwd")
        if value:
            return value
        else:
            return ""

    def get_wifi_passwd(self, index):
        value = self.db_read_row_field(index, "wifi_passwd")
        if value:
            return value
        else:
            return ""


oqc_products_list = OqcProductsList("oqc_products_list")
