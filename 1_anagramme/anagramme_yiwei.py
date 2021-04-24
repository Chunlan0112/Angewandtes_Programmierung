# -*-coding:utf-8 -*-
import string
import re
import sys
import time

PUNCTUATION_STRING = string.punctuation
ROOT="."
SAVE_FLAG="of"

if __name__ == '__main__':
    # set start time
    start_time=time.time()
    # set the parameters
    read_file_name=sys.argv[1]
    # read file
    with open(f"{ROOT}/{read_file_name}.txt", encoding="utf-8") as f:
        count=0
        alphabet_list=[]
        original_list=[]
        line = f.readline()
        while line:
            # delete blank
            word_original=line.split()[0].strip()
            word_sorted=word_original.lower()
            # delete punctuations, numbers
            if word_sorted.isalpha() and len(word_sorted)>=3:
            # build original list and key list
                alphabet_list.append("".join(sorted(word_sorted)))
                original_list.append(word_original)
            line = f.readline()
    dict={}
    for i in range(len(alphabet_list)):
        key=alphabet_list[i]
        word=original_list[i]
        if key in dict.keys():
            same_list=dict[key]
            check_list=[x.lower() for x in dict[key] ]
            if word.lower() in check_list:
                continue
            else:
                same_list.append(word)
                dict[key]=same_list
        else:
            same_list=[word]
            dict[key]=same_list
    # print the dictionary

    savename="{}_result_{}.txt".format(read_file_name,int(time.time()))
    with open(f"{ROOT}/{savename}", 'w',encoding="utf-8") as f:
        for key, value_list in dict.items():
            if len(value_list) >= 2:
                for i in value_list:
                    f.write("{value} ".format(value=i))
                f.write("\n")
                for x in value_list:
                    print(x,end=" ")
                print()
            else:
                continue
    print()
    print("plese check the result in the filesystem")
    # set end time
    end_time=time.time()
    print((end_time-start_time)*1000,"ms")
