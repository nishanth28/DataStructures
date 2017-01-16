#use list data structure for python

#key insight is stacks reverse order. soo using stack on a stack reverse the reversed order to give the original order.

class Queue2Stack(object):

    def __init__(self):

        self.inStack = []
        self.outStack = []

    def enqueue(self,item):

         return self.inStack.append(item)

    def dequeue(self):

        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack.pop()