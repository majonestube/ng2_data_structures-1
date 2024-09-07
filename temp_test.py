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
        return self.head

    def pop(self) -> Node:
        """Remove last added node and return its data"""
        if self.size == 0:
            return None
        else:
            removed = self.head 
            self.head = self.head.next
            self.size -= 1
            return removed.data


stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(f"Øverste element i stacken har verdi {stack.head.data}")
print(f"Dette kan vi også sjekke ved å bruke peek(): {stack.peek()}")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())