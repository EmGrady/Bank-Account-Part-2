
from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    """Savings accounts earn monthly compounding interest"""
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super.__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def calculate_interest(self, months =12):
        """Returns the interest rate that will be given over the next year"""
        monthly_rate = self.interest_rate / 12
        new_balance = self.current_balance * (1+monthly_rate) ** months
        return round(new_balance - self.current_balance, 2)

    def apply_interest(self, months =12):
        """Add the earned interest rate to the current balance"""
        interest = self.calculate_interest(months)
        self.current_balance = round(self.current_balance + interest, 2)
        print(f"Interest Applied: ${interest:,.2f} over {months} month(s) "
              f"at {self.interest_rate:.2%} APR\n"
              f"Current Balance: ${self.current_balance:,.2f}")
        return self.current_balance

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Account Type: Savings Account\n"
              f"Interest Rate: {self.interest_rate:.2%}\n")