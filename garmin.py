from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
webD =  webdriver.Chrome("chromedriver.exe")
for page in range(1,3):
	webD.get('https://www.amazon.in/s?i=sporting&bbn=4730577031&rh=n%3A4730577031%2Cp_89%3AGarmin&dc&qid=1644519013&rnid=3837712031&ref=sr_pg_' + str(page))	
	for i in range(4,5):
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
		#table = webD.find_element(By.CLASS_NAME, "a-lineitem a-align-top")
		#if(table.find_element(By.TAG_NAME, "td").text != "Deal Price:"):
		#	final_price = webD.find_element(By.CLASS_NAME, "priceToPay")
		#	print(final_price.text)
		#else:
		#	final_price = webD.find_element(By.CLASS_NAME, "apexPriceToPay")
		#	print(final_price.text)
		final_price = webD.find_element(By.CLASS_NAME, "priceToPay")
		print(final_price.text)
		actual_price = webD.find_element(By.CLASS_NAME, "basisPrice").text.split(":")[1]
		print(actual_price)
		discount = webD.find_element(By.CLASS_NAME, "savingsPercentage")
		print(discount.text)
		reviews_link = webD.find_element(By.ID , "reviews-medley-footer").find_element(By.TAG_NAME,"a").get_attribute('href')
		print(reviews_link)
		actual_rating = webD.find_element(By.CLASS_NAME , "averageStarRatingNumerical")
		print(actual_rating.text)
		total_rating = webD.find_element(By.CLASS_NAME, "averageStarRating")
		print(total_rating.text)
		try:
			list_of_variations = webD.find_element(By.CLASS_NAME, "imageSwatches")
			variations = list_of_variations.find_elements(By.TAG_NAME, "li")
			for variation_info in range(0, len(variations))
				variation_info = variations[k].find_elements(By.ID , "productOverview_feature_div")
				colour = webD.variation_info.find_element(By.TAG_NAME, "tr")[3].find_element(By.TAG_NAME, "td")[1].text
				print(colour)
				price = list_of_variations.find_elements(By.CLASS_NAME, "twisterSwatchPrice")
				print(price.text)
		except:
		#for case with no variations
			colour = webD.find_elements(By.ID, "productOverview_feature_div").find_element(By.TAG_NAME, "tr")[3].find_element(By.TAG_NAME, "td")[1].text
			print(colour)
		print("----------------------------------------------------------------------------------------------------------------")
		webD.close()
		webD.switch_to.window(webD.window_handles[0])
