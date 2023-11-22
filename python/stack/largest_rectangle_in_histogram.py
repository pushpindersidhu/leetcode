class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                start = i
                max_area = max(max_area, (index - i) * h)

            stack.append((start, height))

        while stack:
            (i, h) = stack.pop()
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area
