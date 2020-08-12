
class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node

    def get_val(self):
        return self.val

    def set_next(self, new_next_node):
        self.next_node = new_next_node

    def get_next(self):
        return self.next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):

        new_node = Node(value)
        if self.tail is None and self.head is None:
            self.head = new_node

            self.tail = new_node
        else:

            self.tail.set_next(new_node)

            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        curr = self.head

        if self.head is self.tail:
            val = self.tail.get_val()
            self.tail = None
            self.head = None
            return val

        while curr.get_next() and curr.get_next() is not self.tail:
            curr = curr.get_next()

        val = self.tail.get_val()

        self.tail = curr
        self.tail.set_next(None)


        return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        if not self.head.get_next():
            head = self.head.get_val()
            self.head = None
            self.tail = None
            return head

        val = self.head.get_val()
        self.head = self.head.get_next()
        return val

    def contains(self, value):
        if not self.head:
            return False

        curr = self.head
        while curr:
            if curr.get_val() is value:
                return True
            curr = curr.get_next()
        return False

    # def get_max(self):
    #     if not self.head:
    #         return None
    #     max_value = self.head.get_val()
    #     current = self.head.get_next()
    #     while current:
    #         if current.get_val() > max_value:
    #             max_value = current.get_val()
    #         current = current.get_next()

    #     return max_value

    def is_empty(self):
        return self.head is None and self.tail is None
    def length(self):
        if self.tail is None and self.head is None:
            return 0
        if self.tail is self.head:
            return 1

        counter = 0
        curr = self.head
        while curr is not None:

            counter+=1
            curr = curr.get_next()

        return counter