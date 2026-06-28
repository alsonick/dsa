from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        found = False
        output = []
        for i in range(n):
            if found:
                break
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    found = True
                    break

        return output
