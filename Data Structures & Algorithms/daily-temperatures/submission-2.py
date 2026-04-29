class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if res[j] == 0:
                    j = n # to make sure we ignore line 14 15 after break
                    break
                j += res[j] # what if there is no warmer day for j? and t[j] < t[i]
            # when t[i] < t[i] then add to res
            if j < n:
                res[i] = j - i
        return res