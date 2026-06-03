class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        monotonic decreasing stack
        stack to store the temp index, res list
        process: iterate temperatures list, check if temp is higher than stack.top() 
        -> if yes: update res list and pop from stack, then append current temp index to stack
        '''
        n = len(temperatures)
        res = [0] * n
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop() 
            stack.append(idx)

        return res