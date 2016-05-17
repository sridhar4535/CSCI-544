from itertools import izip
import math
import sys
import os
import io

def ngrams(input_data, n):
  data = input_data.split()
  ngram_dict = {}
  for i in range(len(data)-n+1):
    term = ' '.join(data[i:i+n]).lower()
    ngram_dict.setdefault(term, 0)
    ngram_dict[term] += 1
  return ngram_dict

f = [sys.argv[1]]
if not sys.argv[2].endswith(".txt"):
    for root, dirs, files in os.walk(sys.argv[2]):
        for fname in files:
                f.append(os.path.join(root, fname))
else:
    f.append(sys.argv[2])

files = [io.open(i,'r', encoding='utf-8') for i in f]
pN = 0
c = 0
r = 0
for i in range(1, 5):
    numerator = 0
    denominator = 0
    ref_ngram = {}
    for rows in izip(*files):
        cand_ngram = ngrams(rows[0], i)
        for j in range(1, len(files)):
            ref_ngram[j] = ngrams(rows[j], i)
        if i == 1:
            c += sum(cand_ngram.values())
            ref = sum(ref_ngram[1].values())
            for key in ref_ngram:
                if sum(ref_ngram[key].values()) - sum(cand_ngram.values()) < ref - sum(cand_ngram.values()):
                    ref = sum(ref_ngram[key].values())
            r += ref
        denominator += sum(cand_ngram.values())
        for key in cand_ngram:
            val = 0
            for ref_key in ref_ngram:
                if key in ref_ngram[ref_key]:
                    val = max(val,ref_ngram[ref_key][key])
            numerator += min(val, cand_ngram[key])
    for l in range(0, len(files)):
        files[l].seek(0)
    pN += math.log(float(numerator)/denominator) / 4


if c > r:
    BP = 1
else:
    BP = math.exp(1 - float(r)/c)

BLEU = BP * math.exp(pN)

target = open('bleu_out.txt', 'w')
try:
    target.write(str(BLEU))
finally:
    target.close()