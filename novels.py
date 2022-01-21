from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/')
n = webD.find_elements(By.CLASS_NAME, "item-list")
for name in n:
	print(name.text)
