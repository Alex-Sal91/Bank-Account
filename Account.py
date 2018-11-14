class Account():
    no_of_accounts = 0

    def __init__(self, first, last, acc_num):
        self.first = first
        self.last = last
        self.account_number = acc_num
        Account.no_of_accounts += 1


    def __repr__(self):
        return "Account Holder: {} {}\n Account No: {}".format(self.first, self.last, self.account_number)

    def display_accounts(self):
        return Account.no_of_accounts


acc1 = Account("Alex", "Sal", 45347789)

print(acc1)
print(acc1.display_accounts())

