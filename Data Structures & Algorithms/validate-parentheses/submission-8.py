class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        charP = {
            "}" : "{" ,
            ")" : "(" ,
            "]" : "["
        }

        for c in s:
            if c in charP:
                if stack and stack[-1] == charP[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        