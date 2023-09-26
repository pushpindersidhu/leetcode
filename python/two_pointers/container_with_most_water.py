class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        area = 0

        while left < right:
            if height[left] < height[right]:
                area = max(height[left] * (right - left), area)
                left += 1
            else:
                area = max(height[right] * (right - left), area)
                right -= 1

        return area

