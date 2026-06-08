from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = 0
        n = len(arr)
        output = []
        if n == 1:
            return [-1]
        for i in range(n - 1, 0, -1):
            if i == n - 1:
                output.append(-1)
            if arr[i] > greatest:
                output.append(arr[i])
                greatest = arr[i]
            else:
                output.append(greatest)
        output.reverse()

        return output
