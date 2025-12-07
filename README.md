# 🏦 Simple Banking System in Python

A simple and beginner-friendly Python Banking System that demonstrates core banking operations such as account creation, deposit, withdrawal, and balance inquiry. This project is perfect for students learning Python, OOP concepts, and file handling.

## 📌 Features

- ✅ **Create New Account** - Register a customer with basic details such as name, account number, and initial deposit.
- ✅ **Deposit Money** - Add funds to the selected account.
- ✅ **Withdraw Money** - Withdraw funds with proper balance validation.
- ✅ **Check Balance** - View the current balance of an account.
- ✅ **Transaction History** - Maintains a log of deposits and withdrawals with timestamps.
- ✅ **List All Accounts** - View all registered accounts in the system.
- ✅ **Data Persistence** - User data is stored using JSON file handling so all changes are saved.

## 🛠 Technologies Used

- **Python 3.13.7**
- **File Handling / JSON Storage**
- **Classes & Objects (OOP)**
- **Menu-Driven Console Application**

## 📁 Project Structure

```
Simple-Banking-System/
│
├── account.py          # Account class with OOP features
├── bank.py             # Bank class with file operations
├── main.py             # Main menu-driven application
├── data.json           # JSON file for data storage (created automatically)
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13.7 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/prashant0413/Simple-Banking-System-0187CS231163.git
   cd Simple-Banking-System-0187CS231163
   ```
   
   Or download as ZIP and extract it, then navigate to the project directory:
   ```bash
   cd Simple-Banking-System-0187CS231163
   ```

### Running the Application

Run the main Python file:

```bash
python main.py
```

Or on some systems:

```bash
python3 main.py
```

## 📖 How to Use

1. **Create New Account**
   - Enter the account holder's name
   - Optionally provide an initial deposit amount
   - The system will generate a unique account number (e.g., ACC001, ACC002)

2. **Deposit Money**
   - Enter the account number
   - Enter the deposit amount
   - The balance will be updated automatically

3. **Withdraw Money**
   - Enter the account number
   - Enter the withdrawal amount
   - The system validates sufficient balance before processing

4. **Check Balance**
   - Enter the account number
   - View the current balance and account details

5. **Transaction History**
   - Enter the account number
   - View all deposits and withdrawals with timestamps

6. **List All Accounts**
   - View all registered accounts with their balances

7. **Exit**
   - Safely exit the application (data is automatically saved)

## 💾 Data Storage

All account data is stored in `data.json` file in JSON format. The file is automatically created when you first run the application. Each time you perform an operation, the data is saved to ensure persistence.

**Example data.json structure:**
```json
{
  "accounts": [
    {
      "account_number": "ACC001",
      "name": "John Doe",
      "balance": 1000.0,
      "transactions": [
        {
          "type": "deposit",
          "amount": 1000.0,
          "timestamp": "2024-12-05 10:30:00",
          "balance_after": 1000.0
        }
      ]
    }
  ]
}
```

## 🎓 Learning Objectives

This project demonstrates:

- **Object-Oriented Programming (OOP)**
  - Class definition and instantiation
  - Methods and attributes
  - Class methods and instance methods

- **File Handling**
  - Reading from JSON files
  - Writing to JSON files
  - Error handling for file operations

- **Data Structures**
  - Dictionaries for account storage
  - Lists for transaction history

- **User Input/Output**
  - Console-based menu system
  - Input validation
  - User-friendly error messages

- **Control Flow**
  - Loops and conditionals
  - Exception handling

## 🔒 Features & Validations

- ✅ Account number uniqueness
- ✅ Balance validation for withdrawals
- ✅ Positive amount validation
- ✅ Account existence validation
- ✅ Automatic data saving after each operation
- ✅ Transaction history tracking
- ✅ Error handling and user-friendly messages

## 📝 Example Usage Flow

```
🏦 SIMPLE BANKING SYSTEM
==================================================
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. List All Accounts
7. Exit
==================================================

Enter your choice (1-7): 1

--- Create New Account ---
Enter Account Holder Name: Alice Smith
Enter Initial Deposit (0 for no deposit): $500
✅ Account created successfully!
   Account Number: ACC001
   Name: Alice Smith
   Initial Balance: $500.00
```

## 🤝 Contributing

This is a learning project. Feel free to fork, modify, and enhance it with additional features like:
- Account deletion
- Account modification
- Interest calculation
- Multiple account types
- Password protection
- GUI interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project is open source and available for educational purposes.

## 👨‍💻 Author

**prashant0413**

- GitHub: [@prashant0413](https://github.com/prashant0413)
- Repository: [Simple-Banking-System-0187CS231163](https://github.com/prashant0413/Simple-Banking-System-0187CS231163)

Created as a learning project for Python beginners.

---

**Happy Coding! 🎉**

