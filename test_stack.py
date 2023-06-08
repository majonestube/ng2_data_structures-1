from data_structures import Stack
import pytest

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