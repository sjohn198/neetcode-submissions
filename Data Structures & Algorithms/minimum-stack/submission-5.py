class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # print(f"Val: {val}")
        # print(f"Min: {self.minimum}")
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            #print(f"Min stack: {self.min_stack}")

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
