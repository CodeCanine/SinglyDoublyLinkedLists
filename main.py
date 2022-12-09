# Personal project, to practice the linked list data structure, and OOP methods.
# n = # of nodes
# Space complexity = O(n)
# Time complexity = O(n)
# (For most of the methods)

from singlylinkedlist import *
from doublylinkedlist import *

if __name__ == '__main__':
    # Singly Linked List
    sl1 = SinglyLinkedList()
    # Asking for input, and creating the nodes of the SLL
    elements = input("Enter the elements of the Singly Linked List: ").split()
    for i in range(len(elements)):
        data = elements[i]
        head = sl1.insert(data)
    print("Singly Linked List:")
    sl1.print_forward()
    insert_value = input("\nInsert a value: ")
    sl1.insert(insert_value)
    print("\nAfter insertion:")
    sl1.print_forward()
    print("\nAfter removing the duplicates (if any):")
    sl1.delete_duplicates()
    sl1.print_forward()

    # Doubly Linked List
    dl1 = DoublyLinkedList()
    dl1.insert_begin(10)
    dl1.insert_begin(20)
    dl1.insert_begin(30)
    dl1.insert_begin(10)
    dl1.insert_end(30)
    dl1.insert_end(30)
    dl1.insert_end(40)
    dl1.insert_after(2, 40)
    dl1.insert_before(3, 40)
    print("\nDoubly Linked List Forwards: ")
    dl1.print_forward()
    print("\nDoubly Linked List Backwards: ")
    dl1.print_reverse()

    dl1.del_by_value(20)
    print("\nRemoving the duplicates:")
    dl1.delete_duplicates()
    dl1.print_forward()
