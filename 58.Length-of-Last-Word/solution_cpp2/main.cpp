#include <iostream>
#include <string>
#include "solution.h"  // like Python's `from solution import Solution`

int main() {
    std::string input;

    std::cout << "Provide a string (sentence): ";
    std::getline(std::cin, input);

    Solution sol;
    int result = sol.lengthOfLastWord(input);
    
    std::cout << "The length of the last word in the string is: " << result << std::endl;

    return 0;
};
