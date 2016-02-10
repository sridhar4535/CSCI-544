def isRotation(str1,str2):
    if len(str1) != len(str2):
        return False
    str = str1 + str1
    if str.find(str2) > -1:
        return True
    else:
        return False

str1 = "waterbottle"
str2 = "erbottlewat"
if isRotation(str1, str2):
    print ("str2 is a rotation of str1.")
else:
    print ("str2 is not a rotation of str1.")