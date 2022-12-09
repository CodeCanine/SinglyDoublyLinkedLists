# Methods for the Doubly Linked List data structure

from node import *


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        current = self.head
        # Until there are elements in the DLL, traverse through them, and print its data
        while current is not None:
            # end=" " keeps the cursor in same line
            if current.next is not None:
                print(current.data, " <-> ", end=" ")
                current = current.next
            # If it is the last node, print its data, but without <->, for visuals
            else:
                print(current.data)
                current = current.next

    def print_reverse(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        current = self.head
        # Traversing through all nodes to the last one
        while current.next is not None:
            current = current.next
        # Printing the tail, then traversing backwards, printing all the nodes in reverse order
        while current is not None:
            # end=" " keeps the cursor in same line
            if current.prev is not None:
                print(current.data, " <-> ", end=" ")
                current = current.prev
            # If it is the last node, print its data, but without >->, for visuals
            else:
                print(current.data)
                current = current.prev

    def insert_begin(self, data):
        # Initializing new node
        new_node = Node(data)
        # If the DLL is empty, add the new node to the beginning
        if self.head is None:
            self.head = new_node
            return
        # If it is not, the new_node's next pointer must refer to the head
        new_node.next = self.head
        # The original head's previous pointer must refer to the new node
        self.head.prev = new_node
        # And the new_node must be the new head
        self.head = new_node

    def insert_end(self, data):
        # Initializing new node
        new_node = Node(data)
        # If the DLL is empty, add the new node to the beginning
        if self.head is None:
            self.head = new_node
            print("List is empty, adding element to the beginning!")
            return
        # If it is not, traverse through all the nodes with a running variable
        current = self.head
        while current.next is not None:
            current = current.next
        # The last node's next pointer must refer to the new node
        current.next = new_node
        # And the new_node's previous pointer must refer to the previous last node
        new_node.prev = current

    def insert_after(self, data, x):
        # Initializing new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("List is empty, adding element to the beginning!")
            return
        # Initializing running variable
        current = self.head
        # Start traversing through the DLL
        while current is not None:
            # If the value to be inserted after is found, jump out of the loop and continue
            if x == current.data:
                break
            # If not, continue to traverse
            current = current.next
        if current is None:
            print("Node is not present!")
            return
        # If the node to be inserting after is found
        else:
            # The new_node's next pointer must refer to the current's next pointer
            new_node.next = current.next
            # And the new_node's previous pointer must refer to the current node
            new_node.prev = current
            # If it is not the last node
            if current.next is not None:
                # The node before we insert the new_node, must refer to the new_node
                current.next.prev = new_node
            # If it is, insert it to the tail, and set the current's next pointer to the new node
            current.next = new_node

    def insert_before(self, data, x):
        # Initializing new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("List is empty, adding element to the beginning!")
            return
        # Initializing running variable
        current = self.head
        # Start traversing through the DLL
        while current is not None:
            # If the value to be inserted before is found, jump out of the loop and continue
            if x == current.data:
                break
            current = current.next
        if current is None:
            print("Node is not present!")
            return
        # If the node to be inserting before is found
        else:
            # The new_node's next pointer must refer to the current
            new_node.next = current
            # And the new_node's previous pointer must refer to the current's previous node
            new_node.prev = current.prev
            # If it is not the first node
            if current.prev is not None:
                # The previous node's next pointer must refer to the new node
                current.prev.next = new_node
            else:
                # If it is, insert to the head
                self.head = new_node
            # And the current's previous pointer to the new_node/new_head
            current.prev = new_node

    def del_by_value(self, value):
        # Single element
        if self.head is None:
            print("Linked list is empty!")
            return
        # Initializing running variable
        current = self.head
        # Edge case -> Only 1 element in the DLL
        if current.next is None:
            # And it matches the value to be deleted
            if value == current.data:
                # Set the head to None, thus emptying the list
                self.head = None
                print("Linked list is now empty!")
            # If the value does not match any of the list's elements
            else:
                print(value, " Is not present!")
            # In both cases we can return, to avoid duplicate code, one return is enough
            return

        # Multiple elements
        # Edge case -> deleting the head
        # As the current still points to self.head, if the value to be deleted is the head
        if current.data == value:
            # Set the head as its next neighbour
            self.head = self.head.next
            # And its previous pointer to None
            self.head.prev = None
            return
            # Edge case -> Value in the middle, or the end
        # Start traversing through the DLL
        while current.next is not None:
            # If the value to be deleted is found
            if value == current.data:
                # Jump out of the loop, and continue
                break
            # If not, continue to traverse
            current = current.next
        # Edge case -> Middle element
        if current.next is not None:
            # The next node's previous pointer must refer to the previous node
            current.next.prev = current.prev
            # The previous node's next pointer must refer to the next node
            current.prev.next = current.next
            # This removes the element from the DLL
        # Edge case -> Tail, or not found
        else:
            # If it is the tail
            if current.data == value:
                # The previous node's next pointer must refer to None
                current.prev.next = None
            else:
                print(value, "is not present in List")

    def delete_duplicates(self):
        if self.head is None:
            print("Linked List is empty!")
            return
            # Initialize running variable
        current = self.head
        # Nested loops, to compare all elements with upcoming elements
        while current:
            # Another helper variable for brevity
            index = current.next
            while index:
                # If the data of the current Node is equal to the data of the upcoming node's
                if current.data == index.data:
                    # Switch the pointers
                    index.prev.next = index.next
                    #
                    #      current                index               index.next
                    #  --- ------ ---         --- ------ ---        --- ------ ---
                    # | p | data | n | <---> | p | data | n | <---> | p | data | n |
                    #  --- ------ ---         --- ------ ---        --- ------ ---
                    #
                    # And if it is not the last one, change the previous pointer as well
                    if index.next is not None:
                        index.next.prev = index.prev
                # Compare current with the next node
                index = index.next
            # Step to the next node, to start comparing again
            current = current.next
