# words = ["ab","cd","ef"]
words = ["foo","bar"]
s = "barfoothefoobarman"

words = ["foo", "foo"]
s = "foofoobar"


n = len(words)
l = len(words[0])

import itertools
import re

# -----------------------
# solution 1: brute force

permutations  = set(itertools.permutations(words, n))
# print("Concatenated strings:", concatenated_strings)  
# print("Concatenated strings:", permutations)
# for p in permutations:
#     print(''.join(p))

# concantenated_strings = set([''.join(p) for p in permutations])
# # print("Concatenated strings:", concantenated_strings)

# for c in concantenated_strings:
#     # print(c)
#     index = s.find(c)
#     if index != -1:
#         print("yes", c, "found at index", index)

# ------------------------
# solution 2: smarter way

occurrences = []
for w in words:
    # re.finditer(w, s)
    matches = [match.start() for match in re.finditer(w, s)]
    if len(matches) == 0:
        print("No match found for word:", w)
        break
    # occurrences.append([w, matches])
    occurrences.append(matches)
    # print(w, matches)
# print("Occurrences of each word in the string:", occurrences)

# sequences = set()
sequences = []
for perm in itertools.permutations(occurrences):
    # sequences.add(itertools.product(*perm))
    sequences.extend(itertools.product(*perm))
print("\nAll possible sequences of indices:", sequences)

# valid_c = [c for c in itertools.product(*occurrences) if all(c[i + 1] - c[i] == l for i in range(n - 1))]
valid_c = [c for c in sequences if all(c[i + 1] - c[i] == l for i in range(n - 1))]
print("Valid combinations of indices:", valid_c)

starting_indices = list({c[0] for c in sequences if all(c[i + 1] - c[i] == l for i in range(n - 1))})
print("Starting indices of valid combinations:", starting_indices)
