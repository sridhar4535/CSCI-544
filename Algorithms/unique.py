def isUnique(str):
    n = len(str)
    char_set = [False] * 256
    for i in range(n):
        if(char_set[ord(str[i])]):
            return False
        char_set[ord(str[i])] = True
    return True

str = "abc"
if isUnique(str):
    print ("The string has all unique characters.")
else:
    print ("The string has non-unique characters.")