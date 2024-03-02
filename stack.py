class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

# push
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

# pop
stack.pop()
stack.pop()
stack.pop()

# print(stack.items)
for i in stack.items:
    print(i)

# size
a = stack.size()
print("Stack uzunligi: ", a)