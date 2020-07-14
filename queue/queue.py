"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# import sys
# sys.path.append("../singly_linked_list/singly_linked_list")
# from singly_linked_list import LinkedList


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        # returns the node's data
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    '''
    Adds `data` to the end or the begining of the LinkedList 
   is O(1)  
   removing data from the end of the linked list is O(n)
    '''

    def add_to_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_tail(self):
        if self.head is None:
            return None
        # save the tail Node's data
        node_value = self.tail.get_value()

    #   if there is only one node in the list
        if self.head == self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:

            current = self.head

            # before the tail Node
            while current.get_next() != self.tail:
                current = current.get_next()

            self.tail = current

        return node_value

    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.get_value()

        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:

            self.head = self.head.get_next()

        return data

    def contains(self, data):

        if not self.head:
            return False

        current = self.head

        while current is not None:

            if current.get_value() == data:
                return True

            current = current.get_next()

        return False

    def get_max(self):
        if self.head is None:
            return None

        max = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max:
                max = current.get_value()

            current = current.get_next()

        return max


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()  # LinkedList

    def __len__(self):
        return self.size

    def enqueue(self, value):

        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()
