class SplitBaseService:
    def __init__(self, members, total_amount, split_data=None):
        self.members = members
        self.total_amount = total_amount
        self.split_data = split_data

    def create(self):
        pass

    def validate(self):
        pass

    def get_splits(self):
        if not self.validate():
            # Raise exception
            return False
        return self.create()
