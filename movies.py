from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import re
webD =  webdriver.Chrome("chromedriver.exe")
webD.get('https://en.wikipedia.org/wiki/List_of_films_considered_the_best')
enitre_page_data = webD.find_elements(By.TAG_NAME, "ul") 
fields = ['Movie Name', 'Year released' , 'Actor name' , 'Date of birth' , 'Years active']
filename = "movies.csv"
with open(filename, 'w', newline='') as csvfile:
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	for i in range(5,6):
			movie_names = enitre_page_data[i].find_elements(By.TAG_NAME, "li")
			for movie_name in movie_names:
				title = str(movie_name.text).split("(")[0]
				print(title)
				try:
					year = re.split("[()]" , movie_name.text)[1]
					print(year)

					movie_link=movie_name.find_element(By.TAG_NAME,"a").get_attribute('href')
					try:
						webD.execute_script("window.open('');")					
						# Switch to the new window and open new URL
						webD.switch_to.window(webD.window_handles[1])
						webD.get(movie_link)
						actors_list = webD.find_elements(By.CLASS_NAME, "plainlist")
						
						for actor_list in actors_list:
							outer_loop = actor_list.find_element(By.XPATH , '../..')
							if(outer_loop.find_element(By.TAG_NAME, "th").text != "Screenplay by") and (outer_loop.find_element(By.TAG_NAME, "th").text != "Starring"):
								continue
							actor_name_and_link = actor_list.find_elements(By.TAG_NAME, "li")
							for actor in actor_name_and_link:
								actor_name = actor.text
								print(actor_name)
								try:
									actor_link = actor.find_element(By.TAG_NAME, "a").get_attribute('href')
								except:
									print("Actor link not found")
									continue
								try:						
									# Open a new window
									webD.execute_script("window.open('');")
									# Switch to the new window and open new URL
									webD.switch_to.window(webD.window_handles[2])
									webD.get(actor_link)
									actor_info = webD.find_elements(By.TAG_NAME, "tbody")[0]
									#for actor_details in actor_info:						
									date_of_birth = actor_info.find_elements(By.CLASS_NAME , "infobox-data")[0]
									print(date_of_birth.text)
									years_active = actor_info.find_elements(By.CLASS_NAME , "infobox-data")[3]
									print(years_active.text)
									print("--------------------------------------------------------------------")
										
								except Exception as e:
									print("actor info not printed")

								csvwriter.writerow([movie_name , year , actor_name, date_of_birth , years_active])
								webD.close()
								webD.switch_to.window(webD.window_handles[1])
								
					except:
						print("actors list not found")
					webD.close()
					webD.switch_to.window(webD.window_handles[0])    
				except Exception as e:
					print("movie name not found")
				print("======================================================================================")
				print("error occured", i)
