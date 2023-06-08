from data_structures import Queue
import pytest

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

def test_dequeue():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.dequeue() == 'A'
    assert queue.dequeue() == 'B'
    assert queue.dequeue() == 'C'

def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()