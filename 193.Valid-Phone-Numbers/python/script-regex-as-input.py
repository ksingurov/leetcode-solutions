import sys
import re

# function to check if enought argements are provided
def enough_input_argements(args: list[str]) -> bool:
    if len(sys.argv) < 3:
        inp = " ".join(sys.argv)
        print(f"Error -> Not enough argements were provided: '{inp}'")
        print(f"Usage: {sys.argv[0]} <file-name> <pattern>")
        return False
    return True

# function to validate provided pattern
def is_valid_regex(pattern: str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error as e:
        # print(f"[DEBUG] Regex error: {e}")
        print(f"Error -> Invalid regex: {e}")
        regex_syntax_link = "https://docs.python.org/3/library/re.html#regular-expression-syntax"
        print(f"Refer to regex syntax here: {regex_syntax_link}")
        return False

# function which reads lines within a file and checks if they match provided pattern
def valid_phone_numbers(file_name: str, pattern: str) -> str:
    with open(file_name, "r") as file:
        lines_to_print = [line.rstrip("\n") for line in file if re.search(pattern, line)]
    return "\n".join(lines_to_print)

# entry-point
if __name__ == "__main__":
    # handle input argement
    if not enough_input_argements(sys.argv):
        sys.exit(1)
    file_name = sys.argv[1]
    pattern = sys.argv[2]

    # check pattern
    if not is_valid_regex(pattern):
        sys.exit(1)
    
    try:
        # pass parameters to the functions and print the result
        res = valid_phone_numbers(file_name, pattern)
        print(res)
    except FileNotFoundError:
        print(f"Error -> {file_name} doesn't exist")
