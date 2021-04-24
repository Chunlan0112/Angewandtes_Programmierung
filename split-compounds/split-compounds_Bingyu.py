#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li

import sys

def break_down(compound, start_position, substrings):
    for n in range(start_position + 3, len(compound)):
        if compound[start_position:n] in freq.keys() or (compound[n-1]=='s' and compound[start_position:n-1] in freq.keys()):
            substrings.append(compound[start_position:n])
            break_down(compound[n:], n, substrings)
        if n == len(compound)-1:
            yield from substrings
        break
            #yield compound[start_position:n]



freq = {}
with open('zeit.tagged', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split()[0]
        if line.split()[1] == 'NN' and word.isalpha():
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

            substring_list = [word]
            for substring in break_down(word, 0, substring_list):
                if len(substring_list) >= 2:
                    print(substring_list)

