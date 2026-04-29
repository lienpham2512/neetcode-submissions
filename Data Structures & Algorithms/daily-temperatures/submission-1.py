class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n-1 and temperatures[i] >= temperatures[j]:
                j += 1
            if temperatures[i] < temperatures[j]:
                res[i] = j - i
        return res