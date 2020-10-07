"""
* Name:
* Description: BIA-660-WS Homework 4 - Twitter
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

from selenium import webdriver
import time
import csv
import re


def getTweets( link1, link2 ):
    driver = webdriver.Chrome('chromedriver.exe')

    # *** Get the first 30 Tweets with Comment Counts from Link 1
    driver.get( link1 )
    time.sleep(2)

    link1_already_seen = set()  #keeps track of tweets we have already seen.
    link1_tweets_and_commentsCount = {}
    link1_tweet_index = 0

    # Store Link 1 Tweets and Comments Counts in Dictionary
    while( link1_tweet_index < 30 ):

        # Find all elements that have the value "tweet" for the data-testid attribute
        tweets=driver.find_elements_by_css_selector('div[data-testid="tweet"]')#
        # print(len(tweets),' tweets found\n')


        # Process each tweet
        for tweet in tweets:

            if tweet in link1_already_seen:
                continue #we have seen this tweet before while scrolling down, ignore
            link1_already_seen.add(tweet) #first time we see this tweet. Mark as seen and process.

            txt, comments = 'NA', 'NA'

            # ** Find the Tweet Text
            try:
                txt = tweet.find_element_by_css_selector("div.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0").text
                txt = txt.replace('\n', ' ')
            except:
                print ('no text')

            # ** Find the number of comments
            try:

                #find the div element that havs the value "retweet" for the data-testid attribute
                retweetElement = tweet.find_element_by_css_selector('div[data-testid="reply"]')

                #find the span element that has all the specified values (space separated) in its class attribute
                comments = retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text

            except:
                print ('no comments')

            #only write tweets that have text or retweets (or both).
            if txt != 'NA' or comments != 'NA':
                if ( link1_tweet_index < 30 ):
                    link1_tweet_index = link1_tweet_index + 1
                    if ( comments.endswith('K') ):
                        comments = float(comments.rstrip('K')) * 1000
                    elif ( comments.endswith('M') ):
                        comments = float(comments.rstrip('M')) * 1000000
                    link1_tweets_and_commentsCount[link1_tweet_index] = {'tweet': txt, 'comments': int(comments)}
                else:
                    break

        if ( link1_tweet_index < 30 ):
            #scroll down twice to load more tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break

        time.sleep(2)

    print(link1_tweets_and_commentsCount)
    print('\n')

    # *** Get the first 30 Tweets with Like Counts from Link 2
    driver.get( link2 )
    time.sleep(2)

    link2_already_seen = set()#keeps track of tweets we have already seen.
    link2_tweets_and_likesCount = {}
    link2_tweet_index = 0

    # Store Link 1 Tweets and Comments Counts in Dictionary
    while( link2_tweet_index < 30 ):

        #find all elements that have the value "tweet" for the data-testid attribute
        link2_tweets=driver.find_elements_by_css_selector('div[data-testid="tweet"]')#
        # print(len(link2_tweets),' tweets found\n')

        # Process each tweet
        for tweet in link2_tweets:

            if tweet in link2_already_seen:
                continue #we have seen this tweet before while scrolling down, ignore
            link2_already_seen.add(tweet) #first time we see this tweet. Mark as seen and process.

            txt, likes = 'NA', 'NA'

            # ** Find the Tweet Text
            try:
                txt = tweet.find_element_by_css_selector("div.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0").text
                txt = txt.replace('\n', ' ')
            except:
                print ('no text')

            # ** Find the number of comments
            try:

                #find the div element that havs the value "retweet" for the data-testid attribute
                retweetElement = tweet.find_element_by_css_selector('div[data-testid="like"]')

                #find the span element that has all the specified values (space separated) in its class attribute
                likes = retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text

            except:
                print ('no likes')

            #only write tweets that have text or retweets (or both).
            if txt != 'NA' or likes != 'NA':
                if ( link2_tweet_index < 30 ):
                    link2_tweet_index = link2_tweet_index + 1
                    if ( likes.endswith('K') ):
                        likes = float(likes.rstrip('K')) * 1000
                    elif ( likes.endswith('M') ):
                        likes = float(likes.rstrip('M')) * 1000000
                    link2_tweets_and_likesCount[link2_tweet_index] = {'tweet': txt, 'likes': int(likes)}
                else:
                    break

        if ( link2_tweet_index < 30 ):
            #scroll down twice to load more tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break

        time.sleep(2)

    print(link2_tweets_and_likesCount)
    print('\n')


    # *** Get post from Link 1 with the Most Comments (Call it tweet1)
    currentMaxComments = -1
    tweet1 = 'NA'
    for _, tweet_data in link1_tweets_and_commentsCount.items():
        if ( tweet_data['comments'] > currentMaxComments ):
            currentMaxComments = tweet_data['comments']
            tweet1 = tweet_data['tweet']

    print(tweet1)
    print(currentMaxComments)

    # *** Get post from Link 2 with the Most Likes (Call it tweet2)
    currentMaxLikes = -1
    tweet2 = 'NA'
    for _, tweet_data in link2_tweets_and_likesCount.items():
        if ( tweet_data['likes'] > currentMaxLikes ):
            currentMaxLikes = tweet_data['likes']
            tweet2 = tweet_data['tweet']

    print(tweet2)
    print(currentMaxLikes)

    # *** Process and Clean Up Tweet Text
    # Remove all non-alpha characters and lowercase tweet1
    tweet1 = re.sub( '[^a-z]', ' ', tweet1.lower() ) # Replace all non-letter characters with a space; Lowercase all letter characters
    tweet1_words = tweet1.split(' ') # Split to get the words in the text
    print(tweet1_words)

    # Remove all non-alpha characters and lowercase tweet2
    tweet2 = re.sub( '[^a-z]', ' ', tweet2.lower() ) # Replace all non-letter characters with a space; Lowercase all letter characters
    tweet2_words = tweet2.split(' ') # Split to get the words in the text
    print(tweet2_words)

    # *** Create set of words from Tweet Text
    # Create set for tweet1
    tweet1_set = set()
    for word in tweet1_words:
        tweet1_set.add(word)
    print(tweet1_set)

    # Create set for tweet2
    tweet2_set = set()
    for word in tweet2_words:
        tweet2_set.add(word)
    print(tweet2_set)

    # *** Create the set of words that appear in the text of both tweet1 and tweet2
    tweet1_and_tweet2_set = tweet1_set.intersection(tweet2_set)

    # *** Return set of words that appear in the text of both tweet1 and tweet2
    return tweet1_and_tweet2_set

getTweets('https://twitter.com/SHAQ', 'https://twitter.com/DwyaneWade')