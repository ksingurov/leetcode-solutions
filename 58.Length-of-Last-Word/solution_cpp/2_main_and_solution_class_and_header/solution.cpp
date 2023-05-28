#include "solution.h"

int Solution::lengthOfLastWord(const std::string& s) {
    int i = s.length() - 1;
    while (i >= 0 && s[i] == ' ') --i;
    int j = i;
    while (j >= 0 && s[j] != ' ') --j;
    return i - j;
};
