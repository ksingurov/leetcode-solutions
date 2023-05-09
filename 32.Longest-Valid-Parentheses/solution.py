# Solution based on stack
# (see explanation in the body of the function)

class Solution:
    def longestValidParentheses(s: str) -> int:
        # Initialize stack with -1 to mark the base before starting
        # It is needed to ensure that:
        # if the entire string is valid, -1 will stay in in the stack till the end
        # and lenght calculated as: "index of last iteration" - stack[-1] will yield exatly the lenght of the entire string
        stack = [-1]

        # variable to keep track of the longest valid substring
        max_len = 0
        
        for i, char in enumerate(s):
            if char == "(":
                # pushing the index of found "(" to the stack
                # we keep it since it is possible there is ")" further in the string which will "close" it
                stack.append(i)
            else:
                # it means char = ")"
                # in this case we pop the last "(" index - "closing" the parantheses
                stack.pop()
                
                # if there indeed was "(" found before, stack will be non empty after popping the last index
                # and will we can calculate a new lenght
                # but if there are not indeces left in the stack, it means we need to start again from current place
                if not stack:
                    # If stack is empty, push current index as a new base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring:
                    # "current index" - "index at new top of the stack"
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
