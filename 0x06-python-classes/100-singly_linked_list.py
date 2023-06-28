#!/usr/bin/python3
"""Singly linked list class
"""


class SinglyLinkedList:
    """represents a Singly linked list"""

    def __init__(self):
        """Initialize the list"""
        self.__head = None

    def sorted_insert(self, value):
        """sort the linked list

        Args:
            value (int): data of the node
        """
        newNode = Node(value)
        if not self.__head:
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            newNode.next_node = tmp.next_node
            tmp.next_node = newNode

    def __str__(self):
        """print the linked list

        Returns:
            string: the data of each node
        """
        tmp = self.__head
        link = ""
        while tmp is not None:
            link += str(tmp.data)
            if tmp.next_node is not None:
                link += "\n"
            tmp = tmp.next_node
        return link


"""Node class
"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize the node

        Args:
            data (int): data of the node
            next_node (Node): next node . Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data of the node.

        Returns:
            int: data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """set data

        Args:
            value (int): data to set.

        Raises:
            TypeError: value must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next node

        Returns:
            Node: the next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next node

        Args:
            value (Node): next node's object

        Raises:
            TypeError: value must be a Node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
