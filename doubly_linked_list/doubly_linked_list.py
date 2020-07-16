"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            new_node.prev = None
            self.head = new_node
            self.length += 1
        else:
            new_node = ListNode(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None

        if self.head:
            cur = self.head.next
            cur.prev = None
            self.head = cur

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            new_node.prev = None
        else:
            new_node = ListNode(value)

            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        cur = self.head
        if not cur.next:
            cur = None
            self.head = None
            return
        else:
            while cur.next:
                cur = cur.next
            
            prev = cur.prev
            prev.next = None
            cur = None
            return

    def print_l(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next


dll = DoublyLinkedList()
dll.add_to_tail("A")
dll.add_to_tail("B")
dll.add_to_tail("C")
dll.add_to_tail("D")
print("before")
dll.print_l()
print("after")
dll.remove_from_tail()
dll.print_l()

# """
# Removes the input node from its current spot in the
# List and inserts it as the new head node of the List.
# """

# def move_to_front(self, node):
#     pass

# """
# Removes the input node from its current spot in the
# List and inserts it as the new tail node of the List.
# """

# def move_to_end(self, node):
#     pass

# """
# Deletes the input node from the List, preserving the
# order of the other elements of the List.
# """

# def delete(self, node):
#     pass

# """
# Finds and returns the maximum value of all the nodes
# in the List.
# """

# def get_max(self):
#     pass
