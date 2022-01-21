from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/')
n = webD.find_elements(By.CLASS_NAME, "item-list")
for name in n:
	print(name.text)
lnks=webD.find_elements(By.TAG_NAME , "a")
# traverse list
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute('href'))
