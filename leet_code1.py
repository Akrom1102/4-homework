# TWO SUM
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i

        return []


nums = [2, 7, 11, 15]
target = 18
sol = Solution()
print(sol.twoSum(nums, target))

