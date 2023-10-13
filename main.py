from services.expense_manager import ExpenseManager

if __name__ == '__main__':
    em = ExpenseManager()
    u0 = ExpenseManager().register_user(id="u1", name="A", email="abc@abc.com", phone="1234")
    u1 = ExpenseManager().register_user(id="u2", name="A", email="abc@abc.com", phone="1234")
    u2 = ExpenseManager().register_user(id="u3", name="A", email="abc@abc.com", phone="1234")
    u3 = ExpenseManager().register_user(id="u4", name="A", email="abc@abc.com", phone="1234")

    # EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
    # EXPENSE u1 1250 2 u2 u3 EXACT 370 880
    # EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
    # SHOW
    # SHOW u1

    while True:
        input_str = input("What do you want me to do? ")
        print()
        words = input_str.split(" ")
        command = words[0]
        if command == "SHOW":
            if len(words) == 1:
                em.show_balances()
            else:
                user_id = words[1]
                em.show_balance(user_id=user_id)
        elif command == "EXPENSE":
            paid_by = words[1]
            total_amount = float(words[2])
            no_of_members = int(words[3])
            end = 4 + no_of_members
            members = words[4:end]
            type = words[end].lower()
            split_data = words[end+1:]
            if split_data:
                split_data = [float(x) for x in split_data]
            em.add_expense(user_id=paid_by, total_amount=total_amount, members=members, type=type, split_data=split_data)
        elif command == "END":
            break
        else:
            print("please enter a valid command")
        print()
