from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap.get(key, []) # lookup based on key, return empty [] default if not found
        if not values:
            return ""

        i = bisect.bisect_right(values, (timestamp, chr(127)))
        if i == 0:
            return ""
        return values[i-1][1]