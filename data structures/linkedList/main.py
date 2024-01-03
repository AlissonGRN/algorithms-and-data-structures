from node import Node

class LinkedList:

    def __init__(self) -> None:

        self.head = None # initialize the head of the list pointing to none

    def addToStart(self, data):
        '''Add a node on the beggining of the list'''

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addToEnd(self, data):
        '''Add a node to the end of the list'''

        pass