#preorder - visit root node
#followed by recursive preorder of left sub tree
#followed by recursive preorder of the right subtree

#inorder - recursive inorder on left
#visit the root node
#recursive inorder on rightsub tree

#postorder - recursive postorder on the left sub tree
#recursive postorder on the right sub tree
#visit the node

def preorder_rec(tree):

    if tree:
        print(tree.getRootVal())
        preorder_rec(tree.getLeftChild())
        preorder_rec(tree.getRightChild())

def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

def postorder_rec(tree):

    if tree:
        postorder_rec(tree.getLeftChild())
        postorder_rec(tree.getRightChild())
        print(tree.getRootVal())

def inorder_rec(tree):

    if tree:
        inorder_rec(tree.getLeftChild())
        print(tree.getRootVal())
        inorder_rec(tree.getRightChild())



