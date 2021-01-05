#!/usr/bin/python3
""" linked list with python"""


class Node:
    """ Node Class """

    def __init__(self, data, next_node=None):
        """ Init node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ return data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set data """
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ point to next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set next node """
        if not isinstance(value, Node) and value != None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ linked list class """

    def __init__(self):
        """ init linked list """
        self.__head = None

    def sorted_insert(self, value):
        """ sort insert """
        pass
