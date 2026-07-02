from collections import defaultdict
class TimeMap:
    '''
    dict to store key -> list of (timestamp, value)
    edge cases:
        timestamp not existed: return prev timestamp's value
        key not existed: return ""
    search in list
    '''

    def __init__(self):
        self.keyMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.keyMap:
            l, r = 0, len(self.keyMap[key]) - 1
            while l <= r:
                mid = l + (r-l)//2
                if timestamp >= self.keyMap[key][mid][0]:
                    res = self.keyMap[key][mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
        return res
