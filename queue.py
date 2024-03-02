class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()

queue.enqueue(15)
queue.enqueue("Akrom")
queue.enqueue(10)
queue.enqueue("Kamron")
queue.enqueue(16)
queue.enqueue("Davron")
print(queue.items)


for i in queue.items:
    print(i)

# size
a = queue.size()
print("Queue uzunligi: ", a)