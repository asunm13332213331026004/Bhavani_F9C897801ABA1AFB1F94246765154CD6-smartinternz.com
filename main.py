#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
        elif amount > self.__account_balance:
            print("Invalid withdrawal amount or Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ₹{self.__account_balance}")


# Create an instance of BankAccount
my_account = BankAccount("1234567890", "Hari", 5000.0)

# Test deposit and withdrawal functionality
my_account.display_balance()
my_account.deposit(500.0)
my_account.withdraw(200.0)
my_account.display_balance()