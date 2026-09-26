# Group Assignment for ITSC 3155 Software Engineering
# Group Members: Morgan Grady and Kirk Patton

from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

# Create 2 Checking Account Instances
morgan_checking = CheckingAccount("Morgan", 200, 20,101 ,2101 , 100)
kirk_checking = CheckingAccount("Kirk", 400, 40, 201 , 2202, 200)

# Create 2 Savings Account Instances
morgan_savings = SavingsAccount("Morgan", 400, 100,102 , 2101, 0.01)
kirk_savings = SavingsAccount("Kirk", 800, 200, 202, 2202, 0.02)


# Scenario 1: Morgan uses her checking and savings account
print("\n--- Scenario 1: Morgan ---")

print("\nMorgan's checking account:")
morgan_checking.print_customer_information()

# Morgan deposits $50 then withdraws $30
morgan_checking.deposit(50)
morgan_checking.withdraw(30)

# Morgan transfers money to her savings account
morgan_checking.transfer(40, morgan_savings)
morgan_checking.transfer(150, morgan_savings)

# Morgan's saving account
print("\nMorgan's saving account:")
morgan_savings.print_customer_information()

# Calculate and apply interest to savings
print(f"Interest calculated for 12 months: ${morgan_savings.calculate_interest()}")
morgan_savings.apply_interest(12)

# Scenario 2: Kirk uses his checking and savings account
print("\n---Scenario 2: Kirk---")

print("\nKirk's checking account")
kirk_checking.print_customer_information()

kirk_checking.deposit(100)
kirk_checking.withdraw(50)

# Transfer money from checking to savings
kirk_checking.transfer(100, kirk_savings)
kirk_checking.transfer(250, kirk_savings)

print("\nKirk savings account:")
kirk_savings.print_customer_information()

# Calculate and apply interest to his savings
print(f"Interest calculated for 12 months: ${kirk_savings.calculate_interest()}")
kirk_savings.apply_interest(12)
