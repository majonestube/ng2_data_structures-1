# Imports
import pytest
import heapdict
import warnings
import binarytree

# Node class
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 

# Add your implementations below and commit and push the file to your repository
# (uit-dte-2602-f23/data-structures-<your github username>)
# Every "pass" command should be replaced with your own code.

class Stack:
    def __init__(self):
        """ Initialize stack object, with head attribute """
        pass

    def push(self,data):
        """ Add new node with data to stack """
        pass

    def peek(self):
        """ Return data from node on top of stack, without changing stack """
        pass

    def pop(self):
        """ Remove last added node and return its data """
        pass


class Queue:
    def __init__(self):
        """ Initialize queue object with head and tail """
        pass

    def enqueue(self,data):
        """ Add node with data to queue """
        pass

    def peek(self):
        """ Return data from head of queue without changing the queue """
        pass
            
    def dequeue(self):
        """ Remove node from head of queue and return its data """
        pass
        

class EmergencyRoomQueue:
    def __init__(self):
        """ Initialize emergency room queue, use heapdict as property 'queue' """
        pass

    def add_patient_with_priority(self,patient_name,priority):
        """ Add patient name and priority to queue 
        
        # Arguments:
        patient_name:   String with patient name
        priority:       Integer. Higher priority corresponds to lower-value number.
        """
        pass

    def update_patient_priority(self,patient_name,new_priority):
        """ Update the priority of a patient which is already in the queue 
                
        # Arguments:
        patient_name:   String, name of patient in queue
        new_priority:   Integer, updated priority for patient
        """
        pass

    def get_next_patient(self):
        """ Remove highest-priority patient from queue and return patient name 
        
        # Returns:
        patient_name    String, name of patient with highest priority
        """
        pass
    

class IndexList:
    def __init__(self):
        """ Create IndexList object with head """
        pass
     
    def insert(self, data, index):
        """ Create new node with data and insert at given index 
        
        # Arguments:
        data:       Content of node to be inserted
        index:      Index of node to be inserted. The node is inserted into the list 
                    before any existing nodes with the given index.
                    Index must be an integer in the range [0,1,...,N]
                    where N is the number of elements in the list.
                    If the list is empty, insert(data,0) creates the first node.
                    If index == N, the node is inserted after the last node in the list.
                    If index > N, an IndexError is raised.
        """
        pass

    def peek(self,index):
        """ Return data of node at given index without changing list """
        pass

    def pop(self, index):
        """ Remove and return data of node at given index """
        pass

    def __str__(self):
        """ String representation of list (helper method for debugging)"""
        # No need to change this method
        list_string = ''
        current = self.head
        index = 0
        while current is not None:
            list_string += str(current.data) + f'({index}) -> '
            current = current.next
            index += 1
        return list_string
    

class BinarySearchTree:
    def __init__(self,root=None):
        """ Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of binarytree.Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a binary search tree (see property binarytree.Node.is_bst ). If not, raise ValueError.
        """
        pass 
    
    def insert(self, value):
        """ Insert a new node into the tree (binarytree.Node object)

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """
        pass

    def __str__(self):
        """ Return string representation of tree (helper function for debugging) """
        if self.root:
            return(str(self.root))
        