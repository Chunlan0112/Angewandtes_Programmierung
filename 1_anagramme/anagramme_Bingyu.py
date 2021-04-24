#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li
# Führe das Programm mit 'python3 anagramme.py zeit.tagged' aus

import sys

anagrams = {}
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split()[0]  # Lese alle Wörter in der ersten Spalte der Datei ein

        # Wenn die Wörter mehr als drei Buchstaben und keine andere Zeichen als Buchstaben haben
        if len(word) >= 3 and word.isalpha():
            letters = sorted(word.lower())
            sorted_word = ''
            for i in letters:
                sorted_word += i  # Erstelle die sortierte Liste von Buchstaben

            if sorted_word not in anagrams:  # Wenn das Dict noch nicht die sortierte Buchstabenliste als Key hat
                anagrams[sorted_word] = {word}  # Nimm die Menge von diesem Wort als Value
            else:
                anagrams[sorted_word].add(word)  # Sonst füge Anagramme in die Menge hinzu

            # Lösche die Duplikate mit unterschiedlichen Klein/Großschreibungen
            for n in range(0, len(anagrams[sorted_word])):
                if word.lower() == list(anagrams[sorted_word])[n]:
                    anagrams[sorted_word].discard(list(anagrams[sorted_word])[n])
                    break

for word_set in anagrams.values():
    if len(word_set) >= 2:  # Wenn die Mengen mehr als 2 Elemente haben, werden die Mengen ausgegeben
        print(word_set)  
