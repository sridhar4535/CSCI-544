import sys
UTF16Stream = []

def decode(w1):

    a = 256*ord(w1[0]) + ord(w1[1])

    return a

fr = open(sys.argv[1],'rb')
fw = open('utf8encoder_out.txt','w')

try:
    byte = fr.read(2)
    while byte:
        UTF16Stream.append(byte)
        byte = fr.read(2)

    for x in UTF16Stream:
        string = str('{0:08b}'.format((decode(x))))
        if decode(x) < 128:
            result = '0' + string
            fw.write(chr(int(result,2)))

        elif decode(x) < 2048:
            result = '1100000010000000'
            diff = len(result) - len(string)
            for i in range(diff):
                string = '0' + string
            string = string[::-1]
            result = result[::-1]
            s = list(string)
            r = list(result)

            for i in range(6):
                r[i] = s[i]
            for j in xrange(8,13):
                i += 1
                r[j] = s[i]
            string = ''.join(s)
            result = ''.join(r)[::-1]
            fw.write(chr(int(result[:8],2)) + chr(int(result[8:],2)))


        else:
            result = '111000001000000010000000'
            diff = len(result) - len(string)
            for i in range(diff):
                string = '0' + string
            string = string[::-1]
            result = result[::-1]

            s = list(string)
            r = list(result)

            for i in range(6):
                r[i] = s[i]
            for j in xrange(8,14):
                i += 1
                r[j] = s[i]
            for l in xrange(16,20):
                i += 1
                r[l] = s[i]
            string = ''.join(s)
            result = ''.join(r)[::-1]
            fw.write(chr(int(result[:8],2)) + chr(int(result[8:16],2)) + chr(int(result[16:],2)))

finally:
    fr.close()
    fw.close()