# Efficient stack based solution
# Logic:
# Iterate over characters in the string, and check folllowing condition:
# - if character is an opening bracket ("if")
#   -> add it to the stack
# - if it is not, and stack is empty or last paranthesis in the stack doesn't match the current ("elif")
#   -> invalid sequence of parentheses - end the cycle and return False
# - otherwise ("else" = i.e. if parentheses matched)
#   -> remove last opening parenthesis


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
