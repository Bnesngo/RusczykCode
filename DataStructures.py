class baseDS:
    _data = []
    count = 0
    def get(self, location):
        return data[location]
    def sort(self):
        data.sort()
    def find(self, i):
        try:
            return data.index(i)
        except:
            return -1

class Queue(baseDS):
    def addToBack(self, item):
        data.append(item)
        count = count + 1
    def removeFromFront(self):
        data.remove(data[0])
        count = count - 1

class Bag(baseDS):
    def add(self, item):
        data.append(item)
        count = count + 1       

class Stack(baseDS):
    def addToTop(self, item):
        data.append(item)
        count = count + 1
    def removeFromTop(self):
        data.remove(data[count-1])
        count = count - 1;

class DoubleEndedQueue(baseDS):
    def addToBack(self, item):
        data.append(item)
        count = count + 1
    def removeFromFront(self):
        data.remove(data[0])
        count = count - 1
    def removeFromBack(self):
        data.pop()
        count = count - 1
    def addToFront(self, item)
        data.insert(0, item)
        count = count + 1
