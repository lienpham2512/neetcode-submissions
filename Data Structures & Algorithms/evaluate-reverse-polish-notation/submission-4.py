class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack to keep int
        # if run to operator, pop elements and perform operations
        # then append back into stack
        # return array[0]

        stack = []
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(b-a)
                elif c == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
