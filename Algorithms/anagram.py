def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    count1 = [0] * 256
    count2 = [0] * 256
    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if isAnagram(str1,str2):
    print ("The strings are anagrams of each other.")
else:
    print ("The string are not anagrams of each other.")