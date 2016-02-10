import os
import re
import sys
from collections import defaultdict

stopList = ['a','about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves']

def dsum(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)

def retrieveFiles(directory):
    f = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                if "fold1" not in os.path.join(root, file):
                    f.append(os.path.join(root, file))
    return f

def updateDict(dictionary,size):
    for key in dictionary:
        dictionary[key] = (float(dictionary[key] + 1)/size) * 10000.0
    return dictionary

def constructHash(directory):
    lookup = dict()
    list = retrieveFiles(directory)

    for filename in list:
        f = open(filename, "r").read()
        file = re.sub('[^a-zA-Z]', ' ', f)
        for word in file.lower().split():
            if word in stopList:
                continue
            if word not in lookup:
                lookup[word] = 1
            else:
                lookup[word] += 1
    return lookup


def writeFile(dictionary):
    fw.write("0.5\n")
    fw.write(str(len(dictionary)) + "\n")
    for entry in dictionary.items():
        fw.write(entry[0] + " " + str(entry[1]) + "\n")

positiveDict = constructHash(sys.argv[1] + "/positive_polarity")
lookup = positiveDict
lookup = dict.fromkeys(lookup, 0)
nD = constructHash(sys.argv[1] + "/negative_polarity")
negativeDict = dsum(lookup,nD)
lookup = nD
lookup = dict.fromkeys(lookup, 0)
positiveDict = dsum(positiveDict,lookup)
pos = constructHash(sys.argv[1] + "/positive_polarity/truthful_from_TripAdvisor")
neg = constructHash(sys.argv[1] + "/negative_polarity/truthful_from_Web")
truthDict = dsum(pos,neg)
lookup = truthDict
lookup = dict.fromkeys(lookup, 0)
posD = constructHash(sys.argv[1] + "/positive_polarity/deceptive_from_MTurk")
negD = constructHash(sys.argv[1] + "/negative_polarity/deceptive_from_MTurk")
dD = dsum(posD,negD)
deceptiveDict = dsum(lookup,dD)
lookup = dD
lookup = dict.fromkeys(lookup, 0)
truthDict = dsum(truthDict,lookup)
fw = open('nbmodel.txt','w')
try:
    positiveCount = sum(positiveDict.itervalues())
    negativeCount = sum(negativeDict.itervalues())
    truthCount = sum(truthDict.itervalues())
    deceptiveCount = sum(deceptiveDict.itervalues())
    updateDict(positiveDict, positiveCount + len(positiveDict))
    updateDict(negativeDict, negativeCount + len(deceptiveDict))
    updateDict(truthDict, truthCount + len(truthDict))
    updateDict(deceptiveDict, deceptiveCount + len(deceptiveDict))
    writeFile(positiveDict)
    writeFile(negativeDict)
    writeFile(truthDict)
    writeFile(deceptiveDict)
finally:
    fw.close()