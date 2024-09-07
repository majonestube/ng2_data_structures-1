# Imports
from __future__ import annotations  # Needed for typing Node class

import warnings
from typing import Any

import binarytree
import heapdict


# Node class (do not change)
class Node:
    def __init__(self, data: Any = None, next: None | Node = None):
        self.data = data
        self.next = next


# Add your implementations below


class Stack:
    def __init__(self):
        """Initialize stack object, with head attribute"""
        self.head = None
        self.size = 0

    def push(self, data: Any) -> None:
        """Add new node with data to stack"""
        new = Node(data=data, next=self.head)
        self.head = new 
        self.size += 1

    def peek(self) -> Node | None:
        """Return data from node on top of stack, without changing stack"""
        return self.head.data

    def pop(self) -> Node:
        """Remove last added node and return its data"""
        if self.size == 0:
            raise IndexError
        else:
            removed = self.head 
            self.head = self.head.next
            self.size -= 1
            return removed.data


class Queue:
    def __init__(self):
        """Initialize queue object with head and tail"""
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data: Any) -> None:
        """Add node with data to queue"""
        new = Node(data=data, next = None)
        if self.size == 0:
            self.head = self.tail = new
        else:
            temp = self.tail 
            temp.next = new 
            self.tail = new 
        self.size += 1


    def peek(self) -> Node | None:
        """Return data from head of queue without changing the queue"""
        return self.head.data

    def dequeue(self) -> Node:
        """Remove node from head of queue and return its data"""
        if self.size == 0:
            raise IndexError
        else: 
            removed = self.head 
            self.head = removed.next 
            self.size -= 1
            return removed.data


class EmergencyRoomQueue:
    def __init__(self):
        """Initialize emergency room queue, use heapdict as property 'queue'"""
        self.queue = heapdict.heapdict()

    def add_patient_with_priority(self, patient_name: str, priority: int) -> None:
        """Add patient name and priority to queue

        # Arguments:
        patient_name:   String with patient name
        priority:       Integer. Higher priority corresponds to lower-value number.
        """
        self.queue[patient_name] = priority

    def update_patient_priority(self, patient_name: str, new_priority: int) -> None:
        """Update the priority of a patient which is already in the queue

        # Arguments:
        patient_name:   String, name of patient in queue
        new_priority:   Integer, updated priority for patient

        """
        self.queue[patient_name] = new_priority

    def get_next_patient(self) -> str:
        """Remove highest-priority patient from queue and return patient name

        # Returns:
        patient_name    String, name of patient with highest priority
        """
        (name, priority) = self.queue.popitem()
        return name

class BinarySearchTree:
    def __init__(self, root: binarytree.Node | None = None):
        """Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of binarytree.Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a binary search tree (see property binarytree.Node.is_bst ). If not, raise
        ValueError.
        """
        if root: 
            if root.is_bst == False:
                raise ValueError
        self.root = root 


    def insert(self, value: float | int) -> None:
        """Insert a new node into the tree (binarytree.Node object)

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """
        new = binarytree.Node(value=value)
        if self.root is None:
            self.root = new 
        else: 
            placed = False 
            current = self.root
            while not placed: 
                if current.value == new.value:
                    warnings.warn("This value already excists in the tree.")
                    placed = True
                else:
                    if new.value < current.value:
                        if current.left == None:
                            current.left = new
                            placed = True 
                        else: 
                            current = current.left 
                    else: 
                        if current.right == None:
                            current.right = new
                            placed = True 
                        else: 
                            current = current.right 




    def __str__(self) -> str | None:
        """Return string representation of tree (helper function for debugging)"""
        if self.root is not None:
            return str(self.root)



