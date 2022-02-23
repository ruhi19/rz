from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
webD = webdriver.Chrome("chromedriver.exe")
url = 'https://www.amazon.in/s?i=sporting&bbn=4730577031&rh=n%3A4730577031%2Cp_89%3AGarmin&dc&qid=1644590353&rnid=3837712031&ref=sr_pg_1'
webD.get(url)
brnd_name = "Garmin"
fields = ['Name', 'Ratings', 'Reviews', 'Description', 'Variation', 'Main_Image', 'Link', 'Timestamp']
filename = "garmin.csv"
with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	no_of_pages = len(webD.find_elements(By.CLASS_NAME, "s-pagination-item"))-2
	print(no_of_pages)
	for k in range(0, no_of_pages):
		try:
			pages = webD.find_element(By.CLASS_NAME, "s-pagination-next")
			no_of_elements = len(webD.find_elements(By.CLASS_NAME, "sg-col-inner"))
			for i in range(3, no_of_elements):
				print(i)
				try:
					j = i-3
					image_link= webD.find_elements(By.CLASS_NAME, "s-image")[j].get_attribute('src')
					print(image_link)
					page_data = webD.find_elements(By.CLASS_NAME, "sg-col-inner")[i]
					details_link = page_data.find_element(By.TAG_NAME,"a").get_attribute('href')
					print(details_link)
					# Open a new window
					# webD.execute_script("window.open('');")
					# Switch to the new window and open new URL
					page_data.find_element(By.TAG_NAME,"a").click()
					webD.switch_to.window(webD.window_handles[1])
					webD.get(details_link)
					product_title = webD.find_element(By.ID , "productTitle").text
					print(product_title)
					description = webD.find_element(By.ID , "feature-bullets").text
					print(description)
					ratings = ""
					reviews_link = ""
					try:
						reviews_link = webD.find_element(By.ID , "reviews-medley-footer").find_element(By.TAG_NAME,"a").get_attribute('href')
						print(reviews_link)
					except:
						reviews_link = ""
						print("No reviews")
					actual_rating = total_ratings = 0
					try:
						actual_rating = webD.find_element(By.CLASS_NAME , "averageStarRatingNumerical").text
					except Exception as e:
						print(e)
					# print(actual_rating.text)
					try:
						total_ratings = webD.find_element(By.CLASS_NAME, "averageStarRating").text
					except Exception as e:
						print(e)
					# print(total_ratings.text)
					ratings = {
							   "actual_rating": actual_rating,
							   "total_ratings": total_ratings,
							   "total_reviews": total_ratings
							  }
					try:
						variations_div = webD.find_element(By.CLASS_NAME, "imageSwatches")
						colour_variations = variations_div.find_elements(By.TAG_NAME, "li")
						variation_details = []
						for colour in colour_variations:
							colour.click()
							time.sleep(2)
							for m in range(3,7):
								image_link1 = webD.find_elements(By.CLASS_NAME, "a-dynamic-image")[m].get_attribute('src')
								print(image_link1)
							colour_name = ""
							try:
								colour_div = webD.find_element(By.ID , "productOverview_feature_div").find_element(By.TAG_NAME, "table")
								colour_div = colour_div.find_elements(By.TAG_NAME , "tr")
								for c_div in colour_div:
									tag_name = c_div.find_elements(By.TAG_NAME, "td")[0].text
									if tag_name =="Colour":
										colour_name = c_div.find_elements(By.TAG_NAME, "td")[1].text
							except Exception as e:
								print(e)
							print(colour_name)
							actual_price = final_price = 0
							try:
								price_div = webD.find_element(By.ID, "apex_desktop")
								price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
								final_price = price_div[0].text.split("\n")[0]
								print(final_price)
								actual_price = price_div[1].text
								print(actual_price)
							except Exception as e:
								actual_price = final_price
								print(e)
							try:
								discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text
								print(discount[1:3])
							except:
								discount = 0
							
							variation_details.append({'brand': brnd_name, 'colour': colour_name, 'actual_price': actual_price, 'final_price': final_price, 'discount': discount})
					except:
						print("Only one colour present")
						variation_details = []
						colour_name = ""
						try:
							colour_div = webD.find_element(By.ID , "productOverview_feature_div").find_element(By.TAG_NAME, "table")
							colour_div = colour_div.find_elements(By.TAG_NAME , "tr")
							images2 = webD.find_element(By.CLASS_NAME, "regularAltImageViewLayout")
							for l in range(3,7):
								image_link2 = webD.find_elements(By.CLASS_NAME, "a-dynamic-image")[l].get_attribute('src')
								print(image_link2)
							for c_div in colour_div:
								tag_name = c_div.find_elements(By.TAG_NAME, "td")[0].text
								if tag_name == "Colour":
									colour_name = c_div.find_elements(By.TAG_NAME, "td")[1].text
						except Exception as e:
							print(e)
						print(colour_name)
						actual_price = final_price = 0
						try:
							price_div = webD.find_element(By.ID, "apex_desktop")
							price_div = price_div.find_elements(By.CLASS_NAME, "a-price")
							final_price = price_div[0].text.split("\n")[0]
							print(final_price[1:])
							actual_price = price_div[1].text
							print(actual_price[1:])
						except Exception as e:
							print(e)
							actual_price = final_price

						try:
							discount = webD.find_element(By.CLASS_NAME, "savingsPercentage").text[1:3]
						except:
							discount = 0
						variation_details.append({'brand': brnd_name, 'colour': colour_name, 'actual_price': actual_price, 'final_price': final_price, 'discount': discount})
						print(discount)
					csvwriter.writerow([product_title, ratings, reviews_link, description, variation_details, image_link, details_link, time.time()])
					webD.close()
					webD.switch_to.window(webD.window_handles[0])
				except Exception as e:
					print(e)
					print("**************************************")
				print("----------------------------------------------------------------------------------------------------------------")
			pages.click()
			time.sleep(2)
		except:
			pages=webD.find_element(By.CLASS_NAME,"s-pagination-disabled")
			print("This is the last page")
