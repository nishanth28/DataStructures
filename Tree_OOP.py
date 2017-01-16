#representing tree using nodes and references

class BinaryTree(object):

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None

    def insert_left(self,newNode):

        # when there is no left child, simply add the binary node
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:

        #when there is node, insert a node and push the node 1 level down
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t


    def insert_right(self,newNode):

# when there is no right child, simply add the binary node
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:

        #when there is node, insert a node and push the node 1 level down
            t = BinaryTree(newNode)
            t.rightchild = self.leftchild
            self.rightchild = t


    def getRight(self):
        return self.rightchild

    def getLeft(self):
        return self.leftchild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


