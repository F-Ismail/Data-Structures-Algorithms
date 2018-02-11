#Implementation of a linked list:

class Node(object):

    def __init__(self, data):
       self.Data = data
       self.next = None
       self.prev = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        print("Linked List Created!")

    def addNode(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def printList(self):

        currentHead = self.head
        while currentHead != None:
            print(currentHead.Data)
            currentHead = currentHead.next


l = LinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(10)
l.printList()
