from models.split import Split
from services.split.base import SplitBaseService


class SplitEqualService(SplitBaseService):
    def create(self):
        splits = []
        calculated_amount = round(self.total_amount / float(len(self.members)), 2)
        for member_index in range(len(self.members)):
            split = Split(user_id=self.members[member_index], amount=calculated_amount)
            splits.append(split)
        return splits

    def validate(self):
        return True
