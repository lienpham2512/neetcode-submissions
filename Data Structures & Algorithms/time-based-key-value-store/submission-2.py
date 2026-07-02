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
            for i in range(len(self.keyMap[key])):
                temp = self.keyMap[key][i]
                if timestamp >= temp[0]:
                    res = temp[1]
        return res
