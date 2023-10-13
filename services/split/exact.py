from models.split import Split
from services.split.base import SplitBaseService


class SplitExactService(SplitBaseService):
    def create(self):
        splits = []
        for member_index in range(len(self.members)):
            calculated_amount = self.split_data[member_index]
            split = Split(user_id=self.members[member_index], amount=calculated_amount)
            splits.append(split)
        return splits

    def validate(self):
        return sum(self.split_data) == self.total_amount
