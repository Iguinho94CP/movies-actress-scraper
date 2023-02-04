from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json

with open('/home/igor/projects/scrapers/movies_titles.txt', 'r') as file:
    movie_titles = file.read().splitlines()

driver = webdriver.Chrome()
driver.get('https://google.com')


for i in range(5):
    movie = movie_titles[i]
    search_box = driver.find_element(By.NAME, 'q')
    search_box.clear()
    search_box.send_keys(f'actresses in {movie}')
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    actresses = driver.find_elements(By.CLASS_NAME, 'keP9hb')


    counter = 0
    data = []

    for i in actresses:
        if counter == 3:
            break

        try:
            i.click()
        except selenium.common.exceptions.ElementNotInteractableException:
            print("Element not interactable, moving to next element")
            continue

        time.sleep(5)

        try:
            m = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="JTPWx"]/span[2]/span')))
            m.click()
            time.sleep(15)
        except selenium.common.exceptions.ElementNotInteractableException:
            print("Element not interactable, moving to next element")
            continue

        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        movies = soup.find_all('div', {'class':'Z8r5Gb X8kvh PZPZlf'})
        for j in movies:
            try:
                actress = j.find('span', {'class':'yKMVIe'}).text
            except AttributeError:
                actress = "n/a"
            try:    
                link = j.find('a').get('href')
            except AttributeError:
                link = "n/a"
            try:    
                title = j.find('div', {'class':'JjtOHd'}).text
            except AttributeError:
                title = "n/a"
            try:
                year = j.find('div', {'class':'ellip yF4Rkc AqEFvb'}).text
            except:
                year = 'n/a'
            actress_data = {
                "actress": actress,
                "link": link,
                "title": title,
                "year": year
            }
            data.append(actress_data)
            print(f'Title: {title}\nYear: {year}')

        counter += 1

driver.quit()

with open('data.json', 'w') as f:
    json.dump(data, f)
