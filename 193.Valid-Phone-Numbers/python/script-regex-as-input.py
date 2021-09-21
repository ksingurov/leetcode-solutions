import sys
import re

# function to validate provided pattern
def is_valid_regex(pattern: str) -> bool | str:
    try:
        re.compile(pattern)
        return True
    except re.error as e:
        regex_syntax_link = "https://docs.python.org/3/library/re.html#regular-expression-syntax"
        string_to_return = f"Error -> Invalid regex: {e}\nRefer to regex syntax here: {regex_syntax_link}"
        return string_to_return

def get_phone_numbers(file_name: str) -> list[str] | None:
    try:
        with open(file_name, "r") as file:
            phone_numbers = [line.rstrip("\n") for line in file]
        return phone_numbers
    except FileNotFoundError:
        return None

def get_valid_phone_numbers(phone_numbers: list[str], pattern: str) -> list[str]:
    return [pn for pn in phone_numbers if re.search(pattern, pn)]

# entry-point
if __name__ == "__main__":
    # handle input argement
    if len(sys.argv) < 3:
        print(f"Error -> Missing argements\nUsage: {sys.argv[0]} <file-name> <pattern>")
        sys.exit(1)
    file_name = sys.argv[1]
    pattern = sys.argv[2]

    # check pattern
    check_regex = is_valid_regex(pattern)
    if check_regex is not True:
        print(check_regex)
        sys.exit(1)

    # get phone numbers tp process
    phone_numbers = get_phone_numbers(file_name)
    if not phone_numbers:
        print(f"Error -> file {file_name} doesn't exist")
        sys.exit()

    # get valid phone numbers
    valid_phone_numbers = get_valid_phone_numbers(phone_numbers, pattern)
    print("\n".join(valid_phone_numbers))
