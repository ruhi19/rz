from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
import time
url = 'https://www.amazon.in/s?i=shoes&bbn=1983550031&rh=n%3A1983550031%2Cp_89%3ASkechers&dc&fs=true&qid=1619780989&rnid=3837712031&ref=sr_nr_p_89_18'
webD =  webdriver.Chrome("chromedriver.exe")
webD.get(url)
fields = ['Name', 'Ratings', 'Reviews', 'Description', 'Variation', 'Main_Image', 'Link']
filename = "sketchers.csv"
with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	colours_list = webD.find_elements(By.CLASS_NAME , "s-navigation-item")
	for i in range(77,90):
		colour_link = colours_list[i].get_attribute('href')
		print(colour_link)
		# Open a new window
		webD.execute_script("window.open('');")
		# Switch to the new window and open new URL
		webD.switch_to.window(webD.window_handles[1])
		webD.get(colour_link)
		no_of_pages = len(webD.find_elements(By.CLASS_NAME, "s-pagination-item"))-2
		if (no_of_pages == -2):
			print("only one page present")
			no_of_pages = 1
		for k in range(0,no_of_pages):
			try:
				pages = webD.find_element(By.CLASS_NAME , "s-pagination-next")
				no_of_elements = len(webD.find_elements(By.CLASS_NAME, "sg-col-inner"))
				for i in range(3,5):			
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
						webD.switch_to.window(webD.window_handles[2])
						webD.get(details_link)
						product_title = webD.find_element(By.ID , "productTitle").text
						print(product_title)
						description = webD.find_element(By.ID , "feature-bullets").text
						print(description)
						try:
							reviews_link = webD.find_element(By.ID , "reviews-medley-footer").find_element(By.TAG_NAME,"a").get_attribute('href')
							print(reviews_link)
						except:
							print("No reviews")
						actual_rating = webD.find_element(By.CLASS_NAME , "averageStarRatingNumerical").text
						print(actual_rating)
						total_rating = webD.find_element(By.CLASS_NAME, "AverageCustomerReviews").text
						print(total_rating)
						ratings = {
								   "actual_rating": total_ratings,
								   "total_ratings": actual_rating,
								   "total_reviews": actual_rating
								  }
						try:
							variations_div= webD.find_element(By.CLASS_NAME, "imageSwatches")
							colour_variations = variations_div.find_elements(By.TAG_NAME, "li")
							variation_details = []
							for colour in colour_variations:
								colour.click()
								time.sleep(2)
								variations_div = webD.find_element(By.CLASS_NAME, "imageSwatches")
								try:
									size_div = webD.find_element(By.ID, "native_dropdown_selected_size_name")
									size_options = size_div.find_elements(By.CLASS_NAME, "dropdownAvailable")
									for size in size_options:
										print(size.text)
										size.click()
										actual_price = final_price = 0
										try:
											price_div = webD.find_element(By.ID, "apex_desktop")
											price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
											#final_price = price_div.find_element(By.CLASS_NAME,"apexPriceToPay").text.split("\n")[0]
											final_price = price_div[0].text.split("\n")[0]
											final_price = final_price[1:]
											print(final_price)
											actual_price = price_div[1].text
											actual_price = actual_price[1:]
											print(actual_price)
										except Exception as e:
											actual_price = final_price
											print(e)
										try:
											discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text[1:3]
											print(discount)
										except:
											discount = 0
										time.sleep(2)
								except:
									print("no size variations")
									actual_price = final_price = 0
									try:
										price_div = webD.find_element(By.ID, "apex_desktop")
										price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
										#final_price = price_div.find_element(By.CLASS_NAME,"apexPriceToPay").text.split("\n")[0]
										final_price = price_div[0].text.split("\n")[0]
										final_price = final_price[1:]
										print(final_price)
										actual_price = price_div[1].text
										actual_price = actual_price[1:]
										print(actual_price)
									except Exception as e:
										actual_price = final_price
										print(e)
									try:
										discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text[1:3]
										print(discount)
									except:
										discount = 0
										print(discount)
									variation_details.append({'brand': brnd_name, 'colour': colour_name, 'actual_price': actual_price, 'final_price': final_price, 'discount': discount, 'images': images,'available': 'In Stock'})
						except:
							print("There are no variations in colour")  
							variation_details = []
							try:
								size_div = webD.find_element(By.ID, "native_dropdown_selected_size_name")
								size_options = size_div.find_elements(By.CLASS_NAME, "dropdownAvailable")
								for size in size_options:
									print(size.text)
									size.click()
									actual_price = final_price = 0
									try:
										price_div = webD.find_element(By.ID, "apex_desktop")
										price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
										#final_price = price_div.find_element(By.CLASS_NAME,"apexPriceToPay").text.split("\n")[0]
										final_price = price_div[0].text.split("\n")[0]
										final_price = final_price[1:]
										print(final_price)
										actual_price = price_div[1].text
										actual_price = actual_price[1:]
										print(actual_price)
									except Exception as e:
										actual_price = final_price
										print(e)
									try:
										discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text[1:3]
										print(discount)
									except:
										discount = 0
									variation_details.append({'brand': brnd_name, 'colour': colour_name, 'actual_price': actual_price, 'final_price': final_price, 'discount': discount, 'images': images,'available': 'In Stock'})
									
									time.sleep(2) 
							except:
								print("no size variations")
								actual_price = final_price = 0
								try:
									price_div = webD.find_element(By.ID, "apex_desktop")
									price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
									#final_price = price_div.find_element(By.CLASS_NAME,"apexPriceToPay").text.split("\n")[0]
									final_price = price_div[0].text.split("\n")[0]
									final_price = final_price[1:]
									print(final_price)
									actual_price = price_div[1].text
									actual_price = actual_price[1:]
									print(actual_price)
								except Exception as e:
									actual_price = final_price
									print(e)
								try:
									discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text[1:3]
									print(discount)
								except:
									discount = 0
									print(discount)
								variation_details.append({'brand': brnd_name, 'colour': colour_name, 'actual_price': actual_price, 'final_price': final_price, 'discount': discount, 'images': images,'available': 'In Stock'})
						csvwriter.writerow([product_title, ratings, reviews_link, description, variation_details, image_link, details_link, time.time()])		
					except:
						print("")
					print("----------------------------------------------------------------------------------------------------------------")				
				webD.close()
				webD.switch_to.window(webD.window_handles[1])
				pages.click()
				time.sleep(2)
			except:
				pages=webD.find_element(By.CLASS_NAME,"s-pagination-disabled")
				print("This is the last page")
		webD.close()
		webD.switch_to.window(webD.window_handles[0])
