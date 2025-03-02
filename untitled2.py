# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u1e2myoEMS-za_Nz2kN8KABgZZmanOKe
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtPosition(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1
        if current is None:
            print(f"Cannot insert at position {index}, index is out of bounds")
        else:
            new_node.next = current.next
            current.next = new_node

    def removeAtBeginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def removeAtEnd(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def removeAtPosition(self, index):
        if not self.head:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1
        if current is None or current.next is None:
            print(f"Cannot remove at position {index}, index is out of bounds")
        else:
            current.next = current.next.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.addAtBeginning(1)
ll.addAtEnd(3)
ll.addAtPosition(1, 2)
ll.display()

ll.removeAtBeginning()
ll.display()

ll.removeAtEnd()
ll.display()

ll.addAtEnd(4)
ll.addAtEnd(5)
ll.removeAtPosition(1)
ll.display()