# optimized solution with O(n) time complexity
# there is also an earlier exit:
#   - when remaining length of the string (l_string - i_left) is not greater than the current max
#   - i.e. when it's impossible to find a substring longer than the one already found

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_letters = set()  
        i_left = 0
        l_max = 0
        l_string = len(s)

        i = 0 # cycle counter
        print("\nl_string: ", l_string)
        for i_right in range(l_string):
            i += 1 # cycle counter
            print(f"cycle: {i} |          | left: {i_left} | right: {i_right} | checking: {' ' * i_left}{s[i_left: i_right + 1]}")
            j = 0 # while counter
            while s[i_right] in seen_letters:
                j += 1 # while counter
                seen_letters.remove(s[i_left])
                i_left += 1
                print(f"cycle: {i} | while: {j} | left: {i_left} | right: {i_right} | checking: {' ' * i_left}{s[i_left: i_right + 1]}")
            if l_string - i_left <= l_max:
                break
            seen_letters.add(s[i_right])
            l_max = max(l_max, i_right - i_left + 1)
            
        return l_max
