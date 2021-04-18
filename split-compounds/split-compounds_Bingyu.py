#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li

import sys

def break_down(compound, start_position):
    for n in range(start_position + 3, len(compound) - 2):
        if compound[:n] in freq.keys() or (compound[n-1]=='s' and compound[:n-1] in freq.keys()):
            yield compound[:n]
            break_down(compound[n:], n)

freq = {}
with open('zeit.tagged', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split()[0]
        if line.split()[1] == 'NN' and word.isalpha():
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

            for n in break_down(word, 0):
                print(word + ' ' + n)

