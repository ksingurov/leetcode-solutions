n = 3

# left = "(" * (n - 1)
# right = ")" * n

# res = ["("]
# for i in range(2 * n - 1):
#     print(i)

# -------------------------

# n = 3

# left = n - 1
# right = n

# def generate(current, left, right):
#     if left > 0:
#         # new = [current[0] + left.pop(0), current[0] + right.pop(0)]
#         # new1 = current[0] + "("
#         # new2 = current[0] + ")"
#         new = [generate(current[0] + "(", left - 1, right), generate(current[0] + ")", left, right - 1)]
#         # for n in new:
#     else:
#         new = [current[0] + ")" * right]
#     return new

# -------------------------

# n = 3

# left = n - 1
# right = n

# current = [("(", 2, 3)]
# def generate(current):
#     if len(current[0][0]) == n:
#         return current
#     next_current = []
#     for elem in current:
#         if elem[1] > 0:
#             new = generate([(elem[0] + "(", elem[1] - 1, elem[2]), (elem[0] + ")", elem[1], elem[2] - 1)])
#         else:
#             new = [elem[0] + ")" * elem[2]]
#         print("new:", new)
#         print("next_current:", next_current)
#         next_current = next_current + new
#     return next_current
    
# print("result: ", generate([("(", 2, 3)]))


# -------------------------

n = 3

# combinations = ["("]
# combinations = ['((', '()']
# combinations = ["((()))"]
combinations = [""]
new_combinations = []
def generate(combinations):
    if len(combinations[0]) == 2 * n:
        print("returning combinations:", combinations)
        return combinations
    print("generating combinations from:", combinations)
    new_combinations = []
    for c in combinations:
        # print("current combination:", c)
        # left_count = c.count("(")
        # right_count = c.count(")")
        open_count = c.count("(") - c.count(")")
        # c_len = len(c)
        if open_count == 0:
            new_combinations.append(c + "(")
        # elif open_count == n:
        #     new_combinations.append(c + ")")
        # elif c_len > n:
        #     new_combinations.append(c + ")")
        elif open_count == n or len(c) > n:
            new_combinations.append(c + ")")
        else:
            # new_combinations.append(c + "(")
            # new_combinations.append(c + ")")
            new_combinations.extend([c + "(", c + ")"])
    # return new_combinations
    return generate(new_combinations)

res = generate(combinations)
print("result: ", res)

# print('smth')