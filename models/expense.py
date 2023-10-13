class Expense:
    def __init__(self, user_id, total_amount, splits, type):
        self.user_id = user_id
        self.total_amount = total_amount
        self.splits = splits
        self.type = type

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, value):
        self.user_id = value

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, value):
        self.total_amount = value

    def get_splits(self):
        return self.splits

    def set_splits(self, value):
        self.splits = value

    def get_type(self):
        return self.type

    def set_type(self, value):
        self.type = value
