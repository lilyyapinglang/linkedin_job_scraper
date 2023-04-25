import csv
import html
import requests
from bs4 import BeautifulSoup
import json

file = open('linkedin-jobs.csv', 'a')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'Apply', 'Description'])
def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']
        print(job_link)
        job_details_response = requests.get(str(job_link))
        #print(job_details_response)
        job_details_soup = BeautifulSoup(job_details_response.content,'html.parser')
        res = job_details_soup.find('script',type="application/ld+json")
        print(html.unescape(json.loads(res.contents[0])))
        job_details=job_details_soup.find('div', class_='description__text description__text--rich')

        #print(job_details)
        writer.writerow([job_title.encode('utf-8'), job_company.encode('utf-8'), job_location.encode('utf-8'),job_link.encode('utf-8'),job_details.encode('utf-8')])
        print('Data updated')
    if page_number <=1000:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number5p8]
        '[[[[]]]]
    else:
        file.close()
        print('File closed')
          
linkedin_scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%20Scientist&location=New%20York%2C%20New%20York%2C%20United%20States&locationId=&geoId=102571732&f_TPR=&f_PP=102571732&distance=25&f_JT=F&f_WT=1%2C3&f_E=2%2C3%2C4&position=1&pageNum=0&start=', 0)
