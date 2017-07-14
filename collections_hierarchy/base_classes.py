from .node import Node


class Sequenceable(object):
    def __init__(self):
        self.start = None
        self.end = None

    def get_elements(self):
        current = self.start
        lst = []
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst


class Appendable(object):
    def append(self, element):
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            # if end is not available
            # current = self.start
            # while current.next is not None:
            #     current = current.next
            # current.next = new_node
            self.end.next  = new_node
            self.end = new_node
            


class Popable(object):
    def pop(self):
        strt_node = self.start
        if strt_node is not None:
            self.start = strt_node.next
            strt_node.next = None
            return strt_node.value
        else: 
            raise IndexError()


class Pushable:
    def push(self, element):
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.next =  self.start
            self.start = new_node


