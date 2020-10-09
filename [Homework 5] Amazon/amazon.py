"""
* Name: amazon.py
* Description: BIA-660-WS Homework 4 - Amazon
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""


import csv
import requests
from selenium import webdriver
import time


"""
# The function should accept a single parameter: the link to an amazon product
# Creates a csv file called reviews.csv that should include include all the reviews for the product
"""
def scrape( link ):
    # Windows-formatted ChromeDriver exe
    driver = webdriver.Chrome('chromedriver.exe')

    # *** Create reviews.csv file for Writing and Initialize Writer
    reviews_outputfile = open( 'reviews.csv', 'w', encoding='utf8' )
    writer = csv.writer( reviews_outputfile, lineterminator='\n' )


    # *** Open link to Amazon Product
    driver.get( link )
    time.sleep(2)


    # ** Click "See all Reviews" Link under "Top Reviews from the United States"
    try:
        US_All_Reviews_Span = driver.find_element_by_css_selector('span[data-hook="cr-widget-FocalReviews"]')
        US_All_Reviews_Link = US_All_Reviews_Span.find_element_by_link_text('See all reviews')
        US_All_Reviews_Link.click()
    except:
        try:
            OtherCountries_All_Reviews_Span = driver.find_element_by_css_selector('span[data-hook="cr-widget-DesktopGlobalReviews"]')
            OtherCountries_All_Reviews_Link = OtherCountries_All_Reviews_Span.find_element_by_link_text('See all reviews')
            OtherCountries_All_Reviews_Link.click()
        except:
            print('There are No Existing Reviews for this Product')
            reviews_outputfile.close()
            return

    # Attach the new URL to the Driver so we can find elements on the All Reviews Page
    driver.get(driver.current_url)

    # * Get all Reviews on this Page
    # * Click the "Next Page" Link
    # * Repeat until "Next Page" Link is Disabled
    while ( True ):
        time.sleep(2)

        # Get all Reviews on This Page
        All_Reviews_OnPage = driver.find_elements_by_css_selector('div[data-hook="review"]')

        # Parse Text and Rating from each Review
        for review in All_Reviews_OnPage:
            text, rating = 'NA', 'NA'

            try:
                text = review.find_element_by_css_selector('span[data-hook="review-body"]').text
            except:
                print('Review has no text')

            try:
                ratingElement = review.find_element_by_css_selector('span[class="a-icon-alt"]')
                rating = ratingElement.get_attribute('innerHTML')
                rating = rating[0]
            except:
                print('Review has no rating')

            # Only write reviews that have text or rating (or both)
            if ( text != 'NA' or rating != 'NA' ):
                writer.writerow([text, rating])


        # Get "Next Page" Link
        #   Click the Link if enabled
        #   Break out of Loop if disabled (On the Last Page - All Reviews Found)
        try:
            Next_Page_Link = driver.find_element_by_partial_link_text("Next page")
            Next_Page_Link.click()
        except: # Last page of reviews and "Next Page" is no longer a link element
            break


    # Close reviews.csv and return
    reviews_outputfile.close()
    return

scrape('https://www.amazon.com/Sennheiser-Momentum-Cancelling-Headphones-Functionality/dp/B07VW98ZKG')  # Given Example
# scrape('https://www.amazon.com/gp/product/B07ZTRWBDZ/ref=crt_ewc_img_oth_1?ie=UTF8&psc=1&smid=AJD86ZG0LXE8Q')  # Only one page of reviews
# scrape('https://www.amazon.com/gp/product/B08C2D9FGL/ref=crt_ewc_img_dp_3?ie=UTF8&psc=1&smid=A1JW1XF109MUPH')  # No Reviews
# scrape('https://www.amazon.com/Google-GA00439-US-Chromecast-3rd-Generation/dp/B015UKRNGS/ref=sr_1_2?dchild=1&keywords=chromecast&qid=1602279362&sr=8-2')    # 3000+ Reviews