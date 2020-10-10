import csv
import requests
from selenium import webdriver
import time
import csv


"""
# The function should accept a single parameter: the link to an amazon product
# Creates a csv file called reviews.csv that should include include all the reviews for the product
"""
def scrape( link ):
    # Windows-formatted ChromeDriver exe
    driver = webdriver.Chrome('D:\Fall 2020\BIA 660\week 6\chromedriver_win32\chromedriver.exe')

    fw = open( 'reviews-test5.csv', 'w', encoding='utf8' )
    writer = csv.writer( fw, lineterminator='\n' )


    # *** Open link to Amazon Product
    driver.get(link)
    time.sleep(10)


    # ** Click "See all Reviews" Link under "Top Reviews from the United States"
    try:
        us_reviews = driver.find_element_by_css_selector('span[data-hook="cr-widget-FocalReviews"]')
        us_review_link = us_reviews.find_element_by_link_text('See all reviews')
        us_review_link.click()
    except:
        print('No reviews')
       
        
    driver.get(driver.current_url)   
    
    while(True):
        reviews = driver.find_elements_by_css_selector('div[data-hook="review"]')
        for review in reviews:
            text, rating = 'NA', 'NA'

            try:
                text = review.find_element_by_css_selector('span[data-hook="review-body"]').text
                print(text)
            except:
                print('Review has no text')

            try:
                ratingElement = review.find_element_by_css_selector('span[class="a-icon-alt"]')
                rating = ratingElement.get_attribute('innerHTML')
                rating = rating[0]
                print(rating)
            except:
                print('Review has no rating')


            if ( text != 'NA' or rating != 'NA' ):
                writer.writerow([text, rating])
                
        try:
            next_page = driver.find_element_by_partial_link_text("Next page")
            next_page.click()
            time.sleep(10)
            driver.get(driver.current_url) 
            
        except:
            print("No next page")
            break
                
    fw.close()
    return

#scrape('https://www.amazon.com/Kempshott-750-Smooth-Paper-Clips/dp/B08CSQ41GX/ref=sr_1_12?dchild=1&keywords=clips&qid=1602360907&sr=8-12')
scrape('https://www.amazon.com/Super-Health-Diet-Last-Will-ebook/dp/B004Y0V9G6/ref=cm_cr_arp_d_product_top?ie=UTF8')
    
    

        