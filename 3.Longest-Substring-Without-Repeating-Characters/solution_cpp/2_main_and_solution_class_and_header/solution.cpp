#include <unordered_set>
#include <string>
// #include <algorithm>
#include "solution.h"

int Solution::lengthOfLongestSubstring(const std::string& s) {
    std::unordered_set<char> seen_letters;
    int i_left = 0;
    int l_max = 0;
    int l_string = s.length();

    for (int i_right = 0; i_right < l_string; ++i_right) {
        while (seen_letters.find(s[i_right]) != seen_letters.end()) {
            seen_letters.erase(s[i_left]);
            ++i_left;
        }
        if (l_string - i_left <= l_max) {
            break;
        }
        seen_letters.insert(s[i_right]);
        l_max = std::max(l_max, i_right - i_left + 1);
    }

    return l_max;
}
