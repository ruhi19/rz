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
			movie_link=movie_name.find_element(By.TAG_NAME,"a").get_attribute('href')
			webD.execute_script("window.open('');")

			# Switch to the new window and open new URL
			webD.switch_to.window(webD.window_handles[1])
			webD.get(movie_link)
			director_name=webD.find_element(By.CLASS_NAME,"infobox-data")
			print(director_name)
			webD.close()
			webD.switch_to.window(webD.window_handles[0])

