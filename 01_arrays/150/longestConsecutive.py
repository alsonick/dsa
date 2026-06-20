from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        n = len(s)
        if n == 0:
            return 0
        c = []
        k = 1
        for i in range(n):
            if i + 1 >= n:
                break
            if s[i] + 1 == s[i + 1]:
                k += 1
            else:
                k = 1
            c.append(k)

        return 1 if len(s) == 1 else max(c)
