N_line_to_print=10

awk -v N="$N_line_to_print" 'NR==N' file.txt
