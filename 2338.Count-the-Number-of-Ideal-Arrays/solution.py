from itertools import product

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        all_arrays = list(product(range(1, maxValue + 1), repeat=n))
        ideal_arrays = [1 if all(arr[i+1] % arr[i] == 0 for i in range(len(arr) - 1)) else 0 for arr in all_arrays]
        return sum(ideal_arrays)
