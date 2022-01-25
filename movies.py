from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://en.wikipedia.org/wiki/List_of_films_considered_the_best')
enitre_page_data = webD.find_elements(By.TAG_NAME, "ul") 
for i in range(5,84):
		movie_names = enitre_page_data[i].find_elements(By.TAG_NAME, "li")
		for movie_name in movie_names:
			title = str(movie_name.text).split("(")[0]
			print(title)
			year = re.split("[()]" , movie_name.text)[1]
			print(year)
