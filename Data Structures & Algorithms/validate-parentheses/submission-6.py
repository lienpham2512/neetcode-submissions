class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        pair = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
