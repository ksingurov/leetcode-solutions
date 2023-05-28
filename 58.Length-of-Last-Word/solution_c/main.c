#include <stdio.h>
#include <string.h>
#include "solution.h"

#define MAX_LEN 50000

int main() {
    char input[MAX_LEN + 1];

    printf("Enter a string (sentence, max %d characters): ", MAX_LEN);
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0';

    int len = lengthOfLastWord(input);
    printf("The length of the last word is: %d\n", len);

    return 0;
}
