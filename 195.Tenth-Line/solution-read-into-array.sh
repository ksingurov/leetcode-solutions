N_line_to_print=10
input_file="file.txt"

lines=()
while IFS= read -r line; do
    lines+=("$line")
done < "$input_file"

index=$((N_line_to_print-1))
echo "${lines[index]}"
