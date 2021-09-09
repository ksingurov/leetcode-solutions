import sys
import re
from typing import Match

# function to return all phone numbers from the file
# return None if file doesn't exists
def get_phone_numbers(file_name: str) -> list[str] | None:
    try:
        with open(file_name, "r") as file:
            phone_numbers = [line.rstrip("\n") for line in file]
        return phone_numbers
    except FileNotFoundError:
        return None

# TODO: function to check that example only contains alphanumeric, (), -, and " "

# function to create a string with format "\d{n}", where n is lenght of a matched string
def digits_sequence(match: Match[str]) -> str:
    sequence_lenght = match.end() - match.start()
    return r"\d{" + str(sequence_lenght) + "}"

# function to substitute all alphanumeric sequences with string "\d{n}", where n is the lenght of the sequence
# uses function defined earlier as an repl parameters in re.sub
def convert_to_pattern(phone_example) -> str:
    # return "^" + re.sub(pattern=r"[A-Za-z0-9_]+", repl=digits_sequence, string=phone_example) + "$"
    result = re.sub(pattern=r"[A-Za-z0-9_]+", repl=digits_sequence, string=phone_example)
    return "^" + re.escape(result) + "$"

# function to return valid phone numbers
def get_valid_phone_numbers(phone_numbers: list[str], pattern: str) -> list[str]:
    return [pn for pn in phone_numbers if re.search(pattern, pn)]

# main function
def main():
    # handle input argement
    if len(sys.argv) < 3:
        print(f"Error -> Missing argements\nUsage: {sys.argv[0]} <file-name> <example> [<example2> ... <exampleN>]")
        sys.exit(1)
    file_name = sys.argv[1]
    examples = sys.argv[2:]

    # get phone numbers tp process
    phone_numbers = get_phone_numbers(file_name)
    print(f"[DEBUG]: phone_numbers -> {phone_numbers}")
    if not phone_numbers:
        print(f"Error -> file {file_name} doesn't exist")
        sys.exit()

    #convert examples to patterns; set is used to avoid identical patterns
    patterns = {convert_to_pattern(example) for example in examples}
    # print(f"[DEBUG]: patterns -> {patterns}")

    # get valid phone numbers
    valid_phone_numbers = []
    for pat in patterns:
        valid_phone_numbers += get_valid_phone_numbers(phone_numbers, pat)
        # print(f"[DEBUG]: pat -> {repr(pat)}")
        # print(f"[DEBUG]: valid_phone_numbers -> {valid_phone_numbers}")
    print("\n".join(valid_phone_numbers))

# entry-point
if __name__ == "__main__":
    main()
