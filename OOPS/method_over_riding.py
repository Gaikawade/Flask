class Transaction:
    def __init__(self, balance=0):
        self.balance = balance
        
    def execute(self):
        pass

class Deposit(Transaction):
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account
        Transaction().__init__(self)
        self.execute()

    def execute(self):
        Transaction().balance += self.amount
        print(f'Deposit of Rs.{self.amount} made to account {self.account}')
        print(f'Balance Rs.{Transaction().balance}')

class Withdrawal(Transaction):
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account
        Transaction().__init__(self, account)
        self.execute()

    def execute(self):
        if Transaction().account_balance < self.amount:
            print("Insufficient funds")
            return
        Transaction().account.balance -= self.amount
        print(f'Withdrawal of Rs.{self.amount} made from account {self.account}')
        print(f'Balance Rs.{Transaction().account_balance}')

tra  = Transaction(200)
depo = Deposit(2000, 123456)
# withd = Withdrawal(1000, 123456)



# class Transfer(Transaction):
#     def __init__(self, amount, account_from, account_to):
#         self.amount = amount
#         self.account_from = account_from
#         self.account_to = account_to
#         Transaction().__init__(self)
#         self.execute()

#     def execute(self):
#         if Transaction().account_from < self.amount:
#             print("Insufficient funds")
#             return
#         self.account_from -= self.amount
#         self.account_to += self.amount
#         print(f'Transfer of {self.amount} made from account {self.account_from} to account {self.account_to}')