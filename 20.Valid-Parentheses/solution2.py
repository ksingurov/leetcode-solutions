class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif not stack or stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
        return not stack
