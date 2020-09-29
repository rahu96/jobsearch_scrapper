
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www.technopark.org/job-search'
r = requests.get(url,verify=False)
soup = BeautifulSoup(r.content,'html.parser')
for l in soup.find_all('tr', {'class' : 'companyList'}):

	

	jobTitle = l.a.text
	jobLink = l.a['href']
	company = l.select('a')[1].text
	companyLink = l.select('a')[1]['href']
	
	print(f"Job: {jobTitle} , link: technopark.org/{jobLink} ")
	print(f"Company: {company}, Link: technopark.org{companyLink} ")
	
	
	print()