# highest priority items are at the front of the queue and lowest

# priority queue - binary heap -enqueue and dequeue O(logn)

#The binary heap has two common variation - min heap - smallest key in the front
#max-largest value at front

# inorder to keep the logrithamic property - it should be balanced or complete binary tree(each level has both left and right nodes)except the leaf node
# 2p = leftchild
# 2p+1 = rightchild
# single list for representing binary tree


# for new added item in max heap
#if its less than its parent , we can swap it the parent
class BinHeap:

    def __int__(self):

        self.heapList = [0]
        self.currentSize = 0

    #insertion
    def pushUP(self,i):

        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp

            i = i/2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize +1
        self.pushUP(self.currentSize)

    #delMin - take the last node in the list and replace it with the root
    # then peform push down function on the last node untill it reaches it position so that
    #heap property is satisfied

    def pushDown(self,i):
        while (i*2)<=self.currentSize:

            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp

            i = mc

    def minChild(self,i):
        if i*2+1 > self.currentSize:
            return i*2:
        else:
            if self.heapList[i*2] <self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.pushDown(1)
        return retval

    def BuildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i>0):
            self.pushDown(i)
            i = i - 1