class MinStack:

    def __init__(self):
        self.global_min = None
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack or (not self.min_stack) or val <= self.global_min:
            self.global_min = val
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.global_min:
            self.min_stack.pop()
            if self.min_stack:
                self.global_min = self.min_stack[-1]
            else:
                self.global_min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.global_min
