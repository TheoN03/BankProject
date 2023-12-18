import sys
import logging
import pickle
import pathlib
from typing import List
from menu import MainMenu
from bank_manager import BankAccount


STARTUP_REQ_DIRS = ["data"]
ROOT = pathlib.Path(__file__).parent

logging.basicConfig(filename=ROOT / "log.log", level=logging.DEBUG)

def create_required_dirs(root: pathlib.Path, dir_paths: List[pathlib.Path]):
    """Function for creating a directory for data that will be stored."""
    r_dir = {}
    for path in dir_paths:
        dp = root / path
        r_dir[path] = dp
        dp.mkdir(exist_ok=True)
    return r_dir

def perform_transaction(bank_account, transaction_type):
    """Function for making a deposit by using input."""
    while True:
        amount_input = input("Enter the transaction amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(input("Enter the transaction amount: "))

    if transaction_type == "1":
        bank_account.deposit(amount)
        print(f"Deposit of {amount} made.")

def perform_withdraw(bank_account, transaction_type):
    """Function for making a withdraw by using input."""
    while True:
        amount_input = input("Enter the withdraw amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(input("Enter the transaction amount: "))
    if transaction_type == "4":
        bank_account.withdraw(amount)
        print(f"Withdraw of {amount} made.")

def check_balance(bank_account):
    """Function for checking current balance of the account."""
    print(f"Current balance: {bank_account.get_balance()}")

def view_transaction_history(bank_account):
    """Function for viewing tranzaction history."""
    transactions = bank_account.get_transaction_history()
    if transactions:
        print("Transaction History:")
        for transaction in transactions:
            print("-" * 30)
            print(
                f"Type: {transaction.type}, Amount: {transaction.amount}, "
                f"Timestamp: {transaction.timestamp}"
            )
            print("-" * 30)
    else:
        print("No transactions yet.")

if __name__ == "__main__":
    logging.info("Starting the Banking Simulation...")
    try:
        logging.debug(f"Trying to create startup directories {STARTUP_REQ_DIRS}")
        program_dirs = create_required_dirs(ROOT, STARTUP_REQ_DIRS)
    except OSError:
        logging.critical("Can not create startup directories.")
        sys.exit(1)
    else:
        logging.info("Startup directories created.")


    bank_account = BankAccount()

    main_menu = MainMenu()
    main_menu.register_entry("1", "Perform Transaction", lambda: perform_transaction(bank_account, "1"))
    main_menu.register_entry("2", "Check Balance", lambda: check_balance(bank_account))
    main_menu.register_entry("3", "View Transaction History", lambda: view_transaction_history(bank_account))
    main_menu.register_entry("4", "Perform Withdraw", lambda:perform_withdraw(bank_account, "4"))
    main_menu.run()


    dump_path = program_dirs.get("data") / "bank_account.pickle"
    
    try:
        with open(dump_path, "wb") as fout:
            pickle.dump(bank_account, fout)
    except OSError as err:
        logging.error("Can not save bank account data.")
        logging.debug(err)
    else:
        logging.info("Bank account data saved to disk.")
