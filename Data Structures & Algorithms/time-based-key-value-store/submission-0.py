from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        l, h = 0, len(arr)-1
        res = ""
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                h = mid - 1
        return res