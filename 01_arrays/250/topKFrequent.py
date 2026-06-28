from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_dict = defaultdict(int)
        output = []
        # Add each element with their frequency into the dictionary
        for num in nums:
            elements_dict[num] += 1
        # Sort them by value from greatest to smallest
        elements_items = sorted(elements_dict.items(), key=lambda x: x[1], reverse=True)
        # Turn it back into a dictionary
        elements_dict = dict(elements_items)
        i = k
        # Gets the k most frequent elements from the dictionary
        for k in elements_dict:
            if i == 0:
                break
            output.append(k)
            i -= 1

        return output
