class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

# imagine a block which is n-node wide. we could walk this "block" all the way down the list, and once the front of the block reached the end, then the other end of the block would be the nth node!
# left and right pointer
# n block

def nth_to_last_node(n,head):

    left = head
    right = head

    for i in xrange(n-1):

        if not right.nextnode:
            raise LookupError('Error')

        right=right.nextnode

    while right.nextnode:
        left=left.nextnode
        right=right.nextnode

    return left