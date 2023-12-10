from hiworker.storage import Storage


class OqcResult(Storage):
    """
    测试结果数据
    """
    def __init__(self, table):
        super(OqcResult, self).__init__(table)

    def add_result(self, product: dict):
        return self.db_add_row(product)

    def del_result(self, field_name: str, value):
        return self.db_del_row(field_name, value)

    def edit_result(self, data_item: dict, ref_field, ref_value):
        return self.db_update_row(data_item, ref_field, ref_value)

    def read_result(self, ref_field, ref_value):
        return self.db_read_row(ref_field, ref_value)


oqc_result = OqcResult("oqc_test_result")
