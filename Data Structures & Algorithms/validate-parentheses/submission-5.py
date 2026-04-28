class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        close_to_open = {")": "(", "]": "[", "}": "{"}

        stack = []
        for e in s:
            if e in close_to_open:
                if stack and stack[-1] == close_to_open[e]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(e)
        return len(stack) == 0