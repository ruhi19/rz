from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
import time
webD =  webdriver.Chrome("chromedriver.exe")
url = 'https://www.amazon.in/s?i=sporting&bbn=4730577031&rh=n%3A4730577031%2Cp_89%3AGarmin&dc&qid=1644590353&rnid=3837712031&ref=sr_pg_1'
webD.get(url)	
no_of_pages = len(webD.find_elements(By.CLASS_NAME, "s-pagination-button"))+1 
pages = webD.find_element(By.CLASS_NAME , "s-pagination-separator")
for k in range(0,no_of_pages):
	pages.click()
