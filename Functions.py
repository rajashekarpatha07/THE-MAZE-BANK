import random
from datetime import datetime


accounts = []

def generate_account_number():
    """Generate a unique account number."""
    return random.randint(1000000, 9999999)

def account_creation():
    """Create a new bank account."""
    account_name = input("Enter Your Name: ")
    account_type = int(input("Enter Your Account Type (1. Savings or 2. Current): "))

    if account_type not in [1, 2]:
        print("Enter a valid account type....!")
        return

    if account_type == 1 or account_type == 2:
        print("NOTE - You need to maintain a minimum balance of 500/- in your account")

    account_no = generate_account_number()
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    account = {
        'account_number': account_no,
        'name': account_name,
        'account_type': account_type,
        'balance': 0,  # Initial balance is 0
        'date_created': date_created
    }
    accounts.append(account)

    print(f"Your Account number is generated: {account_no}")
    print(f"Your Account was successfully created by name {account_name}, Account type is {account_type}, and Account number is {account_no} on {date_created}")

def money_deposit():
    """Deposit money into an existing account."""
    acc_no_to_deposit = int(input("Enter the Account number to Deposit amount: "))
    # Find the account
    account = next((acc for acc in accounts if acc['account_number'] == acc_no_to_deposit), None)
    
    if account is None:
        print("Account number not found.")
        return

    money_to_deposit = float(input("Enter the Amount to deposit: "))
    
    if money_to_deposit <= 0:
        print("Amount must be greater than zero......!")
        return

    account['balance'] += money_to_deposit
    print(f"The amount of {money_to_deposit} is successfully deposited into account {acc_no_to_deposit}. New balance is {account['balance']}.")
    

def money_withdraw():
    """Withdraw money from an existing account."""
    acc_no_to_withdraw = int(input("Enter the Account number to Withdraw amount: "))
    # Find the account
    account = next((acc for acc in accounts if acc['account_number'] == acc_no_to_withdraw), None)
    
    if account is None:
        print("Account number not found.")
        return

    money_to_withdraw = float(input("Enter the Amount to withdraw: "))
    
    if money_to_withdraw <= 0:
        print("Amount must be greater than zero......!")
        return

    if money_to_withdraw > account['balance']:
        print("Insufficient balance for the withdrawal.")
        return

    account['balance'] -= money_to_withdraw
    print(f"The amount of {money_to_withdraw} has been successfully withdrawn from account {acc_no_to_withdraw}. New balance is {account['balance']}.")


def account_enquiry():
    """Enquire details of an existing account."""
    acc_no_to_enquire = int(input("Enter the Account number to enquire about: "))
    # Find the account
    account = next((acc for acc in accounts if acc['account_number'] == acc_no_to_enquire), None)
    
    if account is None:
        print("Account number not found.")
        return

    print(f"Account Number: {account['account_number']}")
    print(f"Name: {account['name']}")
    print(f"Account Type: {'Savings' if account['account_type'] == 1 else 'Current'}")
    print(f"Balance: {account['balance']}")
    print(f"Date Created: {account['date_created']}")
    

def delete_account():
    """Delete an existing account."""
    acc_no_to_delete = int(input("Enter the Account number to delete: "))
    global accounts
    # Find and remove the account
    account = next((acc for acc in accounts if acc['account_number'] == acc_no_to_delete), None)
    
    if account is None:
        print("Account number not found.")
        return

    accounts = [acc for acc in accounts if acc['account_number'] != acc_no_to_delete]
    print(f"Account number {acc_no_to_delete} has been successfully deleted.")
