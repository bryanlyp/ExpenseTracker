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
    