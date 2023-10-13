from models.split import Split
from services.split.base import SplitBaseService


class SplitPercentService(SplitBaseService):
    def create(self):
        splits = []
        for member_index in range(len(self.members)):
            calculated_amount = round((self.total_amount * (self.split_data[member_index] / 100.0)), 2)
            split = Split(user_id=self.members[member_index], amount=calculated_amount)
            splits.append(split)
        return splits

    def validate(self):
        return sum(self.split_data) == 100.00

