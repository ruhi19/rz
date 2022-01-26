from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://en.wikipedia.org/wiki/Oreste_Biancoli')
actor_info = webD.find_elements(By.TAG_NAME, "tbody")[0]
date_of_birth = actor_info.find_elements(By.CLASS_NAME , "infobox-data")
print(date_of_birth.text)
