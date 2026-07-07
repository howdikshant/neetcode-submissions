class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "{[(":
                stack.append(ch)


            
            if ch == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            if ch == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            if ch == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False
        

            