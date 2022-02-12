from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
import time
webD =  webdriver.Chrome("chromedriver.exe")
url = 'https://www.amazon.in/s?i=sporting&bbn=4730577031&rh=n%3A4730577031%2Cp_89%3AGarmin&dc&qid=1644590353&rnid=3837712031&ref=sr_pg_1'
webD.get(url)	
filename = "garmin.csv"
with open(filename, 'w', newline='') as csvfile:
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	for i in range(4,27):			
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
			total_rating = webD.find_element(By.CLASS_NAME, "averageStarRating")
			print(total_rating.text)
			try:
				variations_div = webD.find_element(By.CLASS_NAME, "imageSwatches")
				colour_variations = variations_div.find_elements(By.TAG_NAME, "li")
				for colour in colour_variations:
					colour.click()
					time.sleep(2)
					colour_div = webD.find_element(By.ID , "productOverview_feature_div").find_element(By.TAG_NAME, "table")
					colour_div = colour_div.find_elements(By.TAG_NAME , "tr")
					for c_div in colour_div:
						tag_name = c_div.find_elements(By.TAG_NAME, "td")[0].text
						if tag_name =="Colour":
							colour_name = c_div.find_elements(By.TAG_NAME, "td")[1].text
					print(colour_name)
					price_div = webD.find_element(By.ID, "apex_desktop")
					price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
					final_price = price_div[0].text.split("\n")[0]
					print(final_price)
					actual_price = price_div[1]
					print(actual_price.text)
					try:
						discount = webD.find_element(By.CLASS_NAME, "savingsPercentage")
					except:
						continue
					print(discount.text)
			except:
				print("Only one colour present")
				colour_div = webD.find_element(By.ID , "productOverview_feature_div").find_element(By.TAG_NAME, "table")
				colour_div = colour_div.find_elements(By.TAG_NAME , "tr")
				for c_div in colour_div:
					tag_name = c_div.find_elements(By.TAG_NAME, "td")[0].text
					if tag_name =="Colour":
						colour_name = c_div.find_elements(By.TAG_NAME, "td")[1].text
				print(colour_name)
				price_div = webD.find_element(By.ID, "apex_desktop")
				price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
				final_price = price_div[0].text.split("\n")[0]
				print(final_price)			
				actual_price = price_div[1]
				print(actual_price.text)
				try:
					discount = webD.find_element(By.CLASS_NAME, "savingsPercentage")
				except:
					continue
				print(discount.text)
		except:
			print("")
		print("----------------------------------------------------------------------------------------------------------------")
		webD.close()
		webD.switch_to.window(webD.window_handles[0])
