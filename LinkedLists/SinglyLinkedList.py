"""
INFO:
Implementation of Singly Linked Lists.

Function Requirements:
    1) Done - Linked List Insertion
    2) Done - Linked List Deletion
    3) Done - Linked List Search
    4) Done - Linked List Print (Iterative)
"""

class Node():
    def __init__(self, x):
        self.data = x
        self.next = None

class SinglyLinkedList():

    def __init__(self):
        print("Linked List Initialized!")
        self.head = None

    def insert(self, x):

        if self.head is None:
            self.head = Node(x)
        else:
            newNode = Node(x)
            newNode.next = self.head
            self.head = newNode

    def delete(self, x):

        currentNode = self.head
        nextNode = currentNode.next

        if currentNode.data == x:
            self.head = nextNode
            return

        while nextNode is not None:
            if nextNode.data == x:
                currentNode.next = nextNode.next
                del(nextNode)
                return

            currentNode = currentNode.next
            nextNode = nextNode.next

        return

    def printList(self):

        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

def main():
    myList = SinglyLinkedList()
    for i in range(10):
        myList.insert(i)

    myList.printList()
    print("---------------------")
    myList.delete(12)
    myList.delete(4)
    myList.printList()

main()
