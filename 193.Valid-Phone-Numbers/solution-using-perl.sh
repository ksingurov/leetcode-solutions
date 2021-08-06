file='file.txt'

# -n reads the file line by line
# -e allow to execute provided string
perl -ne 'print if /^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$/' "$file"
