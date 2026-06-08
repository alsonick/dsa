from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i = 0, 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                k += 1; i += 1

        return k
