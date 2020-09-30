"""
* Name: parser.py
* Description: BIA-660-WS Homework 3 - Movie Scraper
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

# ** Import Statements
from bs4 import BeautifulSoup
import re
import time
import requests
import csv


"""
Accepts a URL to the reviews for a movie on RottenTomatoes
Writes a txt file with the following information in each review on the first two pages
    The Name of the Critic
    The Rating of the Review
    The Source of the Review
    The Text of the Review
    The Date of the Review
"""
def run( url ):

    # ** Create reviews.txt file to hold output
    fw = open( 'reviews.txt', 'w', encoding='utf8' )
    writer = csv.writer( fw, lineterminator='\n' )

    # ** Loop through two pages of reviews
    for p in range(1, 3):
        # Variable which will hold the page html data
        html = None

        # ** Build URL to reviews page
        #   Use the input URL for page 1
        #   Append querys to the input URL for page 2
        if ( p == 1 ):
            pageLink = url
        else:
            pageLink = url + '?type=&sort=&page=' + str(p)


        # ** Send HTTP Request to the webpage 5 Times
        for attempt in range(5):
            response = requests.get( pageLink, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', } )
            if ( response ):
                break
            else:
                time.sleep(2)

        # Return None if all 5 attempts fail
        if ( not response ):
            return None


        # ** Get HTML from response and process using BeautifulSoup
        html = response.text
        soup = BeautifulSoup(html,'html')

        # ** Parse out all the divs with review data
        reviews = soup.findAll('div', {'class':'row review_table_row'})


        # ** Parse each review for the following information
        #   The Name of the Critic
        #   The Rating of the Review
        #   The Source of the Review
        #   The Text of the Review
        #   The Date of the Review
        for review in reviews:
            # Define Variables to hold Review Contents
            critic, rating, source, text, date = 'NA', 'NA', 'NA', 'NA', 'NA'

            # Parse Critic
            criticChunk = review.find( 'a', {'href':re.compile('/critic/')} )
            if ( criticChunk ):
                critic = criticChunk.text.strip()

            # Parse Rating
            if ( review.find( 'div', {'class':'review_icon icon small rotten'} ) ):
                rating = 'rotten'
            elif ( review.find( 'div', {'class':'review_icon icon small fresh'} ) ):
                rating = 'fresh'

            # Parse Source
            sourceChunk = review.find( 'em', {'class':'subtle critic-publication'} )
            if ( sourceChunk ):
                source = sourceChunk.text.strip()

            # Parse Text
            textChunk = review.find( 'div', {'class':'the_review'} )
            if ( textChunk ):
                text = textChunk.text.strip()

            # Parse Date
            dateChunk = review.find( 'div', {'class': 'review-date subtle small'} )
            if ( dateChunk ):
                date = dateChunk.text.strip()


            # ** Write Review Data to reviews.txt file
            writer.writerow( [ critic, rating, source, text, date ] )

    # ** Close reviews.txt and Return
    fw.close()
    return


# run( 'https://www.rottentomatoes.com/m/space_jam/reviews/' )
# run( 'https://www.rottentomatoes.com/m/mulan_2020/reviews' )
# run( 'https://www.rottentomatoes.com/m/promare/reviews' )
# run( 'https://www.rottentomatoes.com/m/venom_2018/reviews' )