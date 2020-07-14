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

    def add_to_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def contains(self, value):
        if self.head is None:
            f"There is no items in the list"
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.next
        return False


ll = LinkedList()
ll.add_to_tail("A")
ll.add_to_tail("B")
ll.add_to_tail("C")
ll.add_to_tail("D")
ll.print_list()
print(ll.contains("D"))
