# list of list tree
#first value is the root node
#second value is the left node
#Third value is the right node
#[] represents the empty array - no children

'''myTree = ['a',#root
             ['b', #left subtree
                ['d',[],[]]],
                ['c',#right subtree]'''

def BinaryTree(r):

    return [r,[],[]]

def insert_left(root,newBranch):
    t = root.pop(1) # pop out left child

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insert_right(root,newBranch):
    t = root.pop(2)  #pop out right child

    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootValue(root):
    return root[0]

def setRootValue(root,newVal):
    root[0] = newVal

def getChild_left(root):
    return root[1]

def getChild_right(root):
    return root[2]


r = BinaryTree(3)
print insert_left(r,2)
print insert_right(r,4)