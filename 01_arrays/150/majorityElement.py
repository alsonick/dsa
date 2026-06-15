from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        m, o = [], {}
        for i in range(n):
            o[nums[i]] = o.get(nums[i], 0) + 1
            m.append(o)
        max_value, max_key = 0, 0
        for i in m:
            for k, v in i.items():
                if v > max_value:
                    max_value = v
                    max_key = k
        for j in m:
            for k in j:
                if k == max_key:
                    return k

        return 0