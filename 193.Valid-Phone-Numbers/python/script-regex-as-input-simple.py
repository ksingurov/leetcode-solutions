import sys
import re

# define function which reads lines within a file and checks if they match provided pattern
def valid_phone_numbers(file_name: str, pattern: str) -> str:
    with open(file_name, "r") as file:
        lines_to_print = [line.rstrip("\n") for line in file if re.search(pattern, line)]
    return "\n".join(lines_to_print)

# entry-point
if __name__ == "__main__":
    # get parameters from command line
    file_name = sys.argv[1]
    pattern = sys.argv[2]
    # pass parameters to the functions and print the result
    res = valid_phone_numbers(file_name, pattern)
    print(res)
