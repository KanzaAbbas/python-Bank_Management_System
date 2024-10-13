# acc = account
# no = number

class Customer:
    def __init__(self, name, address, phone_no, email):
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.email = email

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_no}")
        print(f"Email: {self.email}")

class Account:
    def __init__(self, acc_no, acc_type, balance, customer):
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid Deposit Amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid Withdrawal amount OR insufficient Balance")

    def display_account_info(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}")

        self.coustomer.display_details()


class SavingsAccount(Account):
    def display_acc_info(self):
        print(f"Saving Account Number: {self.acc_no}")
        print(f"Balance: {self.balance}")

        self.customer.display_details()


class Bank:
    def __init__(self, name):
        self.name = name
        self.branch = []
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added.")

    def add_acc(self, acc):
        self.account.append(acc)
        print(f"Account {acc.acc_no} added for {acc.customer.name}.")
    
    def display_customers(self):
        print("Customers List: ")

        for customer in self.customers:
            customer.display_details()

    def display_accounts(self):
        print("ACcounts List: ")

        for acc in self.accounts:
            acc.display_acc_info()


class SavingsAccount(Account):
    def display_acc_info(self):
        print(f"Saving Account Number: {self.acc_no}")
        print(f"Balance: {self.balance}")

        self.customer.display_details()