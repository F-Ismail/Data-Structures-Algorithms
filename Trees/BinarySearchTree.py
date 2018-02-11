# Implementation of Binary Search Tree

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        print("Binary Search Tree Created!")

    def addNode(self, data):

        node = Node(data)

        if self.root == None:
            self.root = node
        else:
            currentHead = self.root
            prevHead = currentHead
            while currentHead != None:
                prevHead = currentHead
                if node.data >= currentHead.data:
                    currentHead = currentHead.right
                else:
                    currentHead = currentHead.left

            if node.data >= prevHead.data:
                prevHead.right = node
            else:
                prevHead.left = node

    def print_preorder(self, currentNode):
        if currentNode != None:
            print(currentNode.data)
            self.print_preorder(currentNode.left)
            self.print_preorder(currentNode.right)

    def pre_order(self):
        currentNode = self.root
        self.print_preorder(currentNode)

    def print_tree(self):
        node = self.root
        print(node.data)
        self.print_left(node.left)
        self.print_right(node.right)

a = BinarySearchTree()
a.addNode(3)
a.addNode(2)
a.addNode(10)
a.addNode(11)
a.addNode(4)
a.addNode(7)
a.addNode(8)
a.pre_order()
