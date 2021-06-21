firsts=""
seconds=""

while IFS= read -r line; do
  set -- $line 
  firsts+="$1 "
  [ -n "$2" ] && seconds+="$2 "
done < file.txt

echo $firsts
echo $seconds
