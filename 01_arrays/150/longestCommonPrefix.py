from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current, iterator = 1, 0
        if len(strs[0]) == 0:
            return ""
        first = strs[0][iterator]
        n = len(strs)
        output = ""
        found = 1
        while True:
            if len(strs[current - 1]) == iterator:
                break
            current_character = strs[current - 1][iterator]
            if current_character == first:
                if found == n:
                    output += current_character
                    iterator += 1
                    if iterator == len(strs[0]):
                        break
                    first = strs[0][iterator]
                    current = 1
                    found = 1
                current += 1
                found += 1
            else:
                break
        
        return output
