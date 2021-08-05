file='file.txt'

pattern='^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

grep -E "$pattern" "$file"
