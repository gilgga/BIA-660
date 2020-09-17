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

    # Build a set of english stopwords
    stopLex=set(stopwords.words('english'))

    # Send a request to access links
    # ! Fix this so it works for all 3 links
    for i in range(5): # try 5 times
        response=requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        if response: # explanation on response codes: https://realpython.com/python-requests/#status-codes
            break # we got the file, break the loop
        else: print ('failed attempt for',i)

    # all five attempts failed, return  None
    if not response: return None

    text=response.text# read in the text from the file


    # *** Preprocess/Clean up the text data


    # *** Apply the 3 criteria


    # *** Return the set of words that match the criteria



    return output


# ! Find three links to 3 simple text files that we can use to test our function