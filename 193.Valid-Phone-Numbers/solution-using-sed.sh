file='file.txt'

# -n suppresses automatic printing of every line
# -E enables extended regular expressions (ERE), similar to grep
sed -nE '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/p' "$file"
