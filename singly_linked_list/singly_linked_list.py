class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


# add item


    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        current_node = self.tail
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


# contains


    def contains(self, value):
        if self.head is None:
            print("There is no items in the list")
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False


# remove the node from the head


    def remove_head(self):
        current_node = self.head
        if self.head is None:
            print("The list is empty")

        current_node = current_node.next
        self.head = current_node

    def get_max(self):
        if self.head is None:
            return None

        # get the value of the head
        max_value = self.head.value

        # get the value of the next node
        current_node = self.head.next


        # if the next of the current_value not none
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value

            current_node = current_node.next

        return max_value


ll = LinkedList()
ll.add_to_tail(10)
ll.add_to_tail(20)
ll.add_to_tail(30)
ll.add_to_tail(40)
print("before delete")
ll.print_list()
print("delete")
ll.remove_head()
ll.print_list()

print("delete")
ll.remove_head()
ll.print_list()
print(ll.get_max())
