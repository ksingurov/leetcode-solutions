#include <iostream>
#include <string>
#include "solution.cpp"

int main() {
    std::string input;

    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    Solution sol;
    int result = sol.lengthOfLongestSubstring(input);

    std::cout << "The length of the longest substring without duplicate characters is " << result << std::endl;
}
