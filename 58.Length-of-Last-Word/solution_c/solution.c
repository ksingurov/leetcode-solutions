#include <string.h>
#include <ctype.h>
#include "solution.h"

int lengthOfLastWord(const char* s) {
    int len = strlen(s);
    int i = len - 1;
    while (i >= 0 && isspace(s[i])) --i;
    int j = i;
    while (j >= 0 && !isspace(s[j])) --j;
    return i - j;
}
