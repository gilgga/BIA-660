# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:16:49 2020

@author: Team 8 Victoria Piskarev, Gil Austria, Rashmi Swaroop, Korey Grabowski, Homa Deilamy
"""

import re
from nltk.corpus import stopwords
import requests
from operator import itemgetter

def run(url1, url2, url3): 
    freq={} # keep the freq of each word in the file 
    freq2={} # keep the freq of each word in the file 
    freq3={}# keep the freq of each word in the file 
    wordoutput = [] #keep a set that satisifes all 3 criteria
    stopLex=set(stopwords.words('english')) # build a set of english stopwords
    
    for i in range(5): # try 5 times
        
        #send a request to access the url
        response=requests.get(url1,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
        response2=requests.get(url2,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
        response3=requests.get(url3,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    

        if response: # explanation on response codes: https://realpython.com/python-requests/#status-codes
            break # we got the file, break the loop
        else: print ('failed attempt',i)
        if response2: # explanation on response codes: https://realpython.com/python-requests/#status-codes
            break # we got the file, break the loop
        else: print ('failed attempt',i)
        if response3: # explanation on response codes: https://realpython.com/python-requests/#status-codes
            break # we got the file, break the loop
        else: print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not response: return None
    if not response2: return None
    if not response3: return None
    text=response.text# read in the text from the file
    text2=response2.text# read in the text from the file
    text3=response3.text# read in the text from the file
    
    text=re.sub('[^a-z]',' ',text.lower()) # replace all non-letter characters  with a space
    text2=re.sub('[^a-z]',' ',text2.lower()) # replace all non-letter characters  with a space
    text3=re.sub('[^a-z]',' ',text3.lower()) # replace all non-letter characters  with a space
    words=text.split(' ') # split to get the words in the text  
    words2=text2.split(' ') # split to get the words in the text 
    words3=text3.split(' ') # split to get the words in the text 
    
    for word in words: # for each word in the sentence 
        if word=='' or word in stopLex:continue # ignore empty words and stopwords 
        else: freq[word]=freq.get(word,0)+1 # update the frequency of the word 
            
    for word in words2: # for each word in the sentence 
        if word=='' or word in stopLex:continue # ignore empty words and stopwords 
        else: freq2[word]=freq2.get(word,0)+1 # update the frequency of the word 

    for word in words3: # for each word in the sentence 
        if word=='' or word in stopLex:continue # ignore empty words and stopwords 
        else: freq3[word]=freq3.get(word,0)+1 # update the frequency of the word 
    
    for word in freq.keys():  #add to output set if word meets all three criteria, ignore KeyError
        try:
            if (freq3[word] > freq2[word]) and (freq2[word] > freq[word]) and (freq2[word] > 0):
               wordoutput.append(word)
        except KeyError: 
            continue
        
    return wordoutput


print(run('https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex1', 'https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex2', 'https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex3'))


