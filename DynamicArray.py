import numpy as np


class DynamicArray:
    def __init__(self, size=5):
        self.__logicSize = 0
        self.__realSize = size
        self.__baseArray = np.empty(size, dtype=object)

    def append(self, item):

        if self.__realSize == self.__logicSize:
            self.resize(self.__realSize * 2)
        self.__baseArray[self.__logicSize] = item
        self.__logicSize += 1

    def pop(self):

        self.__baseArray[self.__logicSize - 1] = None
        self.__logicSize -= 1
        if self.__realSize / 2 == self.__logicSize:
            self.resize(self.__logicSize)

    def search(self, item):
        for i in range(self.__logicSize):
            if self.__baseArray[i] == item:
                return i

    def sort(self):
        for i in range(0, self.__logicSize):
            for j in range(i, self.__logicSize):
                if self.__baseArray[i] > self.__baseArray[j]:

                    aux = self.__baseArray[i]

                    self.__baseArray[i] = self.__baseArray[j]
                    self.__baseArray[j] = aux

        return str(self.__baseArray)

    def insert(self, idx, item):
        if idx >= 0 and idx < self.__logicSize:
            if self.__realSize == self.__logicSize:
                self.resize(self.__realSize * 2)

            self.__logicSize += 1

            for i in range(self.__logicSize - 1, idx - 1, -1):
                self.__baseArray[i + 1] = self.__baseArray[i]

            self.__baseArray[idx] = item
        else:
            raise Exception("Índice fuera de limites")

    def remove(self, item):
        idx = self.search(item)
        if idx:
            for i in range(idx, self.__logicSize - 1):
                self.__baseArray[i] = self.__baseArray[i + 1]
                self.__baseArray[i + 1] = None

            self.__logicSize -= 1
            return str(self.__baseArray)

    def resize(self, newsize):
        newArray = np.empty(newsize, dtype=object)
        for x in range(self.__logicSize):
            newArray[x] = self.__baseArray[x]

        self.__baseArray = newArray
        self.__realSize = newsize

    def getRealArray(self):
        return np.array2string(self.__baseArray, separator=", ")

    def getRealSize(self):
        return self.__realSize

    def __setitem__(self, idx, item):
        self.__baseArray[idx] = item

    def __getitem__(self, idx):

        if idx >= 0 and idx < self.__logicSize:
            return self.__baseArray[idx]
        else:
            raise Exception("Índice fuera de limites")

    def __str__(self):
        array = np.empty(self.__logicSize, dtype=object)
        for x in range(self.__logicSize):
            array[x] = self.__baseArray[x]

        return str(np.array2string(array, separator=", "))

    def __len__(self):
        return self.__logicSize


a = DynamicArray()

print(a)
print(a.getRealArray())
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)
print(a.getRealArray())
a.append(6)
print(a)
print(a.getRealArray())
a.pop()
print(a)
print(a.getRealArray())

a.insert(4, 10)
a.insert(0, 99)
print(a)
print(a.search(5))
a.remove(2)
print(a)
a.sort()
print(a)
