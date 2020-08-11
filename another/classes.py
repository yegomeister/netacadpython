class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

    def returnList(self):
        return self.__stackList


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum


class AnotherStack(AddingStack):
    def __init__(self):
        AddingStack.__init__(self)
        self.__count = 0

    def push(self, val):
        self.__count += 1
        AddingStack.push(self, val)

    def pop(self):
        val = AddingStack.pop(self)
        self.__count -= 1

    def getCount(self):
        return self.__count

    def getList(self):
        return Stack.returnList(self)

someStack = AnotherStack()

someStack.push(22)
someStack.push(23)
someStack.push(25)

print(someStack.getCount())
print(someStack.returnList())
exStak = Stack()

#The code below shows that Python's implementation of Private Variables are very limited in their privacy
# exStak._Stack__stackList.append(82)
# print(exStak._Stack__stackList)