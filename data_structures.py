# UiT DTE-2602 Fall 2023
# Assignment 2: Data structures

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 


class Stack:
    def __init__(self):
        """ Initialize stack """
        pass    # Placeholder, remove when implementing your code

    def push(self,data):
        """ Add new node with data to stack """
        pass    # Placeholder, remove when implementing your code
    
    def pop(self):
        """ Return data of last added node """
        pass    # Placeholder, remove when implementing your code


class Queue:
    def __init__(self):
        """ Initialize queue """
        pass

    def enqueue(self,data):
        """ Append node with given data to queue tail """
        pass

    def dequeue(self):
        """ Remove node from queue head and return node data """
        pass


class IndexList:
    def __init__(self):
        """ Initialize IndexList """
        pass

    def append(self, data):
        """ Create new node with data and append to tail end of list"""
        pass

    def insert_before(self, data, index):
        """ Create new node with data and insert before node at given index """
        pass

    def pop(self, index):
        """ Remove and return data of node at given index """
        pass