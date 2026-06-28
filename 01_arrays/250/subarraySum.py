from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        seen = {0:1}
        output = 0
        for num in nums:
            running_sum += num
            output += seen.get(running_sum - k, 0)
            seen[running_sum] = seen.get(running_sum, 0) + 1

        return output
