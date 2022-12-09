# Methods for the Singly Linked List data structure

from node import *
# Importing DoublyLinkedList, as its methods can be overwritten here, or used as is
# Due to Singly Linked List is more primitive (no previous node handling)
from doublylinkedlist import DoublyLinkedList


class SinglyLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.head = None

    def insert(self, data):
        # Initializing the new Node
        new_node = Node(data)
        # If the LL is empty
        if self.head is None:
            self.head = new_node
        # Or there is only 1 element in the SLL
        elif self.head.next is None:
            self.head.next = new_node
        # Or if there are multiple elements in the SLL
        else:
            # Running variable
            current = self.head
            # Traverse through the SLL until the end
            while current.next is not None:
                current = current.next
            # And add the new_node as the last element
            current.next = new_node

    # Just a slight modification of <-> to -> from parent (DoublyLinkedList) class
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty!")
            return
            # Running variable
        current = self.head
        # Until there are elements in the SLL, traverse through them, and print its data
        while current is not None:
            # end=" " keeps the cursor in same line
            if current.next is not None:
                print(current.data, " -> ", end=" ")
                current = current.next
            # If it is the last node, print its data, but without ->, for visuals
            else:
                print(current.data)
                current = current.next

    def delete_duplicates(self):
        # Initializing running variable with the first element of the SLL
        current = self.head
        # Initializing running variable, to be able to chain new nodes together
        prev = None
        # Initializing set to keep track of traversed non-duplicate Nodes
        # Set is faster than list(), and indexing is not required for this approach
        non_duplicate_set = set()
        # Until there are elements in the SLL
        while current:
            # If the current element is not a duplicate
            if current.data not in non_duplicate_set:
                # Add it to the non-duplicate set()
                non_duplicate_set.add(current.data)
                # Switch the comparison variable's value to the current node
                prev = current
            # If the current element is in the non-duplicate set()
            else:
                # A duplicate is found, reassign the previous Node's next pointer
                # to current's next pointer (thus de-duplicating).
                prev.next = current.next
            # Check the next element
            current = current.next
