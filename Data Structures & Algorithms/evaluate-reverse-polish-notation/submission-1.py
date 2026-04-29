class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculator(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return int(a / b)
        operators = ("+", "-", "/", "*")
        stack = []
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                res = calculator(val1, val2, c)
                stack.append(res)
        return stack.pop() if stack else None
               
