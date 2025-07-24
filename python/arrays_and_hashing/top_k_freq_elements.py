from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        out = []
        for key, _ in sorted(map.items(), key=lambda x: x[1], reverse=True):
            if k <= 0:
                break

            out.append(key)
            k -= 1

        return out
