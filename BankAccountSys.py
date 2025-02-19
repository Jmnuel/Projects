from typing import List, Optional
import json
import os

class BankAccount:
    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0):
        if not account_number or not owner_name:
            raise ValueError("Account number and owner name cannot be empty.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number.strip()
        self.owner_name = owner_name.strip()
        self.balance = initial_balance
        self.transactions = []  

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        self.transactions.append(f"Deposited {amount} on {self.get_current_date()}")
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount} on {self.get_current_date()}")
        print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        return True

    def display_balance(self):
        print(f"Account: {self.account_number} owned by {self.owner_name} has a balance of {self.balance}")

    def display_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print(f"Transaction history for account {self.account_number}:")
            for transaction in self.transactions:
                print(f"  - {transaction}")

    @staticmethod
    def get_current_date() -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "account_number": self.account_number,
            "owner_name": self.owner_name,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'BankAccount':
        account = cls(data["account_number"], data["owner_name"], data["balance"])
        account.transactions = data["transactions"]
        return account

class BankAccountSys:
    def __init__(self):
        self.accounts: List[BankAccount] = []
        self.filename = "bank_accounts.json"
        self.load_accounts()

    def save_accounts(self):
        data = [account.to_dict() for account in self.accounts]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_accounts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.accounts = [BankAccount.from_dict(item) for item in data]

    def create_account(self, account_number: str, owner_name: str, initial_balance: float = 0):
        try:
            new_account = BankAccount(account_number, owner_name, initial_balance)
            self.accounts.append(new_account)
            self.save_accounts()
            print(f"Account {account_number} created successfully for {owner_name}!")
        except ValueError as e:
            print(f"Error: {e}")

    def find_account(self, account_number: str) -> Optional[BankAccount]:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

def main():
    bank = BankAccountSys()

    while True:
        print("\nBank Account System (BankAccountSys)")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Display account balance")
        print("5. View transaction history")
        print("6. List all accounts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            account_number = input("Enter account number: ").strip()
            owner_name = input("Enter owner name: ").strip()
            try:
                initial_balance = float(input("Enter initial balance (non-negative): ") or 0)
                if initial_balance < 0:
                    print("Initial balance cannot be negative!")
                    continue
                bank.create_account(account_number, owner_name, initial_balance)
            except ValueError:
                print("Invalid input! Balance must be a number.")

        elif choice == '2':
            account_number = input("Enter account number to deposit to: ").strip()
            account = bank.find_account(account_number)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    bank.save_accounts()
                except ValueError:
                    print("Invalid amount!")
            else:
                print(f"Account {account_number} not found!")

        elif choice == '3':
            account_number = input("Enter account number to withdraw from: ").strip()
            account = bank.find_account(account_number)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    bank.save_accounts()
                except ValueError:
                    print("Invalid amount!")
            else:
                print(f"Account {account_number} not found!")

        elif choice == '4':
            account_number = input("Enter account number to check balance: ").strip()
            account = bank.find_account(account_number)
            if account:
                account.display_balance()
            else:
                print(f"Account {account_number} not found!")

        elif choice == '5':
            account_number = input("Enter account number to view transactions: ").strip()
            account = bank.find_account(account_number)
            if account:
                account.display_transactions()
            else:
                print(f"Account {account_number} not found!")

        elif choice == '6':
            if not bank.accounts:
                print("No accounts exist yet.")
            else:
                print("\nAll Accounts:")
                for account in bank.accounts:
                    print(f"Account {account.account_number} - Owner: {account.owner_name}, Balance: {account.balance}")

        elif choice == '7':
            print("Exiting Bank Account System.")
            bank.save_accounts() 
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()