import sys
import re

# function to return all phone numbers from the file
# return None if file doesn't exists
def get_phone_numbers(file_name: str) -> list[str] | None:
    try:
        with open(file_name, "r") as file:
            phone_numbers = [line.rstrip("\n") for line in file]
        return phone_numbers
    except FileNotFoundError:
        return None

# function to return valid phone numbers
def get_valid_phone_numbers(phone_numbers: list[str], pattern: str) -> list[str]:
    return [pn for pn in phone_numbers if re.search(pattern, pn)]

# TODO: function to check that example only contains alphanumeric, (), -, and " "
# TODO: function(s) to transform examples to patterns

# main function
def main():
    # handle input argement
    if len(sys.argv) < 3:
        print(f"Error -> Missing argements\nUsage: {sys.argv[0]} <file-name> <pattern>")
        sys.exit(1)
    file_name = sys.argv[1]
    # TODO: get examples of patterns (1 or more)
    pattern = sys.argv[2]

    # get phone numbers tp process
    phone_numbers = get_phone_numbers(file_name)
    if not phone_numbers:
        print(f"Error -> file {file_name} doesn't exist")
        sys.exit()

    # TODO: convert examples to patterns
    # TODO: iterate over patterns

    # get valid phone numbers
    valid_phone_numbers = get_valid_phone_numbers(phone_numbers, pattern)
    print("\n".join(valid_phone_numbers))

# entry-point
if __name__ == "__main__":
    main()
