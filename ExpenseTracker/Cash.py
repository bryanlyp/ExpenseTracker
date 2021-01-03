from datetime import datetime
class Cash:
    def __init__(self, value):
        if isinstance(value, str):
            if value.startswith("$"):
                value = value[1:]
            if "." in value:
                self.__value = int(value.split(".")[0]) * 100 + int(value.split(".")[1])
            else:
                self.__value = int(value) * 100
        elif isinstance(value, int):
            self.__value = value
    def __add__(self, o):
        return Cash(self.__value + o.__value)
    def __sub__(self, o):
        return Cash(self.__value - o.__value)
    def __lt__(self, o):
        return self.__value < o.__value
    def __gt__(self, o):
        return self.__value > o.__value
    def __le__(self, o):
        return self.__value <= o.__value    
    def __ge__(self, o):
        return self.__value >= o.__value
    def __eq__(self, o):
        return self.__value == o.__value
    def __ne__(self, o):
        return self.__value != o.__value
    def __str__(self):
        if self.__value < 0:
            string = "-$"
        else:
            string = "$"
        value = abs(self.__value)
        string += str(value // 100) + "." + str(value % 100)
        return string
    def getDollars(self):
        return self.__value // 100
    def getCents(self):
        return self.__value % 100
    def multiply(self, val):
        return Cash(int(self.__value * val))
    def divide(self, val):
        return Cash(int(self.__value / val))
    

class CashStream:
    def __init__(self, name, cash, date):
        self.name = name
        self.cash = cash
        self.date = datetime.strptime(date, "%b-%y").date()

class Account:
    def __init__(self, name, incomeStreams=None, expenseStreams=None):
        self.name = name
        if incomeStreams == None:
            self.incomeStreams = list()
        else:
            self.incomeStreams = incomeStreams
        if expenseStreams == None:
            self.expenseStreams = list()
        else:
            self.expenseStreams = expenseStreams
    def addIncomeStream(self, stream):
        self.incomeStreams.append(stream)
    def addExpenseStream(self, stream):
        self.expenseStreams.append(stream)
    def getBalance(self):
        balance = Cash(0)
        for incomeStream in self.incomeStreams:
            balance += incomeStream.cash
        for expenseStream in self.expenseStreams:
            balance -= expenseStream.cash
        return balance
    def getMonthlyBalance(self):
        pass
