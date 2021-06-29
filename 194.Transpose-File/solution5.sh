# Script to transpose content of a txt file with bash (no awk)

# Count the number of words (columns) in the first line of the file
columns=$(head -n 1 file.txt | wc -w)

# Loop over each column index (1 to number of columns)
for i in $(seq "$columns"); do
    # Initialize a variable to hold the output line
    line_to_print=""
    while read -r -a line; do
        # Index to 
        index=$((i - 1))
        # no space for the first value in the line to be printed
        if [ -z "$line_to_print" ]; then
            line_to_print="${line[$index]}"
        # for the rest add space
        else
            line_to_print="$line_to_print ${line[$index]}"
        fi
    done < file.txt
    # after composing a line print it
    echo "$line_to_print"
done
