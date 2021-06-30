# Script to transpose content of a txt file with bash (no awk)
# Reads file just once into array

# Read the file into array
lines=()
while IFS= read -r line; do
    lines+=("$line")
done < file.txt

# Count the number of rows (number of elements in the array) and of columns (words in the first element)
n_rows="${#lines[@]}"
IFS=' ' read -r -a first_line <<< "${lines[0]}"
n_columns=${#first_line[@]}

# Loop over number of column (i.e. how many line needs to be printed)
for ((col=0; col<n_columns; col++)); do
    # Initialize a variable to hold the output line
    line_to_print=""
    # Loop over number of rows and append element from a given row to the output line
    for ((row=0; row<n_rows; row++)); do
        IFS=' ' read -r -a line_fields <<< "${lines[$row]}"
        line_to_print="$line_to_print ${line_fields[$col]}"
    done
    # after composing a line trim it (first element is added with space in front) and print it
    echo "${line_to_print# }"
done
