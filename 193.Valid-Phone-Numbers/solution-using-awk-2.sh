file='file.txt'

# Given that the variable is defined in bash and then passed to awk with "$"
# extra backslash is required to keep backslash inside awk string
pattern='^(\\([0-9]{3}\\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

awk -v pat="$pattern" '{ if ($0 ~ pat) print }' "$file"

# it could be also run as:
# awk -v pat='^(\\([0-9]{3}\\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' '{ if ($0 ~ pat) print }' "$file"
