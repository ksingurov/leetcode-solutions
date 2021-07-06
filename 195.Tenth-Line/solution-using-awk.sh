N_line_to_print=10
input_file="file.txt"

line=$(awk -v N="$N_line_to_print" 'NR==N' "$input_file")

echo "$line"
