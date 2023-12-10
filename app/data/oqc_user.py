from hiworker.storage import Storage


class OqcUser(Storage):
    """
    不良品列表
    """
    def __init__(self, table):
        super(OqcUser, self).__init__(table)
