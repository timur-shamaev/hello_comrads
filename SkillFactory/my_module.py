def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    return deposit, withdraw

deposit, withdraw = make_account(100)
print(deposit(15))
print(withdraw(30))