from Functions import account_creation, account_enquiry, delete_account, money_deposit, money_withdraw

def display_menu():
    """Display the main menu."""
    print("<----------> WELCOME TO THE MAZE BANK ......! <---------->".center(65).upper())
    print("\n1. Create New Account")
    print("2. Money Deposit")
    print("3. Money Withdraw")
    print("4. Account Enquiry")
    print("5. Account Deletion")
    print("6. Exit")

def main():
    """Main function to handle user choices."""
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            account_creation()
        
        elif choice == 2:
            money_deposit()
        
        elif choice == 3:
            money_withdraw()
        
        elif choice == 4:
            account_enquiry()
        
        elif choice == 5:
            delete_account()
        
        elif choice == 6:
            print("Thank you for using Maze Bank. Goodbye!")
            break
        
        else:
            print("Enter a valid input.")
        
        
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
