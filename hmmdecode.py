import time
start_time = time.time()
file_data = open('hmmmodel.txt', 'r').read()
data_split_list = file_data.split("\n")
tags_words_dict = eval(data_split_list[0])
tags_dict = eval(data_split_list[1])
distinct_tags = eval(data_split_list[2])
distinct_words = eval(data_split_list[3])
len_transition = eval(data_split_list[4])
len_emission = eval(data_split_list[5])
words_dict = eval(data_split_list[6])
target = open('hmmoutput.txt', 'w')
try:
    for sent in open('catalan_corpus_dev_raw.txt'):
        sentence = sent.split()
        sentlen = len(sentence)
        viterbi = []
        backpointer = []
        first_viterbi = {}
        first_backpointer = {}
        if sentence[0] in distinct_words:
                tag_list = words_dict[sentence[0]]
        else:
            tag_list = distinct_tags
        for tag in tag_list:
            if tag == "START": continue
            if sentence[0] in distinct_words:
                first_viterbi[tag] = float(tags_dict['START'][tag] + 1)/float(len(tags_dict['START']) + len_transition['START']) * float(tags_words_dict[tag][sentence[0]])/float(len_emission[tag])
            else:
                first_viterbi[tag] = float(tags_dict['START'][tag] + 1)/float(len(tags_dict['START']) + len_transition['START'])
            first_backpointer[ tag ] = "START"

        viterbi.append(first_viterbi)
        backpointer.append(first_backpointer)

        max = 0.0
        currbest = first_viterbi.keys()[0]
        for tag in first_viterbi.keys():
            if first_viterbi[tag] >= max:
                max = first_viterbi[tag]
                currbest = tag

        for wordindex in range(1, len(sentence)):
            this_viterbi = { }
            this_backpointer = { }
            prev_viterbi = viterbi[-1]
            if sentence[wordindex] in distinct_words:
                tag_list = words_dict[sentence[wordindex]]
            else:
                tag_list = distinct_tags
            for tag in tag_list:
                if tag == "START": continue

                if sentence[wordindex] in distinct_words:

                    best_previous = prev_viterbi.keys()[0]
                    max = 0.0
                    for prevtag in prev_viterbi.keys():
                        val = prev_viterbi[ prevtag ] * float(tags_dict[prevtag][tag] + 1)/float(len(tags_dict[prevtag]) + len_transition[prevtag]) * float(tags_words_dict[tag][sentence[wordindex]])/float(len_emission[tag])
                        if val >= max:
                            max = val
                            best_previous = prevtag

                    this_viterbi[ tag ] = prev_viterbi[ best_previous] * \
                        float(tags_dict[best_previous][tag] + 1)/float(len(tags_dict[best_previous]) + len_transition[best_previous]) * float(tags_words_dict[tag][sentence[wordindex]])/float(len_emission[tag])
                else:

                    best_previous = prev_viterbi.keys()[0]
                    max = 0.0
                    for prevtag in prev_viterbi.keys():
                        val = prev_viterbi[ prevtag ] * float(tags_dict[prevtag][tag] + 1)/float(len(tags_dict[prevtag]) + len_transition[prevtag])
                        if val >= max:
                            max = val
                            best_previous = prevtag

                    this_viterbi[ tag ] = prev_viterbi[ best_previous] * \
                        float(tags_dict[best_previous][tag] + 1)/float(len(tags_dict[best_previous]) + len_transition[best_previous])
                this_backpointer[ tag ] = best_previous

            max = 0.0
            currbest = this_viterbi.keys()[0]
            for tag in this_viterbi.keys():
                if this_viterbi[tag] >= max:
                    max = this_viterbi[tag]
                    currbest = tag

            viterbi.append(this_viterbi)
            backpointer.append(this_backpointer)
        prev_viterbi = viterbi[-1]
        best_previous = prev_viterbi.keys()[0]
        max = 0.0
        for prevtag in prev_viterbi.keys():
            val = prev_viterbi[ prevtag ] * float(tags_dict[prevtag][currbest] + 1)/float(len(tags_dict[prevtag]) + len_transition[prevtag])
            if val >= max:
                max = val
                best_previous = prevtag

        prob_tagsequence = prev_viterbi[ best_previous ] * float(tags_dict[best_previous][currbest] + 1)/float(len(tags_dict[best_previous]) + len_transition[best_previous])

        best_tagsequence = [ best_previous ]
        backpointer.reverse()
        current_best_tag = best_previous
        for bp in backpointer:
            best_tagsequence.append(bp[current_best_tag])
            current_best_tag = bp[current_best_tag]

        best_tagsequence.reverse()
        best_tagsequence.pop(0)
        count = 1
        for w, t in zip(sentence, best_tagsequence):
            if count < len(sentence):
                target.write(w+"/"+t+" ")
                count += 1
            else:
                target.write(w+"/"+t)
        target.write("\n")
finally:
    target.close()

print("--- %s seconds ---" % (time.time() - start_time))