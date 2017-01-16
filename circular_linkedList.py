class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

# mark 1 and mark 2 : mark 2 traverses 2 times faster than mark1 and if the order it matches the value with mark1:then linkedlist is circular
def cycle_check(node):

    mark1 = node
    mark2 = node

    while mark2 != None and mark2.next!=None:

        mark1 = mark1.next
        mark2 = mark2.next.next

        if mark2 == mark1:
            return True

    return False


