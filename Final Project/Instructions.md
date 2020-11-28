We have created 3 Scripts in Total:
1_scrape.py
2_parse.py
3_classify.py

These three scripts should be run in succession from 1 to 3.

1_scrape.py is used to scrape RAW HTML Job Data from Indeed.com for Data Scientists, Software Engineers, and Data Engineers.
It has all the input data necessary to do contained in a dictionary defined within the code as a global variable.

The only requirement to run this script is that it is within the same fodler as an appropriate chrome driver exe file.

If there are no runtime errors, this script with ideally output three folders:
data+scientist
software+engineer
data+engineer

Each folder will contain 5000+ HTML files for the respective job from all the different queried cities.


2_parse.py is used to process/clean the RAW HTML data scraped during 1_scrape.py and store it in a csv file.

Before running this script, you must rename the folders created during 1_scrape.py as follows:
data+scientist -> Data Scientist
software+engineer -> Software Engineer
data+engineer -> Data Engineer

You must also place these folders in the same directory as the 2_parse.py script.

Using the RAW HTML Job Data from all three folders, a csv file called job_ads.csv will be produced that has two colums:
Text
Job Title

Each Job Ad has one line with one entry for Text and Job Title.
"Text" column has the processed/cleaned job data.  This data has all HTML tags and symbols removed, stop words removed, all extraneous whitespace/new-line characters and non-letter chracters removed, and the jobs titles of "data scientist", "software engineer", and "data engineer" removed.
"Job Title" has the job title associated with the job data.  This is taken from the folder name.


3_classify.py takes the job_ads.csv data and run its through a classifier.

The only requirement to run this file is that it is in the same directory as the job_ads.csv file created during 2_parse.py.

This file will output the accuracy of our model.
