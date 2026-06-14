from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # !- Greg Hogg Solution -!
        right_multiplier = 1
        left_multiplier = 1
        n = len(nums)
        right_array = [0] * n
        left_array = [0] * n
        output = [0] * n
        for i in range(n):
            j = -i - 1 # Grabs the last index (basically the index that will iterate backwards)
            right_array[j] = right_multiplier
            left_array[i] = left_multiplier
            right_multiplier *= nums[j]
            left_multiplier *= nums[i]
        for i in range(n):
            output[i] = left_array[i] * right_array[i]
        
        return output

# My original solution which was O(n^2) ~ too slow for larger inputs
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         p, i, j = 1, 0, 1
#         n = len(nums)
#         o = []
#         while i <= n - 1:
#             if j == n:
#                 o.append(p)
#                 i += 1
#                 p = 1
#                 j = 0
#             if i != j:
#                 p *= nums[j]
#             j += 1
        
#         return o