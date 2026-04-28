class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for e in s:
            if e == "(" or e == "[" or e == "{":
                stack.append(e)
            elif e == ")" or e == "]" or e == "}":
                if len(stack) == 0:
                    return False
                if (e == ")" and stack.pop() != "(") or (e == "]" and stack.pop() != "[") or (e == "}" and stack.pop() != "{"):
                    return False
        if len(stack) > 0:
            return False
        return True