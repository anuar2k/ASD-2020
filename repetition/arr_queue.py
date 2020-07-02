class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * (self.capacity + 1)
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.head - self.tail) % len(self.storage) == self.capacity:
            raise Exception("Queue is full")

        self.storage[self.head] = x
        self.head = (self.head + 1) % len(self.storage)

    def dequeue(self):
        result = self.storage[self.tail]
        self.tail = (self.tail + 1) % len(self.storage)

        return result

    def is_empty(self):
        return self.head == self.tail