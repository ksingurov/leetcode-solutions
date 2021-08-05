file='file.txt'

pattern='^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

# -E enables extended regular expressions (ERE)
# and allow to use special regex syntax which are used in the pattern
grep -E "$pattern" "$file"
