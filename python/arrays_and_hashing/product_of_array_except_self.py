from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        product = [1] * len(nums)
        for i in range(len(nums)):
            product[i] = prefix[i] * postfix[i]

        return product
