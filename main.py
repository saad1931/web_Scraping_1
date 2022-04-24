# Two ways for scraping:
# 1- By API
# 2- HTML Web Scraping using tools like bs4


# Step 0:
# Install Libraies for Scraping: 
# bs4
# html5lib
# requests
from tkinter import ANCHOR
from matplotlib.pyplot import get, title
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"


# Step 1:
# Get the HTML

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#r=requests.get(url)
#htmlContent=r.content
#print(htmlContent)

# Step 2:
# Parse the HTML

#soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify())


# Step 3:
# HTML Tree Traversal 
# Commonly used objects:
# 1- Tag
# 2- NavigableString
# 3- Beautifulsoup
# 4- Comments

# Get the title of HTML page 
title=soup.title

# print(title) # Tag
# print(type(title)) # Soup
# print(type(title.string)) # NavigableString

# For Comment
# markup="<p><!-- comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()


# Get all paragraphs of HTML page 
paras = soup.find_all('p')
print(paras)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Get 1st paragraph of HTML page 
p1 = soup.find('p')
print(p1)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


# Get Classes of any element in the HTML page 
ele = soup.find('p')['class']
print(ele)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


# Get all elements with class lead 
l_class = soup.find_all("p",class_="lead")
print(l_class)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


# Get all Anchor tags of HTML page 
anchors = soup.find_all('a')
print(anchors)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Get all links on page 
all_links=set()
for link in anchors:
    if(link.get('href')!= '#'):
        link_text=url+link.get('href')
        all_links.add(link_text)
        print(link_text)

    
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')


navbarSupportedContent=soup.find( id='__next')
print(navbarSupportedContent.contents)

for elem in navbarSupportedContent.children:
    print(elem)

for elemc in navbarSupportedContent.contents:
    print(elemc)

for eles in navbarSupportedContent.stripped_strings:
    print(eles)