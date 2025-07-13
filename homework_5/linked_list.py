class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if not self._head_node:
            self._head_node = new_node
            self._tail_node = new_node
        else:
            new_node.prev = self._tail_node
            self._tail_node.next = new_node
            self._tail_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self._head_node:
            self._head_node = new_node
            self._tail_node = new_node
        else:
            new_node.next = self._head_node
            self._head_node.prev = new_node
            self._head_node = new_node

    def insert(self,item, i):
        new_node = Node(item)
        if self._head_node is None:
            self._head_node = new_node
            self._tail_node = new_node
            return
        
        if i <= 0:
            new_node.next = self._head_node
            self._head_node.prev = new_node
            self._head_node = new_node
            return
        
        current = self._head_node
        count = 0
        while current and count < i:
            current = current.next
            count += 1

        if current is None:
            self._tail_node.next = new_node
            new_node.prev = self._tail_node
            self._tail_node = new_node
        else:
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
                current.prev = new_node
            if new_node.prev is None:
                self._head_node = new_node
    
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self._head_node = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self._tail_node = node.prev

    def find(self, data):
        current = self._head_node
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def display(self, reverse=False):
        if not self._head_node:
            print("Список пуст")
            return
        
        if reverse:
            current = self._tail_node
            while current:
                print(current.data, end=" ")
                current = current.prev

        else:
            current = self._head_node
            while current:
                print(current.data, end=" ")
                current = current.next
        print()

    def __getitem__(self, index):
        current = self._head_node
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError("Индекс выходит за пределы списка")
    
    def __iter__(self):
        return LinkedListIterator(self)

class LinkedListIterator:
    def __init__(self, linked_list):
        self.current = linked_list._head_node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.data
        self.current = self.current.next
        return value

new_list = LinkedList()
new_list.append(1)
new_list.append(2)
new_list.append(3)

#print(new_list[0])  
#print(new_list[2]) 

#try:
#    print(new_list[2])
#except IndexError as e:
#    print(e) 

for item in new_list:
    print(item)