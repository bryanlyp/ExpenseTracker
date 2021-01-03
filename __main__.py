#!/usr/bin/env python3
from .ExpenseTracker.Cash import Cash
from .ExpenseTracker.Cash import CashStream
from .ExpenseTracker.Cash import Account
import sys


if __name__ == "__main__":
    salary = CashStream("Salary", Cash("$500"), "Jan-21")
    fixed_expenses = CashStream("Fixed Expenses", Cash("$100"), "Jan-21")
    variable_expenses = CashStream("Variable Expenses", Cash("$100"), "Jan-21")
    liquefied = CashStream("Liquefied", Cash("$200"), "Jan-21")
    bank = Account("Account", [salary], [fixed_expenses, variable_expenses, liquefied])
    wallet = Account("Wallet", [liquefied])
    print(bank.getBalance())
    print(wallet.getBalance())
