class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                s = "".join(stack) # join the whole stack to a string
                res.append(s)
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if openN > closeN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res