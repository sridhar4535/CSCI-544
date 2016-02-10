def duplicatewords(str):
    wordList = []
    stringList = str.split(" ")
    for i in stringList:
        if i not in wordList:
            wordList.append(i)
    print(' '.join(word for word in wordList))

duplicatewords("Hello Hello WTF WTF Sri Sri sri")