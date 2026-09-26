# Group Assignment for ITSC 3155 Software Engineering
# Group Members: Morgan Grady and Kirk Patton

from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    """Checking Account with per-transfer dollar limit"""

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit


    def transfer(self, transfer_amount, target_account):
        """Move money from one account to another as long as it is within the allowable amount"""
        if transfer_amount > self.transfer_limit:
            print(f"Transfer Denied: ${transfer_amount} exceeds the "
                  f"per-transfer limit of ${self.transfer_limit:,.2f}.")
            return False
        starting_balance = self.current_balance
        self.withdraw(transfer_amount)
        if self.current_balance < starting_balance:
            target_account.deposit(transfer_amount)
            print(f"Transferred ${transfer_amount} to account "
                  f"{target_account.get_account_number()} ")
            return True
        return False

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Account Type: Checking\n"
              f"Transfer Limit: ${self.transfer_limit:,.2f} per transfer\n")