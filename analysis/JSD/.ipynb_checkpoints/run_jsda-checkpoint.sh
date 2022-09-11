echo ${1} ${2}
echo "1gram"
python run_jsda.py -f1 ./data/ngrams/${1}.raw.1gram -f2 ./data/ngrams/${2}.raw.1gram
echo "2gram"
python run_jsda.py -f1 ./data/ngrams/${1}.raw.2gram -f2 ./data/ngrams/${2}.raw.2gram
echo "3gram"
python run_jsda.py -f1 ./data/ngrams/${1}.raw.3gram -f2 ./data/ngrams/${2}.raw.3gram
echo "4gram"
python run_jsda.py -f1 ./data/ngrams/${1}.raw.4gram -f2 ./data/ngrams/${2}.raw.4gram
echo "len"
python run_wasser.py ./data/ngrams/${1}.raw.len ./data/ngrams/${2}.raw.len
