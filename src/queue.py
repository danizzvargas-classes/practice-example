class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[0]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Cola inicial:", q.data)
    print("Frente:", q.front())
    print("Dequeue:", q.dequeue())
    print("Cola después:", q.data)
