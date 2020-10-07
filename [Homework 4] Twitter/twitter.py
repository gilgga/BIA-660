"""
* Name:
* Description: BIA-660-WS Homework 4 - Twitter
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""

from selenium import webdriver
import time
import csv


def getTweets( link1, link2 ):
    driver = webdriver.Chrome('chromedriver.exe')

    # *** Get the first 30 Tweets from Link 1
    driver.get( link1 )
    time.sleep(2)

    link1_already_seen = set()#keeps track of tweets we have already seen.
    link1_tweets_and_commentsCount = {}
    link1_tweet_index = 0

    # Store Link 1 Tweets and Comments Counts in Dictionary
    while( link1_tweet_index < 30 ):

        #find all elements that have the value "tweet" for the data-testid attribute
        tweets=driver.find_elements_by_css_selector('div[data-testid="tweet"]')#
        print(len(tweets),' tweets found\n')


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
                retweetElement=tweet.find_element_by_css_selector('div[data-testid="reply"]')

                #find the span element that has all the specified values (space separated) in its class attribute
                comments=retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text

            except:
                print ('no comments')

            #only write tweets that have text or retweets (or both).
            if txt != 'NA' or comments != 'NA':
                if ( link1_tweet_index < 30 ):
                    link1_tweet_index = link1_tweet_index + 1
                    link1_tweets_and_commentsCount[link1_tweet_index] = {'tweet': txt, 'comments': comments}
                else:
                    break

        if ( link1_tweet_index < 30 ):
            #scroll down twice to load more tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break

        time.sleep(2)

    print(link1_tweets_and_commentsCount)

    # *** Get the first 30 Tweets from Link 2
    driver.get( link2 )
    time.sleep(2)

    link2_already_seen = set()#keeps track of tweets we have already seen.
    link2_tweets_and_likesCount = {}
    link2_tweet_index = 0

    # Store Link 1 Tweets and Comments Counts in Dictionary
    while( link2_tweet_index < 30 ):

        #find all elements that have the value "tweet" for the data-testid attribute
        link2_tweets=driver.find_elements_by_css_selector('div[data-testid="tweet"]')#
        print(len(link2_tweets),' tweets found\n')

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
                retweetElement=tweet.find_element_by_css_selector('div[data-testid="like"]')

                #find the span element that has all the specified values (space separated) in its class attribute
                likes=retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text

            except:
                print ('no likes')

            #only write tweets that have text or retweets (or both).
            if txt != 'NA' or likes != 'NA':
                if ( link2_tweet_index < 30 ):
                    link2_tweet_index = link2_tweet_index + 1
                    link2_tweets_and_likesCount[link2_tweet_index] = {'tweet': txt, 'likes': likes}
                else:
                    break

        if ( link2_tweet_index < 30 ):
            #scroll down twice to load more tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break

        time.sleep(2)

    print(link2_tweets_and_likesCount)


    # *** Get post from Link 1 with the Most Comments (Call it tweet1)


    # *** Get post from Link 2 with the Most Likes (Call it tweet2)


    # *** Process and Clean Up Tweet Text from Link 1


    # *** Process and Clean Up Tweet Text from Link 2



    # *** Create set of words from Tweet Text from Link 1


    # *** Create set of words from Tweet Text from Link 2



    # *** Create the set of words that appear in the text of both tweet1 and tweet2


    # *** Return set of words that appear in the text of both tweet1 and tweet2
    return

getTweets('https://twitter.com/SHAQ', 'https://twitter.com/DwyaneWade')