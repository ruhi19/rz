from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/'

uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser

page_soup=soup(page_html,"html.parser")
container=page_soup.findAll("ul",{"class":"items"})
for title in container:
	name=title.find('li').text
	print(name)
	link=title.get('href')
	print(link)

#for author, year, get button

container1=page_soup.findAll("div",{"class":"insert-details"})
for p in container1:
	author_and_year = container1.findAll('p').text
	print(author_and_year)





    

