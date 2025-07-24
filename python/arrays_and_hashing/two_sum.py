from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_map:
                return [idx, diff_map[diff]]

            diff_map[num] = idx

        return [-1, -1]
