from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if len(values) == 0:
            return ""

        ts = ""
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp == values[mid][1]:
                return values[mid][0]

            if timestamp > values[mid][1]:
                ts = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return ts
