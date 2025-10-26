# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        # Initialize the bank with a list of account balances.
        self.account_balance = balance
        # Store the total number of accounts for validity checks.
        self.total_accounts = len(self.account_balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Convert from 1-indexed to 0-indexed accounts
        account1 -= 1
        account2 -= 1

        # Check if both account numbers are valid
        if (account1 >= self.total_accounts or account1 < 0) or (account2 >= self.total_accounts or account2 < 0):
            return False  # Invalid account number

        # Check if account1 has enough money to transfer
        if money <= self.account_balance[account1]:
            # Perform the transfer
            self.account_balance[account2] += money
            self.account_balance[account1] -= money
            return True
        
        # Transfer fails if insufficient balance
        return False

    def deposit(self, account: int, money: int) -> bool:
        # Convert from 1-indexed to 0-indexed
        account -= 1

        # Check if account number is valid
        if (account >= self.total_accounts or account < 0):
            return False  # Invalid account number

        # Add money to the account
        self.account_balance[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        # Convert from 1-indexed to 0-indexed
        account -= 1

        # Check for valid account and sufficient balance
        if (account >= self.total_accounts or account < 0) or self.account_balance[account] < money:
            return False  # Invalid account or insufficient funds

        # Subtract money from account
        self.account_balance[account] -= money
        return True


# Example of how this class works:
# obj = Bank([100, 200, 300])
# obj.transfer(1, 2, 50)  -> True (transfer 50 from acc1 to acc2)
# obj.deposit(3, 100)     -> True (add 100 to acc3)
# obj.withdraw(2, 150)    -> True (withdraw 150 from acc2)
