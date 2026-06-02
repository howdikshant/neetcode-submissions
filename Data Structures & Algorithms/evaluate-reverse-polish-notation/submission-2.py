class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                if stack:
                    if ch == '+':
                        a = stack.pop()
                        stack.append(a + stack.pop())
                    if ch == '-':
                        a = stack.pop()
                        stack.append(stack.pop() - a)
                        
                    if ch == '*':
                        a = stack.pop()
                        stack.append(stack.pop() * a)
                        
                    if ch == '/':
                        a = stack.pop()
                        stack.append(int(stack.pop() / a))
                        

        return int(stack.pop())
