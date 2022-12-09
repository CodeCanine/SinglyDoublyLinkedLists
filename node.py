# This class can be used both as singly- and doubly linked list.
# If it is a single link, the self.prev will stay None for all Nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
