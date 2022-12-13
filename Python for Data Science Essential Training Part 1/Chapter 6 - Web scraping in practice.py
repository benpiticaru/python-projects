from bs4 import BeautifulSoup
import urllib.request as urlrq
import certifi
from IPython.display import HTML
import re

## how to get a webpage into python
r = urlrq.urlopen('https://analytics.usa.gov/', cafile=certifi.where()).read()
soup = BeautifulSoup(r, 'html.parser')
type(soup)

##print(soup.prettify()[:100])

## gets all links from a webpage
## for link in soup.find_all('a'):
 ##  print(link.get('href'))

##print(soup.get_text())

for link in soup.find_all('a', attrs={'herf': re.compile("^http")}):
    print(link)

##type(link)

## This is how to scrape links for a webpage and upload to a file.txt.
file = open("parsed_data.txt", "w")
for link in soup.find_all('a' , attrs={'herf': re.compile("^http")}):
    soup_link = str(link)
    print(soup_link)

    file.write(soup_link)
file.flush
file.close

