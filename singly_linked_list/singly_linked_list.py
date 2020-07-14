class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


# add item


    def add_to_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


# contains


    def contains(self, value):
        if self.head is None:
            print("There is no items in the list")
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def remove_head(self):
        current_node = self.head
        if self.head is None:
            print("The list is empty")

        current_node = current_node.next
        self.head = current_node


ll = LinkedList()
ll.add_to_tail("A")
ll.add_to_tail("B")
ll.add_to_tail("C")
ll.add_to_tail("D")
print("before delete")
ll.print_list()
print("delete")
ll.remove_head()
ll.print_list()

print("delete")
ll.remove_head()
ll.print_list()
