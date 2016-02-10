def nonrepeat(str):
    count = [0] * 256
    for i in str:
        count[ord(i)] += 1
    for i in range(256):
        if count[i] > 1:
            print (chr(i))

str = "Geeeeekksqdqd"
nonrepeat(str)

"""
def nonrepeat(str):
    count = [0] * 256
    for i in str:
        count[ord(i)] += 1
    for i in str:
        if count[ord(i)] > 1:
            print (i)
            break

str = "Gkksdqd"
nonrepeat(str)
"""