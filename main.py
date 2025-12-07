"""
Simple Banking System - Main Menu
A menu-driven console application for banking operations.
"""

from bank import Bank


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🏦 SIMPLE BANKING SYSTEM")
    print("="*50)
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. List All Accounts")
    print("7. Exit")
    print("="*50)


def get_float_input(prompt: str) -> float:
    """
    Get a float input from user with validation.
    
    Args:
        prompt: Input prompt message
        
    Returns:
        Valid float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Please enter a non-negative number!")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_account_number_input(bank: Bank) -> str:
    """
    Get account number input and validate it exists.
    
    Args:
        bank: Bank instance
        
    Returns:
        Valid account number or None
    """
    account_number = input("Enter Account Number: ").strip()
    if not account_number:
        print("❌ Account number cannot be empty!")
        return None
    
    if not bank.get_account(account_number):
        print(f"❌ Account {account_number} not found!")
        return None
    
    return account_number


def create_account_menu(bank: Bank):
    """Handle account creation."""
    print("\n--- Create New Account ---")
    name = input("Enter Account Holder Name: ").strip()
    
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    initial_deposit = get_float_input("Enter Initial Deposit (0 for no deposit): $")
    bank.create_account(name, initial_deposit)


def deposit_menu(bank: Bank):
    """Handle deposit operation."""
    print("\n--- Deposit Money ---")
    account_number = get_account_number_input(bank)
    if not account_number:
        return
    
    amount = get_float_input("Enter Deposit Amount: $")
    bank.deposit(account_number, amount)


def withdraw_menu(bank: Bank):
    """Handle withdrawal operation."""
    print("\n--- Withdraw Money ---")
    account_number = get_account_number_input(bank)
    if not account_number:
        return
    
    amount = get_float_input("Enter Withdrawal Amount: $")
    bank.withdraw(account_number, amount)


def check_balance_menu(bank: Bank):
    """Handle balance inquiry."""
    print("\n--- Check Balance ---")
    account_number = get_account_number_input(bank)
    if account_number:
        bank.check_balance(account_number)


def transaction_history_menu(bank: Bank):
    """Handle transaction history display."""
    print("\n--- Transaction History ---")
    account_number = get_account_number_input(bank)
    if account_number:
        bank.show_transaction_history(account_number)


def main():
    """Main application loop."""
    # Initialize bank system
    bank = Bank()
    
    print("\n" + "="*50)
    print("Welcome to Simple Banking System!")
    print("="*50)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            create_account_menu(bank)
        elif choice == "2":
            deposit_menu(bank)
        elif choice == "3":
            withdraw_menu(bank)
        elif choice == "4":
            check_balance_menu(bank)
        elif choice == "5":
            transaction_history_menu(bank)
        elif choice == "6":
            bank.list_all_accounts()
        elif choice == "7":
            print("\n" + "="*50)
            print("Thank you for using Simple Banking System!")
            print("Goodbye! 👋")
            print("="*50)
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-7.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please contact support if this issue persists.")

