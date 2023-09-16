class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
            return

        if val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if not self.stack:
            return

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return -1

        return self.min_stack[-1]

