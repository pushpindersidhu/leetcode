class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1, f = nums[0], nums[nums[0]]

        while s1 != f:
            s1 = nums[s1]
            f = nums[nums[f]]

        s2 = 0
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]

        return s1

