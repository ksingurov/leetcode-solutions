firsts=""
seconds=""

while IFS= read -r line; do
  read first second <<< "$line"
  firsts+="$first "
  seconds+="$second "
done < file.txt

echo $firsts
echo $seconds
