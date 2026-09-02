class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {')' : '(',
                    ']' : '[',
                    '}' : '{'}
        
        for char in s:
            if char in mappings:
                if not stack or stack[-1] != mappings[char]:
                    return False
                stack.pop()
            else:   
               stack.append(char)
        return len(stack) == 0