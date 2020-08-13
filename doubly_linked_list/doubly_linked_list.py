"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, nextnode=None):
        self.prev = prev
        self.value = value
        self.next = nextnode

    # def set_prev(self, node):
    #     self.prev = node
    # def get_prev(self):
    #     return self.prev

    # def set_next(self, node):
    #     self.next = node
    # def get_next(self):
    #     return self.next

    # def set_value(self,val):
    #     self.value = val
    # def get_value(self):
    #     return self.value


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
        node = ListNode(value)
        if self.length == 0:
            self.tail = node
            self.head = node
            self.length+= 1
        else:
            self.length+= 1
            prvhead = self.head
            self.head = node
            self.head.next = prvhead
            prvhead.prev = self.head

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.head == self.tail:
            val = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return val.value

        val = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length-=1
        return val.value
    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length+=1

        else:
            prvtail = self.tail
            self.tail = node
            prvtail.next = self.tail
            self.tail.prev = prvtail
            # self.tail.next = None
            self.length+=1


    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        if self.tail == self.head:
            val = self.tail.value
            self.tail = None
            self.head = None
            self.length = 0
            return val
        else:
            val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length-=1
            return val

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 1 or self.head == node:
            return None
        elif self.tail == node:
            self.remove_from_tail()
            self.add_to_head(node.value)
            # print(self.head.value)

        else:
            self.delete(node)
            self.add_to_head(node.value)
            # nxt = node.next
            # prv = node.prev
            # prv.next = nxt
            # nxt.prev = prv
            # node.next = self.head.next
            # self.head = node
            # self.head.prev = None
            ## print(self.head.value)


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length <= 1 or self.tail == node:
            return None
        elif self.head == node:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            nxt = node.next
            prv = node.prev
            prv.next = nxt
            nxt.prev = prv
            node.prev = self.tail
            self.tail = node
            self.tail.next = None

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head:

            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            prv = node.prev
            nxt = node.next
            nxt.prev = prv
            prv.next = nxt
            self.length -= 1
# def delete(self, node):
#         # one node in list
#         if self.length == 1:
#             # update head and tail to None
#             self.head = None
#             self.tail = None
#             # update length (empty)
#             self.length = 0
#         # if node is head
#         elif node == self.head:
#             # remove head
#             self.remove_from_head()
#         # if node is tail
#         elif node == self.tail:
#             # remove tail
#             self.remove_from_tail()
#         else:
#             # references to previous and next node of passed in node
#             next_node = node.next
#             prev_node = node.prev
#             # update next node's previous to current's previous
#             next_node.prev = prev_node
#             # update previous node's next to current's next
#             prev_node.next = next_node
#             # update length (decrease)
#             self.length -= 1




    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head == self.tail:
            return self.head.value
        if not self.head:
            return None
        max_value = self.tail.value
        curr = self.tail.prev
        while curr:
            if curr.value > max_value:
                max_value = curr.value
            print(curr.value)
            curr = curr.prev
        return max_value