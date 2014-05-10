"""
testing queue location
"""
__author__ = 'Naoto'

class Queue:

    class Node:
        def __init__(self, value, next, prev):
            self.value = value
            self.next = next
            self.prev = prev


    ##Node###           ##Node###
    # value #           # value #
#|--# prev  # <-------  # prev  # <-------
    # next  # ------->  # next  # ------->
    #########           #########

    def __init__(self):
        self.front = None
        self.tail = None
        self.front = self.Node(None, self.tail, None)
        self.tail = self.Node(None, None, self.front)
        self.size = 0

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            result = self.front.next.value
            temp = self.front.next
            temp.next.prev = self.front
            self.front.next = temp.next
            temp.value = None
            temp.next = None
            temp.prev = None
            self.size -= 1
            return result

    def enqueue(self, new_obj):
        new_node = self.Node(new_obj, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def make_empty(self):
        while self.size > 0:
            self.dequeue()