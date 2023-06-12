# Imports
import pytest
import heapdict
import data_structures as ds  


# Stack
def test_stack_init(): # 1p
    stack = ds.Stack()
    assert stack.head is None

def test_stack_push(): # 2p
    stack = ds.Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    assert stack.head.data == 'C'
    assert stack.head.next.data == 'B'
    assert stack.head.next.next.data == 'A'

def test_stack_peek(): # 1p
    stack = ds.Stack()
    stack.push('A')
    stack.push('B')
    assert stack.peek() == 'B'

def test_stack_pop(): # 2p
    stack = ds.Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    assert stack.pop() == 'C'
    assert stack.pop() == 'B'
    assert stack.pop() == 'A'

def test_stack_pop_empty(): # 1p
    stack = ds.Stack()
    with pytest.raises(IndexError):
        stack.pop()


# Queue
def test_queue_init(): # 1p
    queue = ds.Queue()
    assert queue.head is None
    assert queue.tail is None

def test_queue_enqueue(): # 2p
    queue = ds.Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.head.data == 'A'
    assert queue.tail.data == 'C'

def test_queue_peek(): # 1p
    queue = ds.Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    assert queue.peek() == 'A'

def test_queue_dequeue(): # 2p
    queue = ds.Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.dequeue() == 'A'
    assert queue.dequeue() == 'B'
    assert queue.dequeue() == 'C'

def test_queue_dequeue_empty(): # 1p
    queue1 = ds.Queue()
    with pytest.raises(IndexError):
        queue1.dequeue()
    queue2 = ds.Queue()
    queue2.enqueue('X')
    _ = queue2.dequeue()
    with pytest.raises(IndexError):
        queue2.dequeue()


# Priority queue
def test_erqueue_init(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    assert isinstance(erqueue.queue,heapdict.heapdict)

def test_erqueue_add_patient(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    assert erqueue.queue['Bob'] == 3

def test_erqueue_update_patient_priority(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.update_patient_priority('Bob',2)
    assert erqueue.queue['Bob'] == 2

def test_erqueue_get_patient(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.add_patient_with_priority('Shabana',2)
    erqueue.add_patient_with_priority('Thu',5)
    assert erqueue.get_next_patient() == 'Shabana'

def test_erqueue_add_update_get_patients(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    erqueue.add_patient_with_priority('Bob',3)
    erqueue.add_patient_with_priority('Shabana',2)
    erqueue.update_patient_priority('Bob',1)
    erqueue.add_patient_with_priority('Thu',5)
    erqueue.update_patient_priority('Shabana',8)
    assert erqueue.get_next_patient() == 'Bob'
    assert erqueue.get_next_patient() == 'Thu'
    assert erqueue.get_next_patient() == 'Shabana'

def test_erqueue_get_from_empty_queue(): # 1p
    erqueue = ds.EmergencyRoomQueue()
    with pytest.raises(IndexError):
        erqueue.get_next_patient()


# Indexed linked list
def test_indexlist_init(): # 1p
    il = ds.IndexList()
    assert il.head is None

def test_indexlist_insert(): # 3p
    il = ds.IndexList()
    il.insert('A',0)
    il.insert('B',0)
    il.insert('C',1)
    il.insert('D',3)
    assert il.head.data == 'B'
    assert il.head.next.data == 'C'
    assert il.head.next.next.data == 'A'
    assert il.head.next.next.next.data == 'D'

def test_indexlist_peek(): # 2p
    il = ds.IndexList()
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

def test_indexlist_pop(): # 3p
    il = ds.IndexList()
    il.insert('A',0)
    il.insert('B',1)
    il.insert('C',2)
    il.insert('D',3)
    assert il.pop(2) == 'C'
    assert il.pop(2) == 'D'
    assert il.pop(0) == 'A'
    assert il.head.data == 'B'

def test_indexlist_popempty(): # 2p
    il = ds.IndexList()
    with pytest.raises(IndexError):
        il.pop(0)
    il.insert('A',0)
    il.pop(0)
    with pytest.raises(IndexError):
        il.pop(0)