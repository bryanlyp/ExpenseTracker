#!/usr/bin/env python3
from .ExpenseTracker.Cash import Cash

if __name__ == "__main__":
    a = Cash("$500.00") < Cash("600.00")
    print(a)
