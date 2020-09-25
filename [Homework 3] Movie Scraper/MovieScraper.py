# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:25:02 2020

@author: rashmi
"""
from bs4 import BeautifulSoup
import re
import time
import requests
import csv

def run(url):
    fw=open('reviews.txt','w',encoding='utf8') 
    writer=csv.writer(fw,lineterminator='\n')
    
    for i in range(1,3):
        if i==1:
            url = url
        else: url=url+'?type=&sort=&page='+str(i)
        for i in range(5):
            response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            if response: 
                break
            else:time.sleep(2) 
            
        if not response: return None
        html=response.text
        soup = BeautifulSoup(html,'html')
        
        reviews=soup.findAll('div', {'class':'row review_table_row'}) # get all the review divs

        for review in reviews:
            name, rating, source, criticText, date='NA','NA','NA','NA','NA'
            
            name=review.find('a',{'href':re.compile('/critic/')})
            if name: name=name.text.strip()
            else: name='NA'
            
            rating=review.find('div',{'class':'review_icon icon small rotten'})
            if rating : 
                rating ='fresh'
            elif review.find('div',{'class':'review_icon icon small fresh'}):
                rating='rotten'
            else:
                rating='NA'
                

            source=review.find('em',{'class':'subtle critic-publication'})
            if source: source=source.text.strip()
            else: source='NA'
            
            
            criticText=review.find('div',{'class':'the_review'})
            if criticText: criticText=criticText.text.strip()
            else: criticText='NA'
            
            
            date=review.find('div',{'class':re.compile('review-date')})
            if date: date=date.text.strip()
            else: date='NA'
            
            
            writer.writerow([name,rating,source,criticText,date]) # write to file 
    fw.close()
        
        
run('https://www.rottentomatoes.com/m/space_jam/reviews/')
