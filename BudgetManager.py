from ExpenseTracker.Cash import Cash
from ExpenseTracker.Cash import CashStream
class BudgetManager:
    def __init__(self, streams):
        # streams is a list of CashStream objects
        self.incomeStreams = list()
        self.expenseStreams = list()
        for stream in streams:
            if stream.isIncome():
                self.incomeStreams.append(stream)
            else:
                self.expenseStreams.append(stream)
    def balance(self):
        pass
