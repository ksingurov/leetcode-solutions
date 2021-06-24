awk '{
    for (i=1; i<=NF; i++) {
        content[NR, i] = $i
    }
    max_col = NF
}
END {
    for (i = 1; i <= max_col; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s ", content[j, i]
        }
        print ""
    }
} ' file.txt
