import time
start_time = time.time()
tags_words = []
tags_words_dict = {}
tags_dict = {}
len_transition = {}
len_emission = {}
word_dict = {}
for sent in open('catalan_corpus_train_tagged.txt'):
    tags_words.append(("START", "START"))
    words = sent.split()
    if "START" in tags_dict:
        tags_dict["START"].append(words[0][-2:])
    else:
        tags_dict["START"] = [words[0][-2:]]
    for i, word in enumerate(words):
        if i != len(words):
            if word[:-3] in word_dict:
                word_dict[word[:-3]].add(word[-2:])
            else:
                word_dict[word[:-3]] = set()
                word_dict[word[:-3]].add(word[-2:])
            if word[-2:] in tags_words_dict:
                tags_words_dict[word[-2:]].append(word[:-3])
            else:
                tags_words_dict[word[-2:]] = [word[:-3]]
            if i + 1 < len(words):
                if word[-2:] in tags_dict:
                    tags_dict[word[-2:]].append(words[i+1][-2:])
                else:
                    tags_dict[word[-2:]] = [words[i+1][-2:]]
                tags_words.extend([(word[-2:],word[:-3])])

tags = [tag for (tag, word) in tags_words]
distinct_tags = set(tags)

words = [word for (tag, word) in tags_words]
distinct_words = set(words)

emission_prob_dictionary = {}
transition_prob_dictionary = {}

list = []
for tag in tags_words_dict:
    list = tags_words_dict[tag]
    dictionary = {}
    for word in list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    emission_prob_dictionary[tag] = dictionary
    len_emission[tag] = len(list)

list = []
for tag in tags_dict:
    list = tags_dict[tag]
    dictionary = {}
    for follow_tag in list:
        if follow_tag in dictionary:
            dictionary[follow_tag] += 1
        else:
            dictionary[follow_tag] = 1
    transition_prob_dictionary[tag] = dictionary
    len_transition[tag] = len(list)


temp_transition = {}

for tag in distinct_tags:
    temp_transition[tag] = 0


for key in transition_prob_dictionary:
    transition_dictionary = {}
    transition_dictionary.update(temp_transition)
    transition_dictionary.update(transition_prob_dictionary[key])
    transition_prob_dictionary[key] = transition_dictionary


target = open('hmmmodel.txt', 'w')
try:
    target.write(str(emission_prob_dictionary))
    target.write("\n")
    target.write(str(transition_prob_dictionary))
    target.write("\n")
    target.write(str(distinct_tags))
    target.write("\n")
    target.write(str(distinct_words))
    target.write("\n")
    target.write(str(len_transition))
    target.write("\n")
    target.write(str(len_emission))
    target.write("\n")
    target.write(str(word_dict))
finally:
    target.close()

print("--- %s seconds ---" % (time.time() - start_time))