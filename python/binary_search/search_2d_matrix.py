from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        row = -1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break

            if matrix[mid][0] > target:
                right = mid - 1
                continue

            left = mid + 1

        return False if row == -1 else self.binary_search(matrix[row], target)

    def binary_search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
                continue

            if nums[mid] > target:
                right = mid - 1
                continue

            return True

        return False
