#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li

string1 = 'abgibt'
string2 = 'abgegeben'
length1 = len(string1)
length2 = len(string2)

# Tabelle initialisieren
tabelle = []
for spalte in range(length1 + 1):
    tabelle.append([])
    for zeile in range(length2 + 1):
        tabelle[spalte].append([])

# Default Werte für erste Spalte und erste Zeile bestimmen
tabelle[0][0] = 0
for n in range(length1):
    tabelle[n + 1][0] = tabelle[n][0] + 1
for m in range(length2):
    tabelle[0][m + 1] = tabelle[0][m] + 1

# Tabelle einfügen
for i in range(1, length1 + 1):
    for k in range(1, length2 + 1):
        if string1[i - 1] != string2[k - 1]:
            tabelle[i][k] = min(tabelle[i - 1][k - 1] + 1, tabelle[i - 1][k] + 1, tabelle[i][k - 1] + 1)
        else:
            tabelle[i][k] = min(tabelle[i - 1][k - 1], tabelle[i - 1][k] + 1, tabelle[i][k - 1] + 1)

operations = []
def operation(spalte, zeile):
    if (0 < spalte <= length1) & (0 < zeile <= length2):
        if string1[spalte - 2] != string2[zeile - 2]:
            if min(tabelle[spalte - 1][zeile - 1], tabelle[spalte - 1][zeile], tabelle[spalte][zeile - 1]) == \
                    tabelle[spalte - 1][zeile - 1]:
                operations.append(str(string2[zeile - 1]) + ':' + str(string1[spalte - 1]))
                operation(spalte - 1, zeile - 1)
            elif min(tabelle[spalte - 1][zeile - 1], tabelle[spalte - 1][zeile], tabelle[spalte][zeile - 1]) == \
                    tabelle[spalte - 1][zeile]:
                operations.append(':' + str(string1[spalte - 1]))
                operation(spalte - 1, zeile)
            else:
                operations.append(str(string2[zeile - 1]) + ':')
                operation(spalte, zeile - 1)
        else:
            if min(tabelle[spalte - 1][zeile - 1], tabelle[spalte - 1][zeile] + 1, tabelle[spalte][zeile - 1] + 1) == \
                    tabelle[spalte - 1][zeile - 1]:
                operations.append(str(string2[zeile - 1]) + ':' + str(string1[spalte - 1]))
                operation(spalte - 1, zeile - 1)
            elif min(tabelle[spalte - 1][zeile - 1], tabelle[spalte - 1][zeile] + 1, tabelle[spalte][zeile - 1] + 1) == \
                    tabelle[spalte - 1][zeile] + 1:
                operations.append(':' + str(string1[spalte - 1]))
                operation(spalte - 1, zeile)
            else:
                operations.append(str(string2[zeile - 1]) + ':')
                operation(spalte, zeile - 1)


print('Levenshtein-Abstand:', tabelle[length1][length2])
operation(length1, length2)
operations.reverse()
for s in operations:
    print(s)
