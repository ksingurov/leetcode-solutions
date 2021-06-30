N_line_to_print=10
input_file="file.txt"

# line=$(head -n "$N_line_to_print" "$input_file" | tail -n 1)

line=$(tail -n +"$N_line_to_print" "$input_file" | head -n 1)

echo "$line"
