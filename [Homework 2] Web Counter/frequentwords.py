# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:58:36 2020

@author: rjnsa
"""

import re
from nltk.corpus import stopwords
import requests


def getUrl(url):
     response=requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' })    
     if response:
         response=response.text 
     else: print ('failed attempt')
     return response
 

def ProcessData(url):
    freq = {}
    stopLex=set(stopwords.words('english'))
    urlText = getUrl(url)
    text=re.sub('[^a-z]',' ',urlText.lower())
    words=text.split(' ')
    for word in words: 
            if word=='' or word in stopLex:continue  
            else: freq[word]=freq.get(word,0)+1
    return freq
    

def fetchWords(url1, url2, url3):
    result = []
    urlText1 = ProcessData(url1)
    urlText2 = ProcessData(url2)
    urlText3 = ProcessData(url3)
    for word in urlText2.keys():
        print(word)
        if word in urlText3.keys() and word in urlText1.keys():
            if (urlText3[word] > urlText2[word] and (urlText2[word] > urlText1[word])):
               result.append(word)        
    return set(result)
    

print(fetchWords
('https://gist.githubusercontent.com/rashmiswaroop10/012403550d28849cea886378801aaa45/raw/9e068f4fadf26aa7c9791ca6ae20cacfb90b6904/text1.txt',
'https://gist.githubusercontent.com/rashmiswaroop10/7ffe171e93071cab8aad9c338c24aea1/raw/74ac846d5c0a8f2b287578ce7862bf006ac05387/text3.txt',
'https://gist.githubusercontent.com/rashmiswaroop10/8086af919f6da231bd458edc6f7ef749/raw/02b7eddfbf778252c613ab50b50258af3bda7554/text2.txt'
))
    