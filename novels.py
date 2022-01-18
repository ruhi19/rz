from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/'

uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser

page_soup=soup(page_html,"html.parser")
container=page_soup.findAll("ul",{"class":"items"})
for x in range (9):
	print(container[x].text)







    
