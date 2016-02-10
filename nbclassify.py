import os
import re
import math
import sys
import csv

lines = [line.rstrip('\n') for line in open('nbmodel.txt')]

stopList = ['a','about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves']

positiveDict = dict()
positive_prior = float(lines[0])
possize = int(lines[1]) + 2
for i in range(2,possize):
    split = lines[i].split(" ")
    positiveDict[split[0]] = split[1]

negativeDict = dict()
negative_prior = float(lines[possize])
negsize = int(lines[possize+1]) + 2 + possize
for i in range(possize+2,negsize):
    split = lines[i].split(" ")
    negativeDict[split[0]] = split[1]

truthDict = dict()
truth_prior = float(lines[negsize])
truthsize = int(lines[negsize+1]) + 2 + negsize
for i in range(negsize+2,truthsize):
    split = lines[i].split(" ")
    truthDict[split[0]] = split[1]

deceptiveDict = dict()
deceptive_prior = float(lines[truthsize])
deceptivesize = int(lines[truthsize+1]) + 2 + truthsize
for i in range(truthsize+2,deceptivesize):
    split = lines[i].split(" ")
    deceptiveDict[split[0]] = split[1]

def retrieveFiles(directory):
    f = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                if "fold1" in os.path.join(root, file):
                    f.append(os.path.join(root, file))
    return f

fw = open('nboutput.txt','w')
fc = open('result.csv', 'wt')

try:
    list = retrieveFiles(sys.argv[1])
    writer = csv.writer(fc)
    writer.writerow(('FileName','Prediction','Reality','T_TP','T_TN','T_FP','T_FN','D_TP','D_TN','D_FP','D_FN','P_TP','P_TN','P_FP','P_FN','N_TP','N_TN','N_FP','N_FN'))
    i = 1
    for filename in list:
        f = open(filename, "r").read()
        file = re.sub('[^a-zA-Z]', ' ', f)
        pos_posterior = math.log(positive_prior)
        neg_posterior = math.log(negative_prior)
        truth_posterior = math.log(truth_prior)
        deceptive_posterior = math.log(deceptive_prior)
        Truthful = False
        Positive = False
        Negative = False
        Deceptive = False
        T_TP = 0
        T_TN = 0
        T_FP = 0
        T_FN = 0
        D_TP = 0
        D_TN = 0
        D_FP = 0
        D_FN = 0
        P_TP = 0
        P_TN = 0
        P_FP = 0
        P_FN = 0
        N_TP = 0
        N_TN = 0
        N_FP = 0
        N_FN = 0
        lookup = set()

        for word in file.lower().split():
            if word not in stopList:
                lookup.add(word)
        for word in lookup:
            if word in positiveDict:
                pos_posterior += math.log(float(positiveDict[word])/10000.0)
            if word in negativeDict:
                neg_posterior += math.log(float(negativeDict[word])/10000.0)
            if word in truthDict:
                truth_posterior += math.log(float(truthDict[word])/10000.0)
            if word in deceptiveDict:
                deceptive_posterior += math.log(float(deceptiveDict[word])/10000.0)
        if truth_posterior > deceptive_posterior:
                fw.write("truthful ")
                Truthful = True
        else:
                fw.write("deceptive ")
                Deceptive = True
        if pos_posterior > neg_posterior:
                fw.write("positive ")
                Positive = True
        else:
                fw.write("negative ")
                Negative = True
        if Truthful:
            prediction = 'Truthful'
        else:
            prediction = 'Deceptive'
        if Positive:
            p_prediction = 'Positive'
        else:
            p_prediction = 'Negative'
        if 'truthful' in filename:
            reality = 'Truthful'
        else:
            reality = 'Deceptive'
        if 'positive' in filename:
            p_reality = 'Positive'
        else:
            p_reality = 'Negative'
        if prediction == reality and prediction == 'Truthful':
            T_TP = 1
        elif prediction == reality and prediction == 'Deceptive':
            T_TN = 1
        elif prediction == 'Truthful' and reality == 'Deceptive':
            T_FP = 1
        else:
            T_FN = 1
        if prediction == reality and prediction == 'Deceptive':
            D_TP = 1
        elif prediction == reality and prediction == 'Truthful':
            D_TN = 1
        elif prediction == 'Deceptive' and reality == 'Truthful':
            D_FP = 1
        else:
            D_FN = 1
        if p_prediction == p_reality and p_prediction == 'Positive':
            P_TP = 1
        elif p_prediction == p_reality and p_prediction == 'Negative':
            P_TN = 1
        elif p_prediction == 'Positive' and p_reality == 'Negative':
            P_FP = 1
        else:
            P_FN = 1
        if p_prediction == p_reality and p_prediction == 'Negative':
            N_TP = 1
        elif p_prediction == p_reality and p_prediction == 'Positive':
            N_TN = 1
        elif p_prediction == 'Negative' and p_reality == 'Positive':
            N_FP = 1
        else:
            N_FN = 1
        writer.writerow((filename, prediction, reality, T_TP, T_TN, T_FP, T_FN,D_TP, D_TN, D_FP, D_FN,P_TP, P_TN, P_FP, P_FN, N_TP, N_TN, N_FP, N_FN))
        if i == len(list):
            fw.write(filename)
        else:
            fw.write(filename + "\n")
        i += 1
finally:
    fw.close()