class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(i)
            elif i == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a + b
                stack.append(res)
            elif i == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a - b
                stack.append(res)
            elif i == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a * b
                stack.append(res)
            elif i == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a / b
                stack.append(res)
        
        return int(stack.pop())