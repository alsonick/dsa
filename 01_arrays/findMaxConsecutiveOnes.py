from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_count = 0
        consecutives = []
        n = len(nums)
        for i in range(n):
            current = nums[i]
            if current == 1:
                consecutive_count += 1
            else:
                consecutives.append(consecutive_count)
                consecutive_count = 0
            if i == n - 1:
                consecutives.append(consecutive_count)
        max_consecutive = 0
        for consecutive in consecutives:
            if consecutive > max_consecutive:
                max_consecutive = consecutive

        return max_consecutive
