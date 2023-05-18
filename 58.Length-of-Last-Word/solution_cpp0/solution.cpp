#include <iostream>
#include <string>

class Solution {
    public:
        int lengthOfLastWord(const std::string& s) {
            int i = s.length() - 1;
            while (i >= 0 && s[i] == ' ') --i;
            int j = i;
            while (j >= 0 && s[j] != ' ') --j;
            return i - j;
        }
    };


int main() {
    std::string input;
    std::cout << "Enter a string (sentence): ";
    std::getline(std::cin, input);

    Solution sol;
    int len = sol.lengthOfLastWord(input);
    std::cout << "The length of the last word is: " << len << std::endl;
    
    return 0;
};
