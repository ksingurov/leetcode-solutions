# Script to transpose content of a txt file using awk
# where each row has the same number of columns, and each field is separated by the ' ' character

# Script Logic
# For each line:
#   Iterate over each field i (from 1 to number of fields NF).
#   Store the field value $i into 2D-array with indeces = (NR, i).
#   Then run nested loop: outer - over fields (1...NF), inner over rows (1...NR)
#   Inside inner loop print the same field (from outer loop) for each row
#   After each inner loop print new line

awk '{
    for (i=1; i<=NF; i++) {
        content[NR, i] = $i
    }
}
END {
    for (i = 1; i <= NF; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s ", content[j, i]
        }
        print ""
    }
} ' file.txt
