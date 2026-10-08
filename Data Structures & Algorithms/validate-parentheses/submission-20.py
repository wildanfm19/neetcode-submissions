class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeM = {
            '}' : "{",
            ']' : '[',
            ')' : '('
        }

        for c in s:
            if c in closeM:
                if stack and closeM[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        