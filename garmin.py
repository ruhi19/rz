from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://www.amazon.in/s?bbn=4730577031&rh=n%3A4730577031%2Cp_89%3AGarmin&dc&qid=1619687558&rnid=3837712031&ref=lp_4730577031_nr_p_89_19')	
for i in range(3,27):
	j=i-3
	image_link = webD.find_elements(By.CLASS_NAME, "s-image")[j].get_attribute('src')
	print(image_link)
	page_data = webD.find_elements(By.CLASS_NAME, "sg-col-inner")[i]
	details_link = page_data.find_element(By.TAG_NAME,"a").get_attribute('href')
	print(details_link)
	# Open a new window
	webD.execute_script("window.open('');")
	# Switch to the new window and open new URL
	webD.switch_to.window(webD.window_handles[1])
	webD.get(details_link)
	#global_ratings = webD.find_element(By.XPATH , "/html/body/div[2]/div[2]/div[5]/div[3]/div[4]/div[1]/div/h1")
	#print(global_ratings)
	#description = webD.find_element(By.CLASS_NAME, "a-unordered-list a-vertical a-spacing-mini")
	print(description.text)
	webD.close()
	webD.switch_to.window(webD.window_handles[0])
