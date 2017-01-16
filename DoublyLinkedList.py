class Node(object):

    def __init__(self,data,prev,next):

        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):

    head = None
    tail = None

    def insert(self,data):
        new_node = Node(data,None,None)
        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def delete(self,node):

        current = self.head

        while current is not None:
            if current.data == node:
                if current.prev is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    self.head = current.next
                    current.next.prev = None

            current = current.next


    def Show(self):
        print "Doubly LinkedList"
        current=self.head
        while current is not None:
            print current.prev.data if hasattr(current.prev,"data") else None,
            print current.data,
            print current.next.data if hasattr(current.next,"data") else None,

            current=current.next
        print "*"*50

d = DoubleLinkedList()

d.insert(1)
d.insert(3)
d.insert(5)
d.insert(10)

d.Show()

d.delete(1)
d.delete(10)

d.Show()