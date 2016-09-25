#hani_7_8
#hani_8_recent
word="삼성전자"

prefix="hani_7_8"
filename=$prefix".txt"

normalized_prefix="normalized_"$prefix
normalized_filename="normalized_"$filename

input="data/"$normalized_filename
output="result/"$normalized_prefix

python3 text_normalizer.py $filename
./fasttext skipgram -input $input -output $output
python3 reader.py $output".vec" $word
