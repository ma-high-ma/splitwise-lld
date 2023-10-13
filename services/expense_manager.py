from models.expense import Expense
from models.user import User
from resolvers.split import SplitByTypeResolver


class ExpenseManager:
    UserMap = {}
    expenses = []
    balance_sheet = {}

    def register_user(self, id, name, email, phone):
        user = User(id=id, name=name, email=email, phone=phone)
        self.UserMap[id] = user
        return user

    def add_expense(self, user_id, total_amount, members, type, split_data=None):
        split_class = SplitByTypeResolver.get_obj(split_type=type)
        splits = split_class(members=members, total_amount=total_amount, split_data=split_data).get_splits()
        if not splits:
            print("error")
            return
        expense = Expense(user_id=user_id, total_amount=total_amount, splits=splits, type=type)

        self.expenses.append(expense)
        self.add_to_balance_sheet(user_id=user_id, splits=splits)

    def add_to_balance_sheet(self, user_id, splits):
        paid_by = user_id
        for split in splits:
            paid_to = split.user_id

            # Update balance sheet for paid_by user
            if not self.balance_sheet.get(paid_by):
                self.balance_sheet[paid_by] = {}

            self.balance_sheet[paid_by][paid_to] = split.amount + self.balance_sheet[paid_by].get(paid_to, 0.0)

            # Update balance sheet for paid_to user
            if not self.balance_sheet.get(paid_to):
                self.balance_sheet[paid_to] = {}

            self.balance_sheet[paid_to][paid_by] = self.balance_sheet[paid_to].get(paid_by, 0.0) - split.amount

    def show_balance(self, user_id):
        balances = self.balance_sheet.get(user_id)
        if not balances:
            return

        for paidTo, amt in balances.items():
            if paidTo == user_id:
                continue
            if amt > 0:
                print(paidTo, " owes ", user_id, " Rs. ", amt)
            if amt < 0:
                print(user_id, " owes ", paidTo, " Rs. ", abs(amt))

    def show_balances(self):
        for user_id, obj in self.UserMap.items():
            print("BALANCE SHEET FOR : ", user_id)
            self.show_balance(user_id=user_id)
            print()
