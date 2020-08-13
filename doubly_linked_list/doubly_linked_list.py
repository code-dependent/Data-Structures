"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, nextnode=None):
        self.prev = prev
        self.value = value
        self.next = nextnode


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
            self.head = node
            self.tail = node
            self.length+=1
        else:
            bumpedhead = self.head
            self.head = node
            self.head.next = bumpedhead
            bumpedhead.prev = self.head
            self.length+=1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return
        elif self.head == self.tail:
            val = self.head.value
            self.tail = None
            self.head = None
            self.length = 0
            return val
        else:
            to_be_removed = self.head.value
            self.head = self.head.next
            self.length-= 1
            self.head.prev = None
            return to_be_removed

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newtail = ListNode(value)
        if self.length == 0:
            self.tail = newtail
            self.head = newtail
            self.length += 1
        else:
            prvtail = self.tail
            self.tail = newtail
            self.tail.prev = prvtail
            prvtail.next = self.tail
            self.length += 1



    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return
        elif self.tail == self.head:
            val = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return val.value
        else:
            val = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return val.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            self.delete(node)
            self.add_to_head(node.value)


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return
        elif node == self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.tail == self.head:
            self.tail = None
            self.head = None
            self.length = 0
        elif node == self.tail:
            self.remove_from_tail()
        elif node == self.head:
            self.remove_from_head()
        else:
            prv = node.prev
            nxt = node.next
            prv.next = nxt
            nxt.prev = prv
            self.length-=1



    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head == self.tail:
            return self.head.value
        elif self.length == 0:
            return
        else:
            max_val = self.head.value
            curr = self.head.next
            while curr is not None:
                if max_val < curr.value:
                    max_val = curr.value
                curr = curr.next
            return max_val