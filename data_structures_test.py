# Imports
import pytest
import heapdict  


# Stack
from data_structures import Stack
def test_stack_init():
    stack = Stack()
    assert stack.head is None

def test_stack_push():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    assert stack.head.data == 'C'
    assert stack.head.next.data == 'B'
    assert stack.head.next.next.data == 'A'

def test_stack_peek():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    assert stack.peek() == 'B'

def test_stack_pop():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    assert stack.pop() == 'C'
    assert stack.pop() == 'B'
    assert stack.pop() == 'A'

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


# Queue
from data_structures import Queue
def test_queue_init():
    queue = Queue()
    assert queue.head is None
    assert queue.tail is None

def test_enqueue():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.head.data == 'A'
    assert queue.tail.data == 'C'

def test_peek():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    assert queue.peek() == 'A'

def test_dequeue():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.dequeue() == 'A'
    assert queue.dequeue() == 'B'
    assert queue.dequeue() == 'C'

def test_dequeue_empty():
    queue1 = Queue()
    with pytest.raises(IndexError):
        queue1.dequeue()
    queue2 = Queue()
    queue2.enqueue('X')
    _ = queue2.dequeue()
    with pytest.raises(IndexError):
        queue2.dequeue()


# Priority queue
from data_structures import EmergencyRoomQueue
def test_erqueue_init():
    erqueue = EmergencyRoomQueue()
    assert isinstance(erqueue.queue,heapdict.heapdict)

def test_add_patient():
    erqueue = EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    assert erqueue.queue['Bob'] == 3

def test_update_patient_priority():
    erqueue = EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.update_patient_priority('Bob',2)
    assert erqueue.queue['Bob'] == 2

def test_get_patient():
    erqueue = EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.add_patient_with_priority('Shabana',2)
    erqueue.add_patient_with_priority('Thu',5)
    assert erqueue.get_next_patient() == 'Shabana'

def test_add_update_get_patients():
    erqueue = EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.add_patient_with_priority('Shabana',2)
    erqueue.update_patient_priority('Bob',1)
    erqueue.add_patient_with_priority('Thu',5)
    erqueue.update_patient_priority('Shabana',8)
    assert erqueue.get_next_patient() == 'Bob'
    assert erqueue.get_next_patient() == 'Thu'
    assert erqueue.get_next_patient() == 'Shabana'

def test_get_from_empty_queue():
    erqueue = EmergencyRoomQueue()
    with pytest.raises(IndexError):
        erqueue.get_next_patient()


# Indexed linked list
from data_structures import IndexList
def test_indexlist_init():
    il = IndexList()
    assert il.head is None

def test_indexlist_insert():
    il = IndexList()
    il.insert('A',0)
    il.insert('B',0)
    il.insert('C',1)
    il.insert('D',3)
    assert il.head.data == 'B'
    assert il.head.next.data == 'C'
    assert il.head.next.next.data == 'A'
    assert il.head.next.next.next.data == 'D'

def test_indexlist_peek():
    il = IndexList()
    il.insert('A',0)
    il.insert('B',0)
    il.insert('C',1)
    il.insert('D',3)
    assert il.peek(0) == 'B'
    assert il.peek(1) == 'C'
    assert il.peek(2) == 'A'
    assert il.peek(3) == 'D'
    with pytest.raises(IndexError):
        il.peek(4)

def test_indexlist_pop():
    il = IndexList()
    il.insert('A',0)
    il.insert('B',1)
    il.insert('C',2)
    assert il.pop(2) == 'C'
    assert il.pop(0) == 'A'
    assert il.head.data == 'B'

def test_indexlist_popempty():
    il = IndexList()
    with pytest.raises(IndexError):
        il.pop(0)
    il.insert('A',0)
    il.pop(0)
    with pytest.raises(IndexError):
        il.pop(0)