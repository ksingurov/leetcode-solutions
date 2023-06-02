from solution import Solution

def main():
    sol = Solution()
    s = input("Enter a string: ")
    res = sol.lengthOfLongestSubstring(s)
    print("The length of the longest substring without duplicate characters is: ", res)

if __name__ =="__main__":
    main()
