from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import re

with open('/home/igor/projects/scrapers/movies_titles.txt', 'r') as file:
	movie_titles = file.read().splitlines()

driver = webdriver.Chrome()
driver.get('https://google.com')

for movie in movie_titles:
	search_box = driver.find_element(By.NAME, 'q')
	search_box.clear()
	search_box.send_keys(f'actresses in {movie}')
	search_box.send_keys(Keys.RETURN)
	
	html_source = driver.page_source

	time.sleep(5)

	soup = BeautifulSoup(html_source, 'html.parser')

	actresses = soup.find_all('div', {'class':'mR2gOd'})
	base_link = "https://www.google.com"

	

	for i in actresses:
		# ...

		try:
			actor_element = i.find('a')
			if actor_element:
				actor_link = base_link + actor_element['href']
				driver.get(actor_link)
				html_source = driver.page_source
				soup = BeautifulSoup(html_source, 'html.parser')
				time.sleep(10)
				
				#<div aria-level="2" role="heading">About</div>
				right_card = soup.find_all('div', {'class':'B03h3d V14nKc i8qq8b ptcLIOszQJu__wholepage-card wp-ms'})
				for card in right_card:
					born = card.find('span', {'class':'LrzXr kno-fv wHYlTd z8gr9e'}).text
					print(born)
		except AttributeError:
			# Handle the exception here, for example by logging it or continuing to the next iteration
			continue
