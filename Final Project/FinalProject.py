# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:27:47 2020

@author: rjnsa
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import requests
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def getUrl(url):
    
    fw=open('final-project.csv','w',encoding='utf8')
    writer=csv.writer(fw,lineterminator='\n')
    
    for i in range(1,3):
     if i==1:
         url = url
     else: 
         url=url+'&start='+str(i)+'0'
         
     driver = webdriver.Chrome('D:/Fall 2020/BIA 660/week 6/chromedriver_win32/chromedriver.exe')
     driver.get(url)
     jobs = driver.find_elements_by_css_selector('div[class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')
     
     for job in jobs:
         jobTitle, jobSummary='na','na'
         
         #extracting job title and job desc
         jobTitle=job.find_element_by_css_selector('a[data-tn-element="jobTitle"]').text
         jobSummary = job.find_element_by_css_selector('div[class="summary"]').text     
         
         #write to csv
         writer.writerow([jobTitle,jobSummary])
         
         #clean data and tokenize
         cleanData(jobSummary)
         
    fw.close()
    


#tokenize and remove stop words
def cleanData(text):
    text = text.replace("\\n", " ").replace(","," ").replace("."," ")
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(text) 
    print(word_tokens)
    
    filtered_sentence = [w.lower() for w in word_tokens if not w in stop_words] 
    filtered_sentence = [] 
    for w in word_tokens: 
     if w not in stop_words: 
        filtered_sentence.append(w)
        
    

def TrainSplitData(X,y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    
    
    
    
         
     #response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
#     if response: 
#         print(response.text)
         
#        html=response.text
#        soup = BeautifulSoup(html,'html')
#        print(soup)
#        jobs=soup.findAll('div', {'class':'jobsearch-SerpJobCard unifiedRow row result clickcard'})
#        print(jobs)
#        for job in jobs:
#            print("5")
#            title = job.find('a',{'data-tn-element':'jobTitle'})
#            jobTitle = title.text.strip()
#            print("jobTitle: "+jobTitle)
#            
#            desc = job.find('div',{'class':'summary'})
#            jobDesc = desc.text.strip()
#            print("jobDesc: "+jobDesc)
        
        
#     else:time.sleep(2) 
     


getUrl('https://www.indeed.com/jobs?q=data+engineer&l=New+York%2C+NY')

