"""
Bank class for managing accounts and data persistence.
Handles file operations using JSON for data storage.
"""

import json
import os
from typing import Dict, Optional
from account import Account


class Bank:
    """Manages bank accounts and handles data persistence."""
    
    def __init__(self, data_file: str = "data.json"):
        """
        Initialize the bank system.
        
        Args:
            data_file: Path to the JSON file for data storage
        """
        self.data_file = data_file
        self.accounts: Dict[str, Account] = {}
        self.load_accounts()
    
    def load_accounts(self):
        """Load accounts from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for account_data in data.get("accounts", []):
                        account = Account.from_dict(account_data)
                        self.accounts[account.account_number] = account
                print(f"✅ Loaded {len(self.accounts)} account(s) from {self.data_file}")
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"⚠️  Error loading accounts: {e}")
                print("Starting with empty account list.")
        else:
            print(f"📁 No existing data file found. Starting fresh.")
    
    def save_accounts(self):
        """Save all accounts to JSON file."""
        try:
            data = {
                "accounts": [account.to_dict() for account in self.accounts.values()]
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error saving accounts: {e}")
            return False
    
    def create_account(self, name: str, initial_deposit: float = 0.0) -> Optional[Account]:
        """
        Create a new bank account.
        
        Args:
            name: Account holder's name
            initial_deposit: Initial deposit amount (default: 0.0)
            
        Returns:
            Created Account object, or None if creation failed
        """
        if not name or not name.strip():
            print("❌ Account name cannot be empty!")
            return None
        
        if initial_deposit < 0:
            print("❌ Initial deposit cannot be negative!")
            return None
        
        # Generate account number (simple incrementing approach)
        account_number = self._generate_account_number()
        
        account = Account(account_number, name.strip(), initial_deposit)
        self.accounts[account_number] = account
        
        if self.save_accounts():
            print(f"✅ Account created successfully!")
            print(f"   Account Number: {account_number}")
            print(f"   Name: {name}")
            print(f"   Initial Balance: ${initial_deposit:.2f}")
            return account
        else:
            # Remove account if save failed
            del self.accounts[account_number]
            return None
    
    def _generate_account_number(self) -> str:
        """
        Generate a unique account number.
        
        Returns:
            Unique account number string
        """
        if not self.accounts:
            return "ACC001"
        
        # Find the highest account number and increment
        max_num = 0
        for acc_num in self.accounts.keys():
            try:
                num = int(acc_num.replace("ACC", ""))
                max_num = max(max_num, num)
            except ValueError:
                continue
        
        return f"ACC{max_num + 1:03d}"
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Get an account by account number.
        
        Args:
            account_number: Account number to look up
            
        Returns:
            Account object if found, None otherwise
        """
        return self.accounts.get(account_number)
    
    def deposit(self, account_number: str, amount: float) -> bool:
        """
        Deposit money into an account.
        
        Args:
            account_number: Account number
            amount: Amount to deposit
            
        Returns:
            True if successful, False otherwise
        """
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found!")
            return False
        
        if account.deposit(amount):
            if self.save_accounts():
                print(f"✅ Deposit successful! New balance: ${account.get_balance():.2f}")
                return True
            else:
                print("❌ Deposit completed but failed to save data!")
                return False
        return False
    
    def withdraw(self, account_number: str, amount: float) -> bool:
        """
        Withdraw money from an account.
        
        Args:
            account_number: Account number
            amount: Amount to withdraw
            
        Returns:
            True if successful, False otherwise
        """
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found!")
            return False
        
        if account.withdraw(amount):
            if self.save_accounts():
                print(f"✅ Withdrawal successful! New balance: ${account.get_balance():.2f}")
                return True
            else:
                print("❌ Withdrawal completed but failed to save data!")
                return False
        return False
    
    def check_balance(self, account_number: str) -> bool:
        """
        Check and display account balance.
        
        Args:
            account_number: Account number
            
        Returns:
            True if account found, False otherwise
        """
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found!")
            return False
        
        print("\n" + "="*50)
        print(f"Account Number: {account.account_number}")
        print(f"Account Holder: {account.name}")
        print(f"Current Balance: ${account.get_balance():.2f}")
        print("="*50)
        return True
    
    def show_transaction_history(self, account_number: str) -> bool:
        """
        Display transaction history for an account.
        
        Args:
            account_number: Account number
            
        Returns:
            True if account found, False otherwise
        """
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found!")
            return False
        
        transactions = account.get_transaction_history()
        
        print("\n" + "="*70)
        print(f"Transaction History - Account {account_number}")
        print(f"Account Holder: {account.name}")
        print("="*70)
        
        if not transactions:
            print("No transactions found.")
        else:
            print(f"{'Date/Time':<20} {'Type':<10} {'Amount':<15} {'Balance After':<15}")
            print("-"*70)
            for trans in transactions:
                trans_type = trans["type"].upper()
                amount = f"${trans['amount']:.2f}"
                balance = f"${trans['balance_after']:.2f}"
                timestamp = trans["timestamp"]
                print(f"{timestamp:<20} {trans_type:<10} {amount:<15} {balance:<15}")
        
        print("="*70)
        return True
    
    def list_all_accounts(self):
        """Display all accounts."""
        if not self.accounts:
            print("No accounts found.")
            return
        
        print("\n" + "="*70)
        print("All Accounts")
        print("="*70)
        print(f"{'Account Number':<15} {'Name':<30} {'Balance':<15}")
        print("-"*70)
        for account in self.accounts.values():
            print(f"{account.account_number:<15} {account.name:<30} ${account.balance:<14.2f}")
        print("="*70)

