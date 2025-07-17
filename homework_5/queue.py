class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self._last_node is None:
            self._first_node = new_node
            self._last_node = new_node
        else:
            self._last_node.next = new_node
            self._last_node = new_node
        self._size += 1

    def dequeue(self):
        if self._first_node is None:
            return None
        
        data = self._first_node.data
        self._first_node = self._first_node.next
        
        if self._first_node is None:
            self._last_node = None
        
        self._size -= 1
        return data
    
    def front(self):
        if self._first_node is None:
            return None
        return self._first_node.data
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def display(self):
        if self._first_node is None:
            print("Стек пуст.")
        else:
            print("Содержимое стека:")
            while self._size:
                print(self.dequeue())

    def __iter__(self):
        return QueueIterator(self)

class QueueIterator:
    def __init__(self, queue):
        self.queue = queue
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.queue.size():
            raise StopIteration
        value = self.queue._first_node
        self.index += 1
        return value
    

new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
#new_queue.display()

for item in new_queue:
    print(item)