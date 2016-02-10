import sys

result = []
def extract_comb(s,l):

    if l == len(s) - 1:
        result.append(s)
    else:
        for i in range(l, len(s)):
            t = list(s)
            t[l], t[i] = t[i], t[l]
            s = ''.join(t)
            extract_comb(s, l + 1)
            t = list(s)
            t[l], t[i] = t[i], t[l]
            s = ''.join(t)

file = open("anagram_out.txt", "w")
string = sys.argv[1]
extract_comb(string,0)
result.sort()
for i in range(len(result)):
    file.write(result[i]+"\n")