class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance    

account = BankAccount(5000)
print(account.balance)