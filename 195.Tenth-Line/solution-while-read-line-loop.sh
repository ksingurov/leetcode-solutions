N_line_to_print=10
input_file="file.txt"

i=1
while IFS=, read -r line; do
    if [ $i = $N_line_to_print ]; then
        echo "$line"
        break
    fi
    ((i++))
done < "$input_file"
