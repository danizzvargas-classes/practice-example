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

    # Validar cola vacía
    assert q.is_empty() == True
    assert q.size() == 0

    # Validar enqueue
    q.enqueue(10)
    assert q.size() == 1
    assert q.front() == 10

    q.enqueue(20)
    q.enqueue(30)
    assert q.size() == 3
    assert q.front() == 10  # El frente no cambia

    print("Cola inicial:", q.data)

    # Validar dequeue
    valor = q.dequeue()
    assert valor == 10
    assert q.size() == 2
    assert q.front() == 20  # Nuevo frente

    print("Dequeue:", valor)
    print("Cola después:", q.data)

    # Validar vaciado completo
    q.dequeue()
    q.dequeue()
    assert q.is_empty() == True

    # Validar error en cola vacía
    try:
        q.dequeue()
        assert False, "Debería lanzar IndexError"
    except IndexError:
        pass

    print("Todas las validaciones pasaron correctamente.")
