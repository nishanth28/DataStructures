class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,inItem):
        return self.items.append(inItem)

    def pop(self):
        return self.items.pop()     #self.items[len(self.items)-1]

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print s.peek()
