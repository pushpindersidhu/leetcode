import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                res.append(-heap[0][0])

        return res
