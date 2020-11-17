"""
* Name: 1_scrape.py
* Description: BIA-660-WS Final Project: Script for Scraping Job Data from Indeed.com
* Authors: Team 8: Gil Austria, Homa Deilamy, Korey Grabowski, Rashmi Swaroop, Victoria Piskarev
* Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
"""
from selenium import webdriver
import time
import csv
import os
import re
import sys

# 15000 HTML files for each Job Ad
# Will have full HTML for each Job Description (can just be the single div doesnt have to have full HTML skeleton)


# ***
# HTML_dir = 'Team 8 - Final Project Job Ad Raw HTML'

# *** Dictionary with Job Title and City+State Pairs for each Job
job_city_state_dict = {
    'data-scientist': {
        'city_state_pair': [('San+Jose', 'CA'), ('Bronx', 'NY'), ('Brooklyn', 'NY'), ('Indianapolis', 'IN'), ('Short Hills', 'NJ'), ('Las+Vegas', 'NV'), ('Arlington', 'VA'), ('Nashville', 'TN'), ('Englewood+Cliffs', 'NJ')]
    },
    'software+engineer': {
        'city_state_pair': [('San+Jose', 'CA'), ('Bronx', 'NY')]
    },
    'data+engineer': {
        'city_state_pair': [('San+Jose', 'CA'), ('Bronx', 'NY'), ('Brooklyn', 'NY'), ('Indianapolis', 'IN'), ('Short Hills', 'NJ'), ('Las+Vegas', 'NV'), ('Arlington', 'VA')]
    }
}


def scrape():

    # *** Scrape Data from Indeed
    driver = webdriver.Chrome('chromedriver.exe')

    for job, city_state_pairs in job_city_state_dict.items():
        os.mkdir(job)
        os.chdir(job)
        job_count = 0
        for city_state_pair in city_state_pairs['city_state_pair']:
            url_city = city_state_pair[0]
            url_state = city_state_pair[1]
            base_url = f'https://www.indeed.com/jobs?q={job}&l={url_city}%2C+{url_state}'   # &start=

            driver.get( base_url )

            while ( True ):
                time.sleep(5)

                # # Get all Job Ads on This Page
                All_JobAd_Cards_OnPage = driver.find_elements_by_css_selector('div[class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')

                # # Parse Text and Rating from each Review
                for jobAd_Card in All_JobAd_Cards_OnPage:
                    time.sleep(3)
                    job_count += 1

                    jobAd_Card.click()
                    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                    jobAd_Card_Description_HTML = driver.find_element_by_css_selector('div[class="jobsearch-jobDescriptionText"]').get_attribute('innerHTML')
                    with open(f'{job_count}.html', 'w', encoding='UTF-8') as f:
                        f.write(jobAd_Card_Description_HTML)
                    driver.switch_to.default_content()


                # Get "Next Page" Link
                #   Click the Link if enabled
                #   Break out of Loop if disabled (On the Last Page - All Reviews Found)
                try:
                    Pagination = driver.find_element_by_css_selector("ul[class='pagination-list']")
                    Next_Page_Link = Pagination.find_element_by_css_selector("a[aria-label='Next']")
                    Next_Page_Link.click()
                except: # Last page of reviews and "Next Page" is no longer a link element
                    print('Last page of reviews reached')
                    break

        os.chdir('..')

    return

scrape()