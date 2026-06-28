class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        output = ""
        t_copy = t
        n = len(s)
        for c in s:
            if c in t_copy:
                t_copy = t_copy.replace(c, "", 1)
                output += c

        return output == s
