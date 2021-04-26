# signs and number as default
INTEGER={"0":0,
         "1":1,
         "2":2,
         "3":3,
         "4":4,
         "5":5,
         "6":6,
         "7":7,
         "8":8,
         "9":9}

def S2N (number_str:str)->int:
    strin_len=len(number_str)
    number=0
    for i in range(strin_len):
        number = number + INTEGER[number_str[-1 - i]] * pow(10, i)
    return number

def Integer (expr:str,startpos:int):
    number_string=""
    while expr[startpos] in INTEGER.keys():
        number_string+=expr[startpos]
        if startpos<len(expr)-1:
            startpos+=1
        else:
            break
    number=S2N(number_string)
    endpos=startpos
    return number,endpos

def Number(expr:str,startpos:int):
    number,startpos=Integer(expr=expr,startpos=startpos)
    if expr[startpos]!='.':
        return number,startpos
    else:
        number2,endpos=Integer(expr=expr,startpos=startpos+1)
        number=number+(number2)*pow(10,-(endpos-startpos-1))
        return number,endpos

def Backetexpr(expr:str,startpos:int):
    if expr[startpos]=="(":
        number,endpos=Addexpr(expr,startpos+1)
        if expr[endpos]!=")":
            raise SyntaxError("Erro in arithmetic print : {}".format(expr))
        return number,endpos+1
    elif expr[startpos]=='-':
        number, endpos = Backetexpr(expr, startpos + 1)
        return -number,endpos
    else:
        return Number(expr,startpos)

def Addexpr(expr:str,startspos:int):
    number, startspos = Mulexpr(expr, startspos)
    while (expr[startspos]=="+" or expr[startspos]=="-") and startspos<len(expr):
        if expr[startspos] == "+":
            number2, startspos = Mulexpr(expr, startspos + 1)
            number = number + number2
        elif expr[startspos] == "-":
            number2, startspos = Mulexpr(expr, startspos + 1)
            number = number - number2
    return number,startspos

def Mulexpr(expr:str,startspos:int):
    number, startspos = Backetexpr(expr, startspos)
    while (expr[startspos]=="*" or expr[startspos]=="/") and startspos<len(expr):
        if expr[startspos]=="*":
            number2,startspos=Backetexpr(expr,startspos+1)
            number=number*number2
        elif expr[startspos]=="/":
            number2, startspos = Backetexpr(expr, startspos + 1)
            number = number / number2
    return number,startspos

if __name__ == '__main__':
    test_expr="2*2*2*2\n"
    num,pos=Addexpr(test_expr,0)
    print(num)
    # print(pos)