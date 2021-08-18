file='file.txt'

pattern='^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

# -n suppresses automatic printing of every line
# -E enables extended regular expressions (ERE), similar to grep
# p after the pattern - prints the line matching the pattern
sed -nE "/$pattern/p" "$file"
