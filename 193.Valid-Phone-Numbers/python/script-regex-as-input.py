import sys
import re

file_name = sys.argv[1]
pattern = sys.argv[2]
# print(pattern)

# pattern = r"^\(?\d{3}\)?( |-)\d{3}-\d{4}$"

with open(file_name, "r") as file:
    # for line in file:
    #     match = re.search(pattern, line)
    #     if match:
    #         print(line.rstrip("\n"))

    # for line in file:
    #     if re.search(pattern, line):
            # print(line.rstrip("\n"))

    # [print(line.rstrip("\n")) for line in file if re.search(pattern, line)]
    lines_to_print = [line.rstrip("\n") for line in file if re.search(pattern, line)]

print("\n".join(lines_to_print))
