# Implementation of Binary Search Tree
import queue

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

    def print_inorder(self, currentNode):
        if currentNode != None:
            self.print_inorder(currentNode.left)
            print(currentNode.data)
            self.print_inorder(currentNode.right)

    def print_postorder(self, currentNode):
        if currentNode != None:
            self.print_postorder(currentNode.left)
            self.print_postorder(currentNode.right)
            print(currentNode.data)

    def print_levelorder(self, currentNode):

        q = queue.Queue()
        q.put(currentNode)

        while not q.empty():

           node = q.get()
           if node.left is not None:
               q.put(node.left)

           if  node.right is not None:
               q.put(node.right)

           print(node.data)



    def print_tree_ALL(self):
        currentNode = self.root
        print("-----------PRE-ORDER-----------")
        self.print_preorder(currentNode)
        print("-----------IN-ORDER-----------")
        self.print_inorder(currentNode)
        print("-----------POST-ORDER-----------")
        self.print_postorder(currentNode)

a = BinarySearchTree()
a.addNode(3)
a.addNode(2)
a.addNode(10)
a.addNode(11)
a.addNode(4)
a.addNode(7)
a.addNode(8)
a.addNode(2)
a.addNode(1)
a.addNode(1)
#a.print_tree_ALL()
a.print_levelorder(a.root)
