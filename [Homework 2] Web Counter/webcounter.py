"""
* Name: webcounter.py
* Description: BIA-660-WS Homework 2 - Web Counter
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

import re  # Regular Expressions for searching specific patterns
from nltk.corpus import stopwords  # Popular library for text mining
import requests  # HTTP Requests
from operator import itemgetter  # For sorting different types of lists for different criteria


"""
Returns a set of all the words that satisfy ALL 3 of the following criteria:
    1. They appear at least once in link2
    2. They appear more frequently in link2 than in link1
    3. They appear less frequently in link2 that in link3

    - Ignore case.
    - Remove all non-letter characters before you count
    - Ignore stopwords
"""
def run( link1, link2, link3 ):

    # Will hold the output: the set of all words that satify the 3 criteria
    output = set()

    # Dictionaries that hold the following information
    #   Key: Each word from each link
    #   Value: Frequency of the word
    link1_textfreq = {} # keep the freq of each word in the file
    link2_textfreq = {} # keep the freq of each word in the file
    link3_textfreq = {}# keep the freq of each word in the file

    # Build a set of english stopwords
    stopLex = set(stopwords.words('english'))

    # *** Send a request to access the three input links
    # Link 1
    for attempt in range(5): # try 5 times
        link1_response = requests.get(link1,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        if ( link1_response ):
            break # we got the file, break the loop
        else:
            print (f'Failed attempt {attempt} to access {link1}' )

    # Link 2
    for attempt in range(5): # try 5 times
        link2_response = requests.get(link2,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        if ( link2_response ):
            break # we got the file, break the loop
        else:
            print (f'Failed attempt {attempt} to access {link2}' )

    # Link 3
    for attempt in range(5): # try 5 times
        link3_response = requests.get(link3,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        if ( link3_response ):
            break # we got the file, break the loop
        else:
            print (f'Failed attempt {attempt} to access {link3}' )

    # If any of the three links failed to return a response, return None
    if ( not link1_response or not link2_response or not link3_response ):
        return None


    # *** Read in the text from the three links
    link1_text = link1_response.text
    link2_text = link2_response.text
    link3_text = link3_response.text


    # *** Preprocess/Clean up the text data
    # Clean up Link 1 Text data
    link1_text = re.sub( '[^a-z]', ' ', link1_text.lower() ) # Replace all non-letter characters with a space; Lowercase all letter characters
    link1_words = link1_text.split(' ') # split to get the words in the text

    # Clean up Link 2 Text data
    link2_text = re.sub( '[^a-z]', ' ', link2_text.lower() ) # Replace all non-letter characters with a space; Lowercase all letter characters
    link2_words = link2_text.split(' ') # split to get the words in the text

    # Clean up Link 3 Text data
    link3_text = re.sub( '[^a-z]', ' ', link3_text.lower() ) # Replace all non-letter characters with a space; Lowercase all letter characters
    link3_words = link3_text.split(' ') # split to get the words in the text


    # *** Calculate the Frequency of Each word from each link
    # Link 1
    for word in link1_words:
        if ( word == '' or word in stopLex ):
            continue # ignore empty words and stopwords
        else:
            link1_textfreq[word] = link1_textfreq.get(word,0) + 1 # update the frequency of the word

    # Link 2
    for word in link2_words:
        if ( word == '' or word in stopLex ):
            continue # ignore empty words and stopwords
        else:
            link2_textfreq[word] = link2_textfreq.get(word,0) + 1 # update the frequency of the word

    # Link 3
    for word in link3_words:
        if ( word == '' or word in stopLex ):
            continue # ignore empty words and stopwords
        else:
            link3_textfreq[word] = link3_textfreq.get(word,0) + 1 # update the frequency of the word
    print(link1_textfreq)
    print(link2_textfreq)
    print(link3_textfreq)


    # *** Apply the 3 criteria
    for word in link2_textfreq.keys():
        # print(word)
        # Check if word exists in Link 3 and that the word appears more frequently in Link 3 than in Link 2
        if ( (word in link3_textfreq.keys()) and (link3_textfreq[word] > link2_textfreq[word]) ):
            # Check if the word exists in Link 1
            #   If yes, then check that the word appears more frquently in Link 2 than in Link 1
            #   If no, then automatically add to output (because any appearance of a word in Link 2 is > 0)
            if ( word in link1_textfreq.keys() ):
                if ( link2_textfreq[word] > link1_textfreq[word] ):   # Check that the word appears more frquently in Link 2 than in Link 1
                    output.add(word)
            else:
                output.add(word)



    # *** Return the set of words that match the criteria
    return output


# Test on links to 3 simple text files
print(run
('https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex1',
'https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex2',
'https://raw.githubusercontent.com/victoriapiskarev/bia660txtfilesex/master/ex3'
))
print(run
('https://gist.githubusercontent.com/rashmiswaroop10/012403550d28849cea886378801aaa45/raw/9e068f4fadf26aa7c9791ca6ae20cacfb90b6904/text1.txt',
'https://gist.githubusercontent.com/rashmiswaroop10/7ffe171e93071cab8aad9c338c24aea1/raw/74ac846d5c0a8f2b287578ce7862bf006ac05387/text3.txt',
'https://gist.githubusercontent.com/rashmiswaroop10/8086af919f6da231bd458edc6f7ef749/raw/02b7eddfbf778252c613ab50b50258af3bda7554/text2.txt'
))