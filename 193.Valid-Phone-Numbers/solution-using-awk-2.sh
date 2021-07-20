file='file.txt'

pattern='^(\\([0-9]{3}\\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

awk -v pat="$pattern" '{ if ($0 ~ pat) print }' "$file"
