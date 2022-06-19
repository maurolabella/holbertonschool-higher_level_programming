#!/usr/bin/python3
"""Singly linked list classes"""


class Node():
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """to set node's value"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """to retrieve node's next"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """to set node's next element"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """defines a singly linked list"""

    def __init__(self):
        """simple instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """insert nodes to the list
        in a ordered fashion from head onwards"""
        curr = self.__head
        ins = Node(value)
        if(self.__head is None):
            self.__head = ins
            return
        else:
            while curr.next_node is not None and curr.next_node.data <= value:
                curr = curr.next_node
            if(ins.data >= curr.data):
                ins.next_node = curr.next_node
                curr.next_node = ins
            else:
                self.__head = ins
                ins.next_node = curr

    def __str__(self):
        """__str__ method"""
        curr = self.__head
        txt = ""
        flag = 0
        while curr is not None:
            if flag == 0:
                txt += str(curr.data)
                flag = 1
            else:
                txt += '\n' + str(curr.data)
            curr = curr.next_node
        return txt
