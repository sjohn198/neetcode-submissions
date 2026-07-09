class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # print(f"Val: {val}")
        # print(f"Min: {self.minimum}")
        if self.minimum is None or val <= self.minimum:
            self.minimum = val
            self.min_stack.append(val)
            #print(f"Min stack: {self.min_stack}")

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.minimum:
            self.min_stack.pop()
            if len(self.min_stack) > 0:
                self.minimum = self.min_stack[-1]
            else:
                self.minimum = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
