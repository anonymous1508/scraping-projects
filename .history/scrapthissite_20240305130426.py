from bs4 import BeautifulSoup
import requests
url='https://www.scrapethissite.com/pages/forms/'
print (requests.get(url))
page =requests.get(url)
print(BeautifulSoup(page.text,'html'))
