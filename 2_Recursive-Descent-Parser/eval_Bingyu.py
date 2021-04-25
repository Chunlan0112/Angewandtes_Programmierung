#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gruppenmitglieder: Chunlan Ma, Bingyu Xiong, Yiwei Li


# '123' -> 1*10^2 + 2*10^1 + 3*10^0
def integer(expr, startpos):
    switcher = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    zahl_length = 0
    for str_digit in expr[startpos:]:
        digit = switcher.get(str_digit)
        if digit is None:
            break
        zahl_length += 1

    counter = 1
    zahl = 0
    for str_digit in expr[startpos:]:
        digit = switcher.get(str_digit)
        if digit is None:
            break
        zahl += digit * 10 ** (zahl_length - counter)
        counter += 1
    return zahl, startpos + zahl_length


def number(expr, startpos):
    zahl, startpos = integer(expr, startpos)
    try:
        if expr[startpos] != '.':
            return zahl, startpos
        else:
            zahl2, endpos = integer(expr, startpos + 1)
            zahl = zahl + zahl2 * 10 ** (-(endpos - startpos - 1))
            return zahl, endpos
    except IndexError:  # Wenn die Zahl nicht eine Nachkommazahl ist
        return zahl, startpos


def bracketexpr(expr, startpos):
    if expr[startpos] == '(':
        zahl, endpos = addexpr(expr, startpos + 1)
        if expr[endpos] != ')':
            print("Fehler!")
        return zahl, endpos + 1
    elif expr[startpos] == '-':
        zahl, endpos = bracketexpr(expr, startpos + 1)
        return -zahl, endpos
    else:
        return number(expr, startpos)


#  multi  ->  bracket ( */ bracket */ bracket ...)
def mulexpr(expr, startpos):
    zahl, startpos = bracketexpr(expr, startpos)
    while startpos < len(expr) and expr[startpos] in ['*', '/']:
        if expr[startpos] == '*':
            zahl *= bracketexpr(expr, startpos + 1)[0]
            startpos = bracketexpr(expr, startpos + 1)[1]
        elif expr[startpos] == '/':
            zahl /= bracketexpr(expr, startpos + 1)[0]
            startpos = bracketexpr(expr, startpos + 1)[1]
    return zahl, startpos


#  add  ->  multi ( +/- multi +/- multi ...)
def addexpr(expr, startpos):
    zahl, startpos = mulexpr(expr, startpos)
    while startpos < len(expr) and expr[startpos] in ['+', '-']:
        if expr[startpos] == '+':
            zahl += mulexpr(expr, startpos + 1)[0]
            startpos = mulexpr(expr, startpos + 1)[1]
        elif expr[startpos] == '-':
            zahl -= mulexpr(expr, startpos + 1)[0]
            startpos = mulexpr(expr, startpos + 1)[1]
    return zahl, startpos


def start(expr, startpos):
    return addexpr(expr, startpos)


with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().replace(' ', '')
        correct_line = True
        counter = 34

        for ele in line:
            counter += 1
            if not ele.isnumeric() and not ele in ['+', '-', '*', '/', '(', ')', '.']:
                print('Fehler in arithmetischem Ausdruck: ' + line + '\n' + ' '*counter + '^')
                correct_line = False

        if correct_line:
            print(line + ' = ' + "%.2f" % start(line, 0)[0])