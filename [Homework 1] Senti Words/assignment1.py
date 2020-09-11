# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:40:05 2020

@author: rjnsa

read the file
strip tabs, whitespaces
check to see if the word in the line exist in the positive words list
get the word after that
append it to a dictinary and the count as value
"""
path="positive-words.txt"
def loadWords():
    wordList =[]
    file = open(path)
    for line in file:
        wordList.append(line.strip())
    return wordList

def findNextWord():
    d ={}
    positive_words=loadWords()
    fin=open("textfile")
    for line in fin:
        line=line.lower().strip()
        words=line.split(' ')
        for word in words:
            if word in positive_words:
                nextWord = words[words.index(word) + 1]
                if nextWord in d.keys():
                    d[nextWord]+=1
                else:
                    d[nextWord]=1
            
    return d

result = findNextWord()
freqKey = max(result, key=result.get)
print(freqKey)