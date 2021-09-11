import sys
import re

def valid_phone_numbers(file_name: str, pattern: str) -> str:
    with open(file_name, "r") as file:
        lines_to_print = [line.rstrip("\n") for line in file if re.search(pattern, line)]
    return "\n".join(lines_to_print)

if __name__ == "__main__":
    file_name = sys.argv[1]
    pattern = sys.argv[2]
    res = valid_phone_numbers(file_name, pattern)
    print(res)
