#include <iostream>
#include <string>
#include "solution.cpp"

int main() {
    std::string input;
    std::cout << "Enter a string (sentence): ";
    std::getline(std::cin, input);

    Solution sol;
    int len = sol.lengthOfLastWord(input);
    std::cout << "The length of the last word is: " << len << std::endl;
    
    return 0;
};
