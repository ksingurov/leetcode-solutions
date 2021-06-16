# bash script to calculate the frequency of each word in a text file

# use awk to iterate over file content and print fields
# awk treats any whitespace as a field separator
# so the is a flattened words.txt with one word on each line
awk '{for(i=1;i<=NF;i++) print $i}' words.txt | 
# sort lines
sort |
# uniq removes consecutive duplicate lines
# -c option counts how many duplicates there were in a row
# given the input is sorted, effectively it produces frequencies of lines
# the output is consist of lines with "word count" 
uniq -c |
# sort lines; -n - sort numerically; -r return in reverse order
sort -nr |
# print second field (word) first and then first filed (its freqency)
awk '{print $2, $1}'
