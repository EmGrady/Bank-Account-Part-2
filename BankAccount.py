# ITSC 3155: Software Engineering
# Assignment: BankAccount Part 2
class BankAccount:
    bankTitle = "Bank of America"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number
        self._routing_number = routing_number

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount
        print("Successful Deposit")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance:
            print("Withdrawal Failed: Withdrawal amount greater than current balance.")
        elif self.current_balance < self.minimum_balance:
            print("Withdrawal Failed: Current balance is less than minimum balance.")
        elif self.current_balance - withdraw_amount < self.minimum_balance:
            print("Withdrawal Denied: Minimum balance requirement would be violated.")
        else:
            self.current_balance -= withdraw_amount
            print(f"Successful Withdraw of {withdraw_amount}\n"
                  f"Current Balance: {self.current_balance}")

    def print_customer_information(self):
        print(f"Bank Title: {BankAccount.bankTitle}\n"
              f"Customer Name: {self.customer_name}\n"
              f"Current Balance: {self.current_balance}\n"
              f"Minimum Balance: {self.minimum_balance}")