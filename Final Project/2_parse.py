"""
* Name: 2_parse.py
* Description: BIA-660-WS Final Project: Script for Parsing Job Data from Indeed.com (Input comes from 1_scrape.py)
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import time
import csv
import os
import re
import sys
import codecs
from progressbar import ProgressBar


base_dir = 'Team 8 - Final Project Job Ad Raw HTML'
data_scientist_dir = 'Data Scientist'
software_engineer_dir = 'Software Engineer'
data_engineer_dir = 'Data Engineer'

jobAd_dirs = [ data_scientist_dir, software_engineer_dir, data_engineer_dir ]

csv_output = 'job_ads.csv'
headers = ['Text', 'Job Title']


# *** Words to drop from every Job Ad
drop_words = [ 'data scientist', 'software engineer', 'data engineer' ]
stop_words = set(stopwords.words('english'))


# *** Remove non-letter characters, lowercase, remove stop words, and remove drop words
def cleanData( text ):
    text = text.replace("\\n", " ").replace(",", " ").replace(".", " ")
    text = re.sub( '[^a-z]', ' ', text.lower() )
    text_words = text.split(' ')

    cleaned_text = []
    for word in text_words:
        if ( word == '' or word in stop_words ):
            continue # ignore empty words and stopwords
        cleaned_text.append(word)

    cleaned_text_join = ' '.join(cleaned_text)

    for word in drop_words:
        cleaned_text_join = cleaned_text_join.replace(word, "")

    return cleaned_text_join


def parse():

    # *** Create reviews.txt file to hold output
    output = open( csv_output, 'w', encoding='UTF-8' )
    writer = csv.writer( output, lineterminator='\n' )
    writer.writerow(headers)

    # *** For loop that goes into every directory with job Ads and parses them using Beautiful Soup
    os.chdir(base_dir)
    for directory in jobAd_dirs:
        pbar = ProgressBar()
        os.chdir(directory)
        print(f'Parsing {directory} Job Ads')
        for jobAd in pbar(os.listdir(os.getcwd())):
            f = codecs.open( jobAd, 'r', encoding="UTF-8")
            html = f.read()

            soup = BeautifulSoup(html, 'lxml')

            # ** Parse out only the text
            jobAd_text = soup.get_text(separator=' ')

            # ** Clean Up Job Ad Text Data
            clean_jobAd_text = cleanData(jobAd_text)

            # ** Write Review Data to reviews.txt file
            writer.writerow( [ clean_jobAd_text, directory ] )

        os.chdir('..')

    # ** Close reviews.txt and Return
    output.close()

    return


parse()
