from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/')
#list of classes containing novels
class_list = webD.find_elements(By.CLASS_NAME, "items") 
len_class_list = len(class_list)
fields = ['Name', 'Details link', 'Author name', 'Year released' , 'Purchase Link']
filename = "novels.csv"
with open(filename, '', newline='') as csvfile:
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	for i in range(1,9):
		novels_details = class_list[i].find_elements(By.TAG_NAME, "li")
		for novels in novels_details:
			novel_name = novels.text
			print(novel_name)
			novel_link = novels.find_element(By.TAG_NAME, "a").get_attribute('href')
			print(novel_link)
			
			# Open a new window
			webD.execute_script("window.open('');")

			# Switch to the new window and open new URL
			webD.switch_to.window(webD.window_handles[1])
			webD.get(novel_link)
			novel_info = webD.find_element(By.CLASS_NAME, "post-rail")
			novel_author_name = novel_info.find_elements(By.TAG_NAME, "p")[0]
			novel_author_name = str(novel_author_name.text).split(":")[1]
			novel_year_released = novel_info.find_elements(By.TAG_NAME, "p")[1]
			novel_year_released = str(novel_year_released.text).split(":")[1]
			novel_purchase_link = novel_info.find_element(By.TAG_NAME, "a").get_attribute('href')
			print("Author name:" + novel_author_name)
			print("Year Released:" + novel_year_released)
			print("Purchase Link:" + novel_purchase_link)
			webD.close()
			webD.switch_to.window(webD.window_handles[0])
			# writing the data rows 
			csvwriter.writerow([novel_name , novel_link , novel_author_name , novel_year_released, novel_purchase_link])
