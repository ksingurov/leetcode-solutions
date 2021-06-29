columns=$(head -n 1 file.txt | wc -w)

for i in $(seq "$columns"); do
    line_to_print=""
    while read -r -a line; do
        if [ -z "$line_to_print" ]; then
            line_to_print="${line[$i-1]}"
        else
            line_to_print="$line_to_print ${line[$i-1]}"
        fi
    done < file.txt
    echo "$line_to_print"
done
