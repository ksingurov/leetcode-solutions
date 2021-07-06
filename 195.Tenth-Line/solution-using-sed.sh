N_line_to_print=10
input_file="file.txt"

line=$(sed -n "$N_line_to_print"p "$input_file")

echo "$line"
