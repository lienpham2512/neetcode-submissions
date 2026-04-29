class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # list of pairs (tuple)
        # iteration for-loop
        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                index = stack[-1][0]
                res[index] = i - index
                stack.pop()
            stack.append((i, value))
        return res