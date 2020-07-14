# School method
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


'''
# This is my way
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
        if current_node:
            self.head = current_node.next
            return current_node.next.value

        return self.head.value

#         current_node = self.head
#         if self.head is None:
#            current_node = current_node.next
#            self.head = current_node

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
# print(ll.get_max())
'''
