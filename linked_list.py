class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, llista):
        self.size = len(llista)
        tail = None
        for i in range(len(llista)):
            if i == 0:
                self.head = Node(llista[i])
                tail = self.head
            else:
                tail.next = Node(llista[i])
                tail = tail.next

    def __len__(self):
        return self.size

    def __str__(self):
        current = linkedList.head
        result = "["

        for element in self:
            result += str(element)
            result += ", "

        return result[:-2] + "]"

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


llista = [1, 2, 3, 4, 5]
linkedList = LinkedList(llista)

print(len(linkedList))
print(linkedList)

for element in linkedList:
    print(element)
