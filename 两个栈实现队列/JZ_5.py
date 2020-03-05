class Solution(object):
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, item):
        self.stackA.append(item)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
