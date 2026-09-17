class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeP = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for c in s:
            if c in closeP:
                if stack and stack[-1] == closeP[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
        
            
        
        