from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
import time
url = 'https://www.amazon.in/s?i=shoes&bbn=1983550031&rh=n%3A1983550031%2Cp_89%3ASkechers&dc&fs=true&qid=1619780989&rnid=3837712031&ref=sr_nr_p_89_18'
webD =  webdriver.Chrome("chromedriver.exe")
webD.get(url)
no_of_pages=len(webD.find_elements(By.CLASS_NAME,"s-pagination-item"))-2
print(no_of_pages)
for k in range(0,no_of_pages):
	try:
		pages = webD.find_element(By.CLASS_NAME , "s-pagination-next")
		no_of_elements = len(webD.find_elements(By.CLASS_NAME, "sg-col-inner"))
		for i in range(3,no_of_elements):			
			print(i)
			try:
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
				product_title = webD.find_element(By.ID , "productTitle")
				print(product_title.text)
				description = webD.find_element(By.ID , "feature-bullets")
				print(description.text)
				try:
					reviews_link = webD.find_element(By.ID , "reviews-medley-footer").find_element(By.TAG_NAME,"a").get_attribute('href')
					print(reviews_link)
				except:
					print("No reviews")
				actual_rating = webD.find_element(By.CLASS_NAME , "averageStarRatingNumerical")
				print(actual_rating.text)
				total_rating = webD.find_element(By.CLASS_NAME, "AverageCustomerReviews")
				print(total_rating.text)
				try:
					variations_div= webD.find_element(By.CLASS_NAME, "imageSwatches")
					colour_variations = variations_div.find_elements(By.TAG_NAME, "li")
					for colour in colour_variations:
						colour.click()
						time.sleep(2)
				except:
					print("There are no variations in colour")        
			except:
				print("")
			print("----------------------------------------------------------------------------------------------------------------")
			webD.close()
			webD.switch_to.window(webD.window_handles[0])
		pages.click()
		time.sleep(2)
	except:
		pages=webD.find_element(By.CLASS_NAME,"s-pagination-disabled")
		print("This is the last page")
