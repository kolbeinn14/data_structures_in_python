from typing import Any
from collections import deque

class LL:
    def __init__(self, value, next=None):
        if not isinstance(next, LL) and next != None:
            raise TypeError(f"next has to point towards another node of type <Linked_list>.")

        self.value = value
        self.next = next
    
class DLL:
    def __init__(self, value, next=None, back=None):
        if not isinstance(next, DLL) and next != None:
            raise TypeError(f"next has to point towards another node of type <Linked_list>.")
        if not isinstance(back, DLL) and back != None:
            raise TypeError(f"back has to point towards another node of type <Linked_list>.")

        self.value = value
        self.next = next
        self.back = back

class circular_buffer:
    def __init__(self, data:list, BUFFER_SIZE:int):
        if (len(data) > BUFFER_SIZE):
            raise BufferError("lenght of list exceeded the buffer size")
        self.data = data
        self.curr_index = len(data)
        self.BUFFER_SIZE = BUFFER_SIZE

    def add(self, value:int) -> None:
        self.curr_index %= self.BUFFER_SIZE
        self.data[self.curr_index] = value
        self.curr_index += 1


class Stack:
    def __init__(self, other=None, fixed_size_int=2<<63) -> None:
        self.stack = []    
        self.fixed_size = int(fixed_size_int)

        if isinstance(other, Stack):
            self.stack = list(other.stack)
            self.fixed_size = int(other.fixed_size)    
            return
            
        elif isinstance(other, list):
            if fixed_size_int < len(other):
                raise BufferError("lenght of list exceeded the buffer size")
            self.stack = other 
            return

        elif (other != None):
            self.stack.append(other)
        
    


    def push(self, value) -> None:
        if (len(self.stack) >= self.fixed_size):
            raise BufferError("lenght of list exceeded the buffer size")
        
        if isinstance(value, list):
            if (len(self.stack + value) >= self.fixed_size):
                raise BufferError("lenght of list exceeded the buffer size")
            
            self.stack += value
            return True
        
        self.stack.append(value)
        return True
    

    def peek(self) -> Any:
        if (len(self.stack) <= 0):
            raise IndexError("Can not access values out of bound.")
        return self.stack[-1]
    
    def pop(self) -> Any:
        if (len(self.stack) <= 0):
            raise IndexError("Can not access values out of bound.")
        return self.stack.pop()
    
    def isEmpty(self) -> bool:
        return len(self.stack)==0
    
    def isFull(self) -> bool:
        return len(self.stack)==self.fixed_size
    

class Queue: 
    def __init__(self, other=None, fixed_size_int=2<<63) -> None:
        self.queue = deque()
        self.fixed_size = int(fixed_size_int)

        if isinstance(other, Queue):
            self.queue = deque(other.queue)
            self.fixed_size = int(other.fixed_size)
            return 
        
        if isinstance(other, list):
            if fixed_size_int < len(other):
                raise BufferError("lenght of list exceeded the buffer size")
            self.queue += other
            return
        
        if (other != None):
            self.queue = other
            return
    
    def enqueue(self, other):
        if (len(self.queue) >= self.fixed_size):
            raise BufferError("lenght of list exceeded the buffer size")

        
        if (isinstance(other, list)):
            if self.fixed_size < len(self.queue + other):
                raise BufferError("lenght of list exceeded the buffer size")
            self.queue += other
            return
        
        self.queue.append(other)
    
    def dequeue(self) -> Any:
        if (len(self.queue) <= 0):
            raise IndexError("Can not access values out of bound.")
        return self.queue.popleft()

    def peek(self) -> Any: 
        if (len(self.queue) <= 0):
            raise IndexError("Can not access values out of bound.")
        return self.queue[0]
    
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    
    def isFull(self) -> bool:
        return len(self.queue) == self.fixed_size
        


class Graph:
    def __init__(self, edge:int, graphs:list=None):

        if isinstance(graphs, list):
            if not isinstance(graphs[0], Graph):
                raise TypeError("graphs must be of type <Graph>")
        elif not isinstance(graphs, Graph) or graphs != None:
            raise TypeError("graphs must be of type <Graph> or equal to (None)")
        
        self.edge = edge
        self.graphs = graphs
    
    
class tree:
    def __init__(self, value, left=None, right=None):
        if not isinstance(left, tree) and left != None:
            raise TypeError("left must be of type <tree> or equal to (None)")
        if not isinstance(right, tree) and right != None:
            raise TypeError("right must be of type <tree> or equal to (None)")
        
        self.value = value
        self.left = left
        self.right = right
        self.instance = 1
    
    def insert(self, value):
        if self.value == value:
            self.instance += 1
            return
        
        elif self.value > value:
            if (self.left == None):
                self.left = tree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if (self.right == None):
                self.right = tree(value)
            else:
                self.right.insert(value)
    
    def search(self, value) -> tree:
        while (True):
            if self.value == value:
                return self
            
            if self.value > value:
                if self.left == None:
                    return None
                self = self.left 
            
            if self.value < value:
                if self.right == None:
                    return None
                self = self.right 
            
