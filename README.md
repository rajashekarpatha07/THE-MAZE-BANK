# Maze Bank Management System

Welcome to the Maze Bank Management System! This is a simple Python-based bank management application that allows users to create accounts, deposit and withdraw money, check account details, and delete accounts.

## Features

- **Create New Account**: Allows users to create a new savings or current account.
- **Deposit Money**: Users can deposit money into their accounts.
- **Withdraw Money**: Users can withdraw money from their accounts.
- **Account Enquiry**: Check account details including balance, account type, and creation date.
- **Account Deletion**: Delete an existing account.

## Prerequisites

To run this project, you need Python installed on your system. It is recommended to use Python 3.6 or higher.

## Installation

1. **Navigate to the Project Directory**
   Nagivate to directory after cloning

   ```bash
   cd "c:/navigate/to/your/directory"
   ```

3. **Install Dependencies**

   This project doesn’t require any external Python packages besides the built-in libraries. However, if you want to create an executable, you will need **PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

## Usage

### Running the Application

To run the Python script directly:

```bash
python Maze_bank.py
```

### Creating an Executable

To create a standalone executable for Windows, run:

```bash
pyinstaller --onefile --add-data "Functions.py;." Maze_bank.py
```

This command will generate a single executable file in the `dist` directory.

## File Structure

- `Functions.py`: Contains the functions for account management operations.
- `Maze_bank.py`: The main entry point of the application.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
3. **Commit Your Changes**
4. **Push to the Branch**
5. **Create a Pull Request**


## Contact

If you have any questions or suggestions, feel free to contact me at rajashekarpatha07@gmail.com.

---
