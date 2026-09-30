class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openC = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for c in s:
            if c in openC:
                if stack and stack[-1] == openC[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


        ([{}])

        

            
        