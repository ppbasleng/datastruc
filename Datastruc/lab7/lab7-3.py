class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.lowernode = None
        self.counter = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            fp = None
            p = self.root
            while p :
                fp = p
                p = p.left if data<p.data else p.right
            if data < fp.data:
                fp.left = Node(data)
            else:
                fp.right = Node(data)
        if data<=self.lowernode:
            self.counter+=1
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,T.lowernode = input('Enter Input : ').split("/")
T.lowernode = int(T.lowernode)
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print(T.counter)