class Solution:
    def isValid(self, s: str) -> bool:
        # !- Neetcode Solution -!
        close = {")": "(", "]": "[", "}": "{"}
        stack = []
        for character in s:
            # Checks if the character is a closing bracket
            if character in close:
                # Checks if the stack is not empty and if the top element matches the closing bracket
                if stack and stack[-1] == close[character]:
                    # If they match then pop from the stack
                    stack.pop()
                else:
                    return False
            else:
                # Append the non closing bracket to the stack
                stack.append(character)
        # If all the brackets were closed then the stack should be empty
        if not stack:
            return True
        
        return False
    