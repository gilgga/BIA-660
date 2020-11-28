**We have created 3 Scripts in Total:**
- 1_scrape.py
- 2_parse.py
- 3_classify.py

*These three scripts should be run in succession from 1 to 3.*


## 1_scrape.py
This is used to scrape RAW HTML Job Data from Indeed.com for Data Scientists, Software Engineers, and Data Engineers.
It has all the input data necessary to do this contained in a dictionary defined within the code as a global variable.

The only requirement to run this script is that it is within the same directory as an appropriate chrome driver exe file.

If there are no runtime errors, this script will ideally output three folders:
1. data+scientist
2. software+engineer
3. data+engineer

*These folders should also not yet exist before running this script or os.mkdir will throw an error*

*Each folder will contain 5000+ HTML files for the respective job from all the different queried cities.*


## 2_parse.py
This is used to process/clean the RAW HTML data scraped during 1_scrape.py and store it in a csv file.

Before running this script, you must rename the folders created during 1_scrape.py as follows:
- data+scientist -> Data Scientist
- software+engineer -> Software Engineer
- data+engineer -> Data Engineer

*You must also place these folders in the same directory as the 2_parse.py script.*

Using the RAW HTML Job Data from all three folders, a csv file called job_ads.csv will be produced that has two columns:
1. Text
2. Job_Title

Each Job Ad has one line with one entry for Text and Job_Title.
- "Text" column has the processed/cleaned job data.  This data has all HTML tags and symbols removed, stop words removed, all extraneous whitespace/new-line characters and non-letter chracters removed, and the jobs titles of "data scientist", "software engineer", and "data engineer" removed.
- "Job_Title" has the job title associated with the job data.  This is taken from the folder names that you defined above.


## 3_classify.py
This takes as input a test data file.  The test data file is hard-coded at the very bottom of the script when the classify function is called.  **You must change the file name to match the input test data before running the script.**

The only requirement to run this file is that it is in the same directory as the job_ads.csv file created during 2_parse.py and that it is provided the path to a test data file.

This file will output a csv file called "output.csv" which has one labeled column called "predictions" which holds all N predictions for the test data where each i-th prediction corresponds to the i-th job ad in the test file.

*This script will print out its progress on the command line since it takes some time to run the script because of Voting Classifier*
