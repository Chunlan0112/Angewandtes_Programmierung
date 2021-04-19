#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li

import sys
import collections

filename = sys.argv[1]

all_word = []
with open(filename, 'r') as myfile:
    for line in myfile:
        try:
            word, tag, lemma = line.split()
        except ValueError:  #some lines have more than three element
            pass
        if tag == 'NN':
            if word.isalnum() and len(word) >= 3:
                all_word.append(word)

#count word frequency into a dict
freq_dict = collections.Counter(word.lower() for word in all_word)
no_repete_word = freq_dict.keys()

def compound(wort, freq_dict, s=0, zerlegung=[]):
    L = len(wort)
    if s==L:
        yield zerlegung
    else:
        for e in range(s, L+1):
            subword = wort[s:e]
            if subword in freq_dict:
                yield from compound(wort, freq_dict, e, zerlegung+[subword])
                if e < len(wort)-3 and wort[e] == 's':
                    yield from compound(wort, freq_dict, e+1, zerlegung+[subword])

#calculate scores of each split form
for word in no_repete_word:
    scores = dict()
    for ele in compound(word, freq_dict):
        grade = 1
        for el in ele:
            grade *= freq_dict[el]
        scores[tuple(ele)] = round(pow(grade, 1/len(ele)), 1)
    sorted_results = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    for words, score in sorted_results:
        print(word.capitalize(), score, ' '.join(word.capitalize() for word in words), sep="\t")
