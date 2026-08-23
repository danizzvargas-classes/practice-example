class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data.pop(0)

if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Cola inicial:", q.data)

    valor = q.dequeue()
    print("Dequeue:", valor)
    print("Cola después:", q.data)

    # Validar vaciado completo
    q.dequeue()
    q.dequeue()

    # Validar error en cola vacía
    try:
        q.dequeue()
        assert False, "Debería lanzar IndexError"
    except IndexError:
        pass

    print("Todas las validaciones pasaron correctamente.")
