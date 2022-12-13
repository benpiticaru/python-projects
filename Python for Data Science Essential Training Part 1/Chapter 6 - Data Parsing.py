import sys
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re

## This is how you open a url into a readable file in python
with urllib.request.urlopen('https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html') as response:
    html = response.read()

soup = BeautifulSoup(html, 'html')
type(soup)

##print(soup.prettify()[0:300])

## Getting data from a parse tree
text_only = soup.get_text()
##print(text_only)

## Searching and retrieving data from a parse tree
soup.find_all("li")

## Retrieving tags by filtering with keyword arguments
soup.find_all(id='link 7')

## Retriving tags by filtering with string arguments
soup.find_all('ol')

## Retreiving tags by filtering with list objects
soup.find_all(['ol','b'])

## Retrieving tags by filtering with regular expressions
t = re.compile('t')
for tag in soup.find_all(t):
    print(tag.name)

## Retrieving tags with a Boolean value
for tag in soup.find_all(True):
    print(tag.name)

## Retriecing weblinks by filtering with string objects
for link in soup.find_all('a'):
    print(link.get('href'))

## Retrieving string by filtering with regular expressions
soup.find_all(string=re.compile("data"))
