from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("Smile-Detection/WebCrawler/chromedriver")

driver.get("https://m.place.naver.com/my/feed")

driver.implicitly_wait(3000)

category_buttons = driver.find_elements(By.CLASS_NAME, '_1gPsI')


imgs = []
reviews = []
for category_button in category_buttons:
    category_button.click()
    time.sleep(3)
    '''
    if category_buttons.index(category_button) == 9:
        driver.find_element("xpath", '//*[@id="app-root"]/div[3]/div/div[2]/div/div/button[2]/span').click()
    '''
    
    posts = driver.find_elements(By.CLASS_NAME, "nNbDE")
    for post in posts:
        imgs.append(post.find_elements(By.CLASS_NAME, "_2WWdU"))
        reviews.append(post.find_element(By.CLASS_NAME, "_7nYoZ").text)


print(len(reviews))