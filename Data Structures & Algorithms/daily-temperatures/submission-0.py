class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # this way we save a step to fill in 0 at the end
        stack = [] # store [Tem, Idx] as each element

        for idx, tem in enumerate(temperatures):
            while stack and stack[-1][0] < tem:
                stackTem, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([tem, idx])

        return res