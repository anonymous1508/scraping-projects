from bs4 import BeautifulSoup
import requests
url='https://www.scrapethissite.com/pages/forms/'
print (requests.get(url))
page =requests.get(url)
BeautifulSoup(page.text,'html')
