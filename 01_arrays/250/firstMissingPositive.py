from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] == 0:
            return 1
        elif n == 1:
            if nums[0] == 1:
                return nums[0] + 1
            return 1
        o = []
        nums_set = set(nums)
        for i in range(n):
            o.append(i + 1)
        for j in range(n):
            if not o[j] in nums_set:
                return o[j]
        
        return o[n - 1] + 1
