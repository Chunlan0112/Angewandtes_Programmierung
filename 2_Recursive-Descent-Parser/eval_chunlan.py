#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li

import sys

num_map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

filename = sys.argv[1]

def start(expr, startpos):
    expr = expr.replace(' ', '')
    zahl, startpos = addexpr(expr, startpos)
    if startpos+1 != len(expr):
        fehler_meldung(expr, startpos)
    else:
        print(expr.replace('\n', '')+'=' + str(round(zahl, 2))+'\n')

def addexpr(expr, startpos):
    zahl, startpos = mulexpr(expr, startpos)
    while startpos < len(expr) and expr[startpos] in ['+', '-']:
        zahl1, end = mulexpr(expr, startpos + 1)
        if expr[startpos] == '+':
            zahl += zahl1
        if expr[startpos] == '-':
            zahl -= zahl1
        startpos = end
    return zahl, startpos

def mulexpr(expr, startpos):
    zahl, startpos = bracketexpr(expr, startpos)
    while startpos < len(expr) and expr[startpos] in ['*', '/']:
        zahl1, end = bracketexpr(expr, startpos+1)
        if expr[startpos] == '*':
            zahl *= zahl1
        if expr[startpos] == '/':
            if zahl1 == 0:
                fehler_meldung(expr, end-1)
                zahl, startpos = None, None
            else:
                zahl /= zahl1
        startpos = end
    return zahl, startpos

def bracketexpr(expr, startpos):
    if expr[startpos] == '(':
        zahl, endpos = addexpr(expr, startpos+1)
        if endpos < len(expr) and expr[endpos] != ')':
            fehler_meldung(expr, endpos)
            zahl, endpos = None, None
        return zahl, endpos + 1
    elif expr[startpos] == '-':
        zahl, endpos = bracketexpr(expr, startpos+1)
        return -zahl, endpos
    else:
        return number(expr, startpos)

def number(expr, startpos):
    zahl, startpos = integer(expr, startpos)
    if startpos+1 < len(expr) and expr[startpos] == '.':
        zahl2, endpos = integer(expr, startpos+1)
        zahl = zahl+zahl2*pow(10, -(endpos-startpos-1))
        return zahl, endpos
    else:
        return zahl, startpos

def integer(expr, startpos, zahl=None):
    try:
        if not zahl:
            zahl = num_map[expr[startpos]]
        if startpos + 1 < len(expr) and expr[startpos+1] in num_map:
            startpos += 1
            zahl *= 10
            zahl2 = num_map[expr[startpos]]
            zahl += zahl2
            return integer(expr, startpos, zahl)
    except KeyError:
        fehler_meldung(expr, startpos)
    else:
        return zahl, startpos + 1

def fehler_meldung(expr, startpos):
    fehler = 'Fehler in arithmetischen Ausdruck: '
    print(fehler + expr.replace('\n', ''))
    print(' '*(len(fehler) + startpos)+'^')


if __name__ == '__main__':
    with open(filename, 'r') as myfile:
        for line in myfile:
            try:
                start(line, 0)
            except TypeError:
                pass
