# Imports
from __future__ import annotations  # Needed for typing Node class

import warnings
from typing import Any



# Node class (do not change)
class Node:
    def __init__(self, data: Any = None, next: None | Node = None):
        self.data = data
        self.next = next


# Add your implementations below

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
            return None 
        else: 
            removed = self.head 
            self.head = removed.next 
            self.size -= 1
            return removed.data

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
print(f"Fremste element i køen er {queue.head.data}")
print(f"Dette kan vi også sjekke med peek(): {queue.peek()}")
print(f"Bakerste element i køen er {queue.tail.data}")
print(f'fjerner {queue.dequeue()}')
print(f"Fremste er nå (): {queue.peek()}")