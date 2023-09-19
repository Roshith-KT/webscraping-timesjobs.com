from bs4 import BeautifulSoup
import requests
import os

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

print(' Searching for jobs....')
print(f'{str(len(jobs))} jobs found.....')

for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    
    if 'few' in published_date:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_='srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        
        def writeLine(f):
            f.write(f'Company Name : {company_name.strip()}\n')
            f.write(f'Required Skills : {skills.strip()}\n')
            f.write(f'More Info : {more_info.strip()}\n\n\n')
        
        file_path="./jobs.txt"
        if os.path.exists(file_path):
            with open(file_path,'a') as f:
                writeLine(f)
        else:
            with open(file_path,'w') as f:
                writeLine(f)
            
        
        # print('Company Name : ',company_name.strip())
        # print('Required Skills : ',skills.strip())
        # print('More Info : ',more_info.strip())
        # print('')
        
        # print(f'''
        #     Company Name : {company_name}
        #     Required Skills : {skills} 
        #     published_date : {published_date}
        #     ''')
