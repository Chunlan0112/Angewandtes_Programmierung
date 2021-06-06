import sys

filename=sys.argv[1]

def levenshtein(s, t):
    n=len(s)
    m=len(t)
    s=' '+s #' ' fuer die erste Spalte inizialisieren
    t=' '+t #' ' fuer die erste Zeile inizialisieren
    tabelle = [[]for _ in range(n+1)] #Tabelle inizialisieren
    for i in range(n+1):
        for k in range(m+1):
            if i == 0: #die erste Spalte inizialisieren
                tabelle[0].append(k)
            elif k == 0: #die erste Zeile inizialisieren
                tabelle[i].append(i)
            else:
                if s[i] == t[k]:
                    a = tabelle[i-1][k-1]
                else:
                    a = tabelle[i-1][k-1]+1
                b = tabelle[i-1][k]+1
                c = tabelle[i][k-1]+1
                tabelle[i].append(sorted([a,b,c])[0])
    min_abstand = tabelle[-1][-1]

    flur = []
    y = len(t)-1 #' '+t  choosed position index
    for x in range(n, 0, -1):
        diagonal = tabelle[x-1][y-1]
        links = tabelle[x][y-1]
        oben = tabelle[x-1][y]
        min = diagonal
        if oben < min:
            if links < oben:
                flur.append((' ', t[y]))
                y -= 1
            else:
                flur.append((s[x], ' '))
                x -= 1
        else:
            if links < min:
                flur.append((' ', t[y]))
                y -= 1
            else:
                flur.append((s[x], t[y]))
                x -= 1
                y -= 1
    print(min_abstand)
    for a, b in flur[::-1]:
         print(f"{a}:{b}", end=' ')
    return min_abstand, flur

with open(filename, 'r') as myfile:
    for line in myfile:
        s = line.strip().split('\t')
        print(s)
        #levenshtein(s[0],s[1])

    #levenshtein('abgegeben', 'abgibt')
