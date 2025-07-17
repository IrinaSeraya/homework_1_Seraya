class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self._top_node = None
        self._size = 0
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self._top_node
        self._top_node = new_node
        self._size += 1

    def pop(self):
        if self._top_node is None:
            return None
        else:
            popped_node = self._top_node
            self._top_node = self._top_node.next
            self._size -= 1
            return popped_node.data

        
    def peek(self):
        if self._top_node is None:
            return None
        else:
            return self._top_node.data
        
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def display(self):
        if self._top_node is None:
            print("Стек пуст.")
        else:
            print("Содержимое стека:")
            while self._size:
                print(self.pop())

    def __iter__(self):
        return StackIterator(self)

class StackIterator:
    def __init__(self, stack):
        self.stack = stack
        self.index = stack.size() - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            value = self.stack._top_node
            self.index -= 1
            return value

#stack = Stack()
#stack.push(1)
#stack.push(2)
#stack.push(3)
#stack.display()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for item in stack:
    print(item)