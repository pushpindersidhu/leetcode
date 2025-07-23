import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        if len(piles) == h:
            return k

        left, right = 1, k
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                k = mid
                right = mid - 1
                continue

            left = mid + 1

        return k
