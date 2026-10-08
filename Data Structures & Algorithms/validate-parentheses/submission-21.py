class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeM = {
            '}' : "{" , 
            ')' : '(' ,
            ']' : '['
        }

        for c in s:
            if c in closeM:
                if stack and stack[-1] == closeM[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
        