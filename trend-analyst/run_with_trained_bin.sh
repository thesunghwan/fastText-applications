#normalized_hani_7_8.txt
#normalized_hani_8_recent.txt
word="삼성전자"
prefix="hani_7_8"
normalized_prefix="normalized_"$prefix
output="result/"$normalized_prefix

python3 reader.py $output".vec" $word
