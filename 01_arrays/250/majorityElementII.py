import math
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        j = math.floor(n / 3)
        dic = {}
        o = []
        for i in range(n):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for k, v in dic.items():
            if v > j:
                o.append(k)
        
        return o
