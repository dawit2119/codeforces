class Stack:

    def __init__(self):
        self.stack = []

    def peak(self):
        if not self.isEmpty():
            return self.stack[-1]

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        output = ""
        for i in range(len(self.stack)):
            output += str(self.stack[i])
        return output


stack = Stack()
stack.push(1)
stack.push(10)
stack.push(11)
stack.pop()
print(stack)
