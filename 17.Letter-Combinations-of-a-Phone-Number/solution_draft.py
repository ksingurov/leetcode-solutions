
phone_numbers = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

digits = "23"
combinmations = [digits]
# print(combinmations)
# combinmations = ["a2", "b2", "c2"]
# combinmations = ["22"]

def generate_combinations(combinmations, index=0):
    # print("index:", index, "len:", len(combinmations[0]))
    if index == len(combinmations[0]):
        # print("index:", index, "len:", len(combinmations[0]))
        return combinmations
    new_combinations = []
    for c in combinmations:
        # print(c, c[:index], c[index + 1:])
        new_combinations += [c[:index] + letter + c[index + 1:] for letter in phone_numbers[c[index]]]
    # return new_combinations
    return generate_combinations(new_combinations, index + 1)

# print(generate_combinations(combinmations, index=1))
print(generate_combinations(combinmations, index=0))
