from bs4 import BeautifulSoup
import requests
url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
print (requests.get(url))
page =requests.get(url)
soup=BeautifulSoup(page.text,'html') 
soup.find_all('table')
