"""
Account class for the Simple Banking System.
Represents a bank account with basic operations and transaction history.
"""

from datetime import datetime
from typing import List, Dict


class Account:
    """Represents a bank account with balance and transaction history."""
    
    def __init__(self, account_number: str, name: str, initial_deposit: float = 0.0):
        """
        Initialize a new account.
        
        Args:
            account_number: Unique account identifier
            name: Account holder's name
            initial_deposit: Initial deposit amount (default: 0.0)
        """
        self.account_number = account_number
        self.name = name
        self.balance = float(initial_deposit)
        self.transactions: List[Dict] = []
        
        # Record initial deposit if provided
        if initial_deposit > 0:
            self.add_transaction("deposit", initial_deposit)
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.balance += amount
        self.add_transaction("deposit", amount)
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw (must be positive and not exceed balance)
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"❌ Insufficient balance! Current balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        self.add_transaction("withdraw", amount)
        return True
    
    def add_transaction(self, transaction_type: str, amount: float):
        """
        Add a transaction to the history.
        
        Args:
            transaction_type: Type of transaction ('deposit' or 'withdraw')
            amount: Transaction amount
        """
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.balance
        }
        self.transactions.append(transaction)
    
    def get_balance(self) -> float:
        """Get the current account balance."""
        return self.balance
    
    def get_transaction_history(self) -> List[Dict]:
        """Get the transaction history."""
        return self.transactions
    
    def to_dict(self) -> Dict:
        """
        Convert account to dictionary for JSON storage.
        
        Returns:
            Dictionary representation of the account
        """
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Account':
        """
        Create an Account instance from a dictionary.
        
        Args:
            data: Dictionary containing account data
            
        Returns:
            Account instance
        """
        account = cls(
            account_number=data["account_number"],
            name=data["name"],
            initial_deposit=0.0  # We'll restore balance from data
        )
        account.balance = data.get("balance", 0.0)
        account.transactions = data.get("transactions", [])
        return account
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"Account {self.account_number} - {self.name} - Balance: ${self.balance:.2f}"

