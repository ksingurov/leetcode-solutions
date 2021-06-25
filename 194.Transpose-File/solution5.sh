lines=$(wc -l < file.txt | xargs)

columns=$(head -n 1 file.txt | wc -w | xargs)

# echo "lines: $lines"
# echo "columns: $columns"

line_to_print=""
while read -r -a line; do
    # echo "${line[0]}"
    if [ -z "$line_to_print" ]; then
        line_to_print="${line[0]}"
    else
        line_to_print="$line_to_print ${line[0]}"
    fi
done < file.txt
echo "$line_to_print"
