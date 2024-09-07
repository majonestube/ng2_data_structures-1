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



erq = EmergencyRoomQueue()
erq.add_patient_with_priority("Noora", 5)
erq.add_patient_with_priority("Jacob", 2)
erq.add_patient_with_priority("Kim", 6)
print("The queue now looks like this:")
for a, b in erq.queue.items():
    print(f"{a}:{b}")
print(erq.get_next_patient())
print(list(erq.queue.keys()))