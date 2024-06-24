class Deque:
    def __init__(self, llista):
        self.llista = llista

    def add_tail(self, data):
        self.llista.append(data)
    
    def remove_tail(self):
        self.llista.pop()

    def add_head(self, data):
        self.llista.insert(0, data)

    def remove_head(self):
        self.llista.pop(0)

    def __str__(self):
        return str(self.llista)

deque = Deque([1,2,3])

deque.add_tail(1)
print(deque)
deque.remove_tail()
print(deque)
deque.add_head(3)
print(deque)
deque.remove_head()
print(deque)
